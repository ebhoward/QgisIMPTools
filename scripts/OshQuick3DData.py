
"""
***************************************************************************
    OshQuick3Data.py
    ---------------------
    Date                 : Nov 2020
    Copyright            : (C) 2020 by Ong See Hai
    Email                : ongseehai at gmail dot com
***************************************************************************
*                                                                         *
*   This program is free software; you can redistribute it and/or modify  *
*   it under the terms of the GNU General Public License as published by  *
*   the Free Software Foundation; either version 2 of the License, or     *
*   (at your option) any later version.                                   *
*                                                                         *
***************************************************************************
"""

__author__ = 'Ong See Hai'
__date__ = 'Nov 2020'
__copyright__ = '(C) 2020, Ong See Hai'

from qgis.PyQt.QtCore import QCoreApplication, QVariant
from qgis.core import (QgsProcessing, 
        QgsProcessingAlgorithm, 
        QgsProcessingContext,
        QgsProcessingException, 
        QgsProcessingParameterMapLayer,
        QgsProcessingParameterNumber,
        QgsProcessingParameterFeatureSink,
        QgsProcessingParameterRasterLayer,
        QgsFeatureSink,
        QgsProcessingUtils, 
        QgsProcessingFeatureSourceDefinition,
        QgsCoordinateReferenceSystem,
        QgsExpressionContextUtils,
        QgsCoordinateReferenceSystem,
        QgsFeature, QgsFeatureRequest,
        QgsField, QgsFields,
        QgsGeometry, 
        QgsPointXY, QgsProject, QgsProperty,
        QgsSpatialIndex,
        QgsVectorLayer
       )
from qgis import processing

class Quick3DData(QgsProcessingAlgorithm):
    INPUT = 'INPUT' 
    INPUT2 = 'INPUT2'
    INPUT3 = 'INPUT3' 
    INPUT4 = 'INPUT4'
    INPUT5 = 'INPUT5'
    INPUT6 = 'INPUT6'
    SLOPEFACTOR = 'SLOPEFACTOR'
    OUTPUT = 'OUTPUT'
    OUTPUT2 = 'OUTPUT2'
    OUTPUT3 = 'OUTPUT3'

    def name(self):
        return 'quick3ddata'
    def displayName(self):
        return 'Quick 3d data'
    def createInstance(self):
        return Quick3DData()
        
    def group(self):
        return 'IMP Tools'

    def groupId(self):
        return 'imp'

    def shortHelpString(self):
        return ( 'Create road, platform and slope polygons with z data for quick 3D visualization \n' 
                 'The Digital elevation model will be clipped to the surrounding area.\n'
                 'The input road node and segment layers must have z values.')

                 
    def initAlgorithm(self, config=None):
        self.addParameter(QgsProcessingParameterMapLayer(
            self.INPUT, 'INPUT: Road casing', 
            types=[QgsProcessing.TypeVectorLine],defaultValue='Casing'))
        self.addParameter(QgsProcessingParameterMapLayer(
            self.INPUT2, 'INPUT2: Platform line',
            types=[QgsProcessing.TypeVectorLine],defaultValue='Platform_line'))
            
        self.addParameter(QgsProcessingParameterMapLayer(
            self.INPUT3, 'INPUT3: Road node',
            types=[QgsProcessing.TypeVectorPoint],defaultValue='Nodez'))
        self.addParameter(QgsProcessingParameterMapLayer(
            self.INPUT4, 'INPUT4: Road segment',
            types=[QgsProcessing.TypeVectorLine],defaultValue='Segmentz'))
        self.addParameter(QgsProcessingParameterMapLayer(
            self.INPUT5, 'INPUT5: Layer with platform elevation',
            types=[QgsProcessing.TypeVectorPolygon],defaultValue='Platformx'))
            
        self.addParameter(QgsProcessingParameterRasterLayer(
            self.INPUT6, 'INPUT6: Digital elevation model',
            defaultValue='DEM_SRTM')) 
            
        self.addParameter(QgsProcessingParameterNumber(
            self.SLOPEFACTOR, 'Slope factor 1:',
            defaultValue='3'))
            
        self.addParameter(QgsProcessingParameterFeatureSink(
            self.OUTPUT, 'Road' ) )
        self.addParameter(QgsProcessingParameterFeatureSink(
            self.OUTPUT2, 'Platform' ) )
        self.addParameter(QgsProcessingParameterFeatureSink(
            self.OUTPUT3, 'Slope' ) )            
            
            
    def processAlgorithm(self, parameters, context, feedback):
    
        maxdistance = 100    # search for nearest Node to line vertex
        
        # Project variables
        project = QgsProject.instance()
        scope = QgsExpressionContextUtils.projectScope(project)
        projfold = scope.variable('project_folder')
        try:
            projcrs = QgsCoordinateReferenceSystem( scope.variable('project_crs') )
        except:
            raise QgsProcessingException ('Project coordinate reference system not set')
        
        caslay = self.parameterAsVectorLayer(parameters,
            self.INPUT, context )
        plolay = self.parameterAsVectorLayer(parameters,
            self.INPUT2, context )  
        nodlay = self.parameterAsVectorLayer(parameters,
            self.INPUT3, context )  
        seglay = self.parameterAsVectorLayer(parameters,
            self.INPUT4, context )  
        plxlay = self.parameterAsVectorLayer(parameters,
            self.INPUT5, context )  
        demlay = self.parameterAsRasterLayer(parameters,
            self.INPUT6, context )
        slopefactor = self.parameterAsDouble(parameters,
            self.SLOPEFACTOR, context ) 
        
        # Road
        flds = QgsFields()
        flds.append( QgsField("plotid", QVariant.Int))
        flds.append( QgsField("luc", QVariant.String))
        (sink, self.dest_id) = self.parameterAsSink ( parameters,
            self.OUTPUT, context,
            flds,
            1003, # polygon Z
            caslay.sourceCrs()  )
            
        # Platform
        flds = QgsFields()
        flds.append( QgsField("plotid", QVariant.Int))
        flds.append( QgsField("platz", QVariant.String))              
        (sink2, self.dest_id2) = self.parameterAsSink ( parameters,
            self.OUTPUT2, context,
            flds,
            1003, # polygon Z
            caslay.sourceCrs()  )

        # Slope
        flds = QgsFields()
        (sink3, self.dest_id3) = self.parameterAsSink ( parameters,
            self.OUTPUT3, context,
            QgsFields(),
            1006, # multipolygon Z
            caslay.sourceCrs()  )      
            
 
    
        
        dic = {}
        nodex = QgsSpatialIndex()
        for f in nodlay.getFeatures():
            dic[ f.id() ] = f.geometry().constGet().z()
            nodex.addFeature(f)

        
        
        # z into casing        
        layer = processing.run("native:setzvalue",
                {'INPUT':caslay,
                'Z_VALUE':0,
                'OUTPUT':'TEMPORARY_OUTPUT'},
                context=context, feedback=feedback, is_child_algorithm=True
                ) ['OUTPUT'] 
        
        layer = processing.run("native:setmvalue",
                {'INPUT':layer,
                'M_VALUE':0,
                'OUTPUT':'TEMPORARY_OUTPUT'},
                context=context, feedback=feedback, is_child_algorithm=True
                ) ['OUTPUT'] 

        cazlay = QgsProcessingUtils.mapLayerFromString(layer, context)   
        sf = cazlay.selectByExpression('ofid > 0')

        # i=0
        cazlay.startEditing()
        for f in cazlay.selectedFeatures():
            # i+=1
            lin = f.geometry().constGet()
            ofid = f['ofid']
            try:
                near0 = nodex.nearestNeighbor( QgsPointXY(lin[0]), 1, maxdistance )
            except:
                continue
            near1 = nodex.nearestNeighbor( QgsPointXY(lin[-1]), 1, maxdistance ) 
            
            z0 = dic[near0[0]]
            z1 = dic[near1[0]]
            lin.setZAt(0,z0)         
            lin.setZAt(-1,z1)
            
            nv = len(lin)
            if nv>2:
                leng = lin.length()
                for v in range(nv-2):
                    vgeom = QgsGeometry(lin[v+1])
                    distv = f.geometry().lineLocatePoint(vgeom)  
                    # distance of current vertex from startpoint
                    zv = z0 + (z1-z0) * distv/leng   
                    # interpolated z for current vertex
                    lin.setZAt(v+1,zv) 
            # print (i,ofid)
            cazlay.updateFeature(f)        
            
        cazlay.commitChanges() 
        
        # Plot line intersect casing
        layer = processing.run('native:splitwithlines', 
                { 'INPUT' : cazlay, 'LINES' : plolay, 
                  'OUTPUT' : 'TEMPORARY_OUTPUT' } , 
                context=context, feedback=feedback, is_child_algorithm=True
                )['OUTPUT']   
        
        caxlay = QgsProcessingUtils.mapLayerFromString(layer, context)   
        caxlay.startEditing()
        
        # Node casing
        sf = caxlay.selectByExpression('id > 0')
        for f in caxlay.selectedFeatures():
            lin = f.geometry().constGet()
            
            near0 = nodex.nearestNeighbor( QgsPointXY(lin[0]), 1, maxdistance )
            near0 = nodex.nearestNeighbor( QgsPointXY(lin[0]), 1, maxdistance )
            
            z = dic[near0[0]]
            
            nv = len(lin)
            for v in range(nv):
                lin.setZAt(v,z)  
            caxlay.updateFeature(f)
            
        caxlay.commitChanges()
        
        # context.addLayerToLoadOnCompletion(caxlay.id(),context.LayerDetails(
                # name='Caxlay',project=context.project() )) 
        
        # Delete plot lines within casing
        pgnlay = processing.run( "native:polygonize", 
                {'INPUT':caxlay,'KEEP_FIELDS':False,
                'OUTPUT':'TEMPORARY_OUTPUT'} ,
                context=context, feedback=feedback, is_child_algorithm=True
                ) ['OUTPUT']
        processing.run("native:createspatialindex",
                {'INPUT':pgnlay },
                context=context, feedback=feedback, is_child_algorithm=True) 

        layer = processing.run("native:joinattributesbylocation", 
                {'INPUT': pgnlay,'JOIN': seglay,
                 'PREDICATE':[0],'METHOD':0,'DISCARD_NONMATCHING':True,'JOIN_FIELDS':'','PREFIX':'',
                'OUTPUT':'TEMPORARY_OUTPUT'},
                context=context, feedback=feedback, is_child_algorithm=True
                ) ['OUTPUT']      
        
        layer = processing.run("native:difference", {
                'INPUT': plolay,
                'OVERLAY': layer,
                'OUTPUT': 'TEMPORARY_OUTPUT'} ,
                context=context,feedback=feedback, is_child_algorithm=True) ['OUTPUT']
        
            
        # Merge casingz_split with plot_line
        layer = processing.run('native:mergevectorlayers', 
                {'CRS': projcrs,
                'LAYERS': [ caxlay, layer ],
                'OUTPUT': 'TEMPORARY_OUTPUT' } ,                
                context=context, feedback=feedback, is_child_algorithm=True
                ) ['OUTPUT'] 
                
        lulay = processing.run( "native:polygonize", 
                {'INPUT':layer,'KEEP_FIELDS':False,
                'OUTPUT':'TEMPORARY_OUTPUT'} ,
                context=context, feedback=feedback, is_child_algorithm=True
                ) ['OUTPUT']
        processing.run("native:createspatialindex",
                {'INPUT':lulay },
                context=context, feedback=feedback, is_child_algorithm=True)        
                
        # Join Node 
        layer = processing.run("native:joinattributesbylocation",
                {'INPUT':lulay,'PREDICATE':[1],
                 'JOIN':nodlay,'METHOD':0 ,
                 'JOIN_FIELDS':'',
                 'DISCARD_NONMATCHING':True,'PREFIX':'',
                 'OUTPUT': 'TEMPORARY_OUTPUT' },
                context=context, feedback=feedback, is_child_algorithm=True
                ) ['OUTPUT']    
        
        alg_params = {
            'FIELDS_MAPPING': [
                {'expression': '$id+1000','length': 0,'name': 'plotid','precision': 0,'type': 4},
                {'expression': '\'rdn\'', 'length': 0,'name': 'luc','precision': 0,'type': 10}  ],
            'INPUT': layer,
            'OUTPUT': 'TEMPORARY_OUTPUT' }
        rdnlay = processing.run('native:refactorfields', alg_params,
            context=context, feedback=feedback, is_child_algorithm=True)['OUTPUT']

        # Join Segment midpoint 
        layer = processing.run("gdal:pointsalonglines", 
                {'INPUT':seglay,'GEOMETRY':'geom',
                'DISTANCE':0.5,'OPTIONS':'',
                'OUTPUT':'TEMPORARY_OUTPUT'},
                context=context, feedback=feedback, is_child_algorithm=True
                ) ['OUTPUT']     

        layer = processing.run("native:joinattributesbylocation", 
                {'INPUT': lulay,'JOIN': layer,
                 'PREDICATE':[1],'METHOD':0,'DISCARD_NONMATCHING':True,'JOIN_FIELDS':'','PREFIX':'',
                 'OUTPUT':'TEMPORARY_OUTPUT'},
                context=context, feedback=feedback, is_child_algorithm=True
                ) ['OUTPUT']   

        alg_params = {
            'FIELDS_MAPPING': [
                {'expression': '$id+2000','length': 0,'name': 'plotid','precision': 0,'type': 4},
                {'expression': '\'rds\'', 'length': 0,'name': 'luc','precision': 0,'type': 10}  ],
            'INPUT': layer,
            'OUTPUT': 'TEMPORARY_OUTPUT' }
        rdslay = processing.run('native:refactorfields', alg_params,
            context=context, feedback=feedback, is_child_algorithm=True)['OUTPUT']
        
        
        # Merge road layers
        rdlay = processing.run('native:mergevectorlayers', 
                {'CRS': projcrs,
                'LAYERS': [ rdnlay, rdslay  ],
                'OUTPUT': 'TEMPORARY_OUTPUT'} ,
                context=context, feedback=feedback, is_child_algorithm=True
                ) ['OUTPUT'] 
                
        rdlay = processing.run("native:filterverticesbyz", 
                {'INPUT': rdlay,
                'MIN':0,'MAX':None,
                'OUTPUT':'TEMPORARY_OUTPUT'},
                context=context, feedback=feedback, is_child_algorithm=True
                ) ['OUTPUT'] 
                

        rdlay = QgsProcessingUtils.mapLayerFromString(rdlay, context) 
        rdlay.selectAll()
        sink.addFeatures(rdlay.selectedFeatures(), QgsFeatureSink.FastInsert)


                
        layer = processing.run("native:difference", {
            'INPUT': lulay,
            'OVERLAY': rdlay,
            'OUTPUT': 'TEMPORARY_OUTPUT'} ,
            context=context,feedback=feedback, is_child_algorithm=True) ['OUTPUT']

        layer = processing.run("native:multiparttosingleparts", {
            'INPUT': layer,
            'OUTPUT': 'TEMPORARY_OUTPUT'},
            context=context,feedback=feedback, is_child_algorithm=True) ['OUTPUT'] 

        alg_params = {
            'FIELDS_MAPPING': [
                {'expression': '$id','length': 0,'name': 'plotid','precision': 0,'type': 4},
                {'expression': '', 'length': 0,'name': 'luc','precision': 0,'type': 10}  ],
            'INPUT': layer,
            'OUTPUT': 'TEMPORARY_OUTPUT'
        }
        pwflay = processing.run('native:refactorfields', alg_params,
            context=context, feedback=feedback, is_child_algorithm=True)['OUTPUT']
            
        # context.addLayerToLoadOnCompletion(pwflay,context.LayerDetails(
                # name='Plot_with_platform',project=context.project() ))
                
        pwflay = QgsProcessingUtils.mapLayerFromString(pwflay, context) 

        
        # point in platformx to get platz
        layer = processing.run("native:pointonsurface", 
                {'INPUT':plxlay,'ALL_PARTS':False,'OUTPUT':'TEMPORARY_OUTPUT'},
                context=context, feedback=feedback, is_child_algorithm=True
                )['OUTPUT']


        # join to plot polygon layer        
        processing.run("native:createspatialindex",
                {'INPUT':pwflay } ,
                context=context, feedback=feedback, is_child_algorithm=True)
        layer = processing.run("native:joinattributesbylocation",
                {'INPUT':pwflay,'PREDICATE':[1],
                 'JOIN':layer,'METHOD':0 ,
                 'JOIN_FIELDS':'',
                 'DISCARD_NONMATCHING':True,'PREFIX':'',
                 'OUTPUT':'TEMPORARY_OUTPUT' },
                context=context, feedback=feedback, is_child_algorithm=True
                ) ['OUTPUT'] 
    
        # Boundary of plot
        layer = processing.run('native:boundary', 
                {'INPUT': layer,
                 'OUTPUT': 'TEMPORARY_OUTPUT' },
                context=context, feedback=feedback, is_child_algorithm=True
                ) ['OUTPUT']

        bdylay = QgsProcessingUtils.mapLayerFromString(layer, context) 
        
        pfmlay = QgsVectorLayer("polygonzm", "Platform", "memory")
        pfmlay.setCrs( caslay.sourceCrs() )

        pfmlay.dataProvider().addAttributes(
                [ QgsField("plotid", QVariant.Int),
                  QgsField("platz",  QVariant.Double)] )
        pfmlay.updateFields()
        pfmlay.startEditing()
        
        for f in bdylay.getFeatures():
            lin = f.geometry().constGet()
            lin.addMValue()
            platz = f['platz']
            for i,v in enumerate(lin):
                zv = v.z()
                m = abs(zv - platz ) * slopefactor
                lin.setMAt(i,m)  
                
            bfmgeom = f.geometry().variableWidthBufferByM(1)
            plotid = f['plotid']
            exp = 'plotid = ' + str(plotid)
            pwflay.selectByExpression(exp)
            pwfgeom = pwflay.selectedFeatures()[0].geometry()
            pfmgeom = pwfgeom.difference(bfmgeom)

            nf = QgsFeature()
            nf.setGeometry(pfmgeom)
            nf.setAttributes([plotid,platz])
            pfmlay.addFeature(nf)

            
        pfmlay.commitChanges() 
        
        pfmlay = processing.run("native:setzvalue", 
                {'INPUT':pfmlay,
                'Z_VALUE':QgsProperty.fromExpression('"platz"'),
                'OUTPUT':'TEMPORARY_OUTPUT'},
                 context=context, feedback=feedback, is_child_algorithm=True
                ) ['OUTPUT']  
                
        pfmlay = QgsProcessingUtils.mapLayerFromString(pfmlay, context) 
        pfmlay.selectAll()
        
        sink2.addFeatures(pfmlay.selectedFeatures(),QgsFeatureSink.FastInsert)

        

        
        layer = processing.run("native:difference", {
                'INPUT': pwflay,
                'OVERLAY': pfmlay,
                'OUTPUT': 'TEMPORARY_OUTPUT'} ,
                context=context,feedback=feedback, is_child_algorithm=True) ['OUTPUT'] 
                
        slplay = processing.run("native:dissolve", 
                {'INPUT':layer,'FIELD':[],
                'OUTPUT':'TEMPORARY_OUTPUT'},
                context=context, feedback=feedback, is_child_algorithm=True
                ) ['OUTPUT'] 
        slplay = QgsProcessingUtils.mapLayerFromString(slplay, context) 
        slplay.selectAll()
        
        sink3.addFeatures(slplay.selectedFeatures(),QgsFeatureSink.FastInsert)   
        

        # Clip raster to surrounding area 
        layer = processing.run('native:mergevectorlayers', 
                {'CRS': projcrs,
                'LAYERS': [ rdlay, pfmlay, slplay ],
                'OUTPUT': 'TEMPORARY_OUTPUT' } ,
                context=context, feedback=feedback, is_child_algorithm=True
                ) ['OUTPUT'] 
                
        raxlay = processing.run("native:polygonfromlayerextent", 
                {'INPUT': demlay,
                'ROUND_TO':0,
                'OUTPUT':'TEMPORARY_OUTPUT'},
                context=context, feedback=feedback, is_child_algorithm=True
                ) ['OUTPUT'] 
                
        layer = processing.run("native:difference", {
                'INPUT': raxlay,
                'OVERLAY': layer,
                'OUTPUT': 'TEMPORARY_OUTPUT'} ,
                context=context,feedback=feedback, is_child_algorithm=True) ['OUTPUT']

        layer = processing.run("gdal:cliprasterbymasklayer", 
                {'INPUT':demlay,'MASK':layer,
                'SOURCE_CRS':None,'TARGET_CRS':None,'NODATA':None,'ALPHA_BAND':False,'CROP_TO_CUTLINE':True,'KEEP_RESOLUTION':False,'SET_RESOLUTION':False,'X_RESOLUTION':None,'Y_RESOLUTION':None,'MULTITHREADING':False,'OPTIONS':'','DATA_TYPE':0,'EXTRA':'',
                'OUTPUT':'TEMPORARY_OUTPUT'},
                context=context,feedback=feedback, is_child_algorithm=True) ['OUTPUT']

        layer = context.addLayerToLoadOnCompletion(layer,context.LayerDetails(
                name='DEM_surrounding',project=context.project() ))
                
        
        feedback.pushInfo( '\n\n ################################\n')
        
        feedback.pushInfo( 'ROAD, PLATFORM AND SLOPE DATA CREATED \n'
                           ' FOR QUICK 3D VISUALIZING \n'
                           'DIGITAL ELEVATION MODEL CLIPPED TO SURROUNDING AREA ')        

        feedback.pushInfo( '\nOshQuick3DData.py v2.1\n'
                           '################################\n')       
                           
                           
        return {self.OUTPUT:self.dest_id, self.OUTPUT2:self.dest_id2, self.OUTPUT3: self.dest_id3 }
        
        
        
    def postProcessAlgorithm(self, context, feedback):
    
        project = QgsProject.instance()
        scope = QgsExpressionContextUtils.projectScope(project)
        projfold = scope.variable('project_folder')
        rdqml = projfold + '\\qsettings\\Road_3d.qml'  
        pfmqml = projfold + '\\qsettings\\Platform_3d.qml'          
        slpqml = projfold + '\\qsettings\\Slope_3d.qml' 
        
        layer = QgsProcessingUtils.mapLayerFromString(self.dest_id, context)
        layer.loadNamedStyle(rdqml)    
        layer = QgsProcessingUtils.mapLayerFromString(self.dest_id2, context)
        layer.loadNamedStyle(pfmqml)
        layer = QgsProcessingUtils.mapLayerFromString(self.dest_id3, context)
        layer.loadNamedStyle(slpqml)           
             

        return {self.OUTPUT:self.dest_id, self.OUTPUT2:self.dest_id2, self.OUTPUT3: self.dest_id3 }


       


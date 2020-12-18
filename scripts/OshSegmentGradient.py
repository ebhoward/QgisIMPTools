
"""
***************************************************************************
    OshSegmentGradient.py
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
        QgsProcessingParameterBoolean,
        QgsProcessingParameterVectorLayer,
        QgsProcessingParameterRasterLayer,
        QgsProcessingParameterNumber,
        QgsProcessingParameterFeatureSink,
        QgsProcessingUtils, 
        QgsFeatureSink
       )
from qgis import processing
from qgis.core import (
        QgsFeature, QgsField, QgsFields, 
        QgsGeometry, QgsGeometryUtils, 
        QgsProject, QgsProperty, QgsVectorLayer,
        QgsExpressionContextUtils,
        QgsSpatialIndex,QgsVertexId,
        QgsLineSymbol, 
        QgsRendererCategory,
        QgsCategorizedSymbolRenderer,        
        )

class SegmentGradient(QgsProcessingAlgorithm):
    
    INPUT = 'INPUT' 
    INPUT2 = 'INPUT2'
    INPUT3 = 'INPUT3' 
    GRADLIM = 'GRADLIM'
    VISOFF = 'VISOFF'

    OUTPUT = 'OUTPUT'
    OUTPUT2 = 'OUTPUT2'
    
    def createInstance(self):
        return SegmentGradient()

    def name(self):
        return 'segmentgradient'

    def displayName(self):
        return 'Segment gradient'

    def group(self):
        return 'Quantum IPMP Tools'

    def groupId(self):
        return 'ipmp'

    def shortHelpString(self):
        return ( 'Calculate road segment gradients\n'
               'Z values from the Digital Elevation Model are inserted into the output road segment endpoints and nodes.'
               '\n'
               'Z values for intermediate vertices in each segment are interpolated from the endpoints by distance along the segment. \n'
               '\n'
               'The input Segment map layer must have lid and wid fields.' )

    def initAlgorithm(self, config=None):

        self.addParameter(QgsProcessingParameterVectorLayer(
                self.INPUT, 'INPUT: Segment',
                [QgsProcessing.TypeVectorLine],'Segment' ) )

        self.addParameter(QgsProcessingParameterVectorLayer(
                self.INPUT2,'INPUT2: Node',
                [QgsProcessing.TypeVectorPoint],'Node' ) )

        self.addParameter(QgsProcessingParameterRasterLayer(
                self.INPUT3,'INPUT3: Digital Elevation Model',
                'DEM_SRTM' ) )

        self.addParameter(QgsProcessingParameterNumber(
                self.GRADLIM,'Highlight segments steeper than 1:' ,
                defaultValue= 25) )

        self.addParameter(QgsProcessingParameterBoolean(
                self.VISOFF,'Turn off other layers ',
                defaultValue=True))    
                
        self.addParameter(
            QgsProcessingParameterFeatureSink(
                self.OUTPUT, 'Segmentz',
                QgsProcessing.TypeVectorAnyGeometry ) )                               
        self.addParameter(
            QgsProcessingParameterFeatureSink(
                self.OUTPUT2, 'Nodez',
                QgsProcessing.TypeVectorAnyGeometry ) )
                
                
    def processAlgorithm(self, parameters, context, feedback):
       
                  
        seglay = self.parameterAsVectorLayer(parameters, self.INPUT, context)
        if seglay is None:
            raise QgsProcessingException(self.invalidSourceError(parameters, self.INPUT))

        nodlay = self.parameterAsVectorLayer(parameters, self.INPUT2, context)
        if nodlay is None:
            raise QgsProcessingException(self.invalidSourceError(parameters, self.INPUT2))
            
        demlay = self.parameterAsRasterLayer(parameters, self.INPUT3, context)
        if demlay is None:
            raise QgsProcessingException(self.invalidSourceError(parameters, self.INPUT3))

        self.gradlim = self.parameterAsInt(parameters, self.GRADLIM, context)  
        if self.gradlim is None:
            raise QgsProcessingException(self.invalidSourceError(parameters, self.GRADLIM))
           
        visibleoff = self.parameterAsBoolean( parameters, self.VISOFF, context )
        
        
        newfields = QgsFields()
        newfields.append(QgsField('lid', QVariant.Int)) 
        newfields.append(QgsField('wid', QVariant.Double)) 
        newfields.append(QgsField('grad', QVariant.Double))         
        newfields.append(QgsField('styl', QVariant.Int))         
        (sink, self.dest_id) = self.parameterAsSink( parameters,
            self.OUTPUT, context,
            newfields,
            seglay.wkbType(),
            seglay.sourceCrs() )

        newfields = QgsFields()
        newfields.append(QgsField('id', QVariant.Int)) 
        newfields.append(QgsField('z', QVariant.Double))   
        (sink2, self.dest_id2) = self.parameterAsSink( parameters,
            self.OUTPUT2, context,
            newfields,
            nodlay.wkbType(),
            nodlay.sourceCrs() )
        
        
        if visibleoff:
            r = QgsProject.instance().layerTreeRoot()
            layers = r.checkedLayers()
            for lay in layers:
                r.findLayer(lay.id()).setItemVisibilityChecked(False)
            

        
        # set Z value from DEM
        layer = processing.run('native:setzfromraster', 
                {'INPUT':nodlay,
                'RASTER': demlay,
                'BAND': 1,
                'NODATA': 0,
                'SCALE': 1,
                'OUTPUT': 'TEMPORARY_OUTPUT' },
                context=context, feedback=feedback, is_child_algorithm=True
                ) ['OUTPUT']

        # Refactor fields
        layer = processing.run('native:refactorfields',
                {'INPUT': layer, 
                 'FIELDS_MAPPING': [
                    {'expression': 'id','length': 0,'name': 'id','precision': 0,'type': 4},
                    {'expression': 'z($geometry)','length': 0,'name': 'z','precision': 0,'type': 6} ],
                 'OUTPUT': 'TEMPORARY_OUTPUT'},
                context=context, feedback=feedback, is_child_algorithm=True
                ) ['OUTPUT']
        
        nodlay = QgsProcessingUtils.mapLayerFromString(layer, context)
        nodlay.selectAll()
        sink2.addFeatures(nodlay.selectedFeatures(),QgsFeatureSink.FastInsert)        

        # nodlay into dict
        d_idz={}
        for f in nodlay.getFeatures():
            id=f.id()
            z=f['z']
            d_idz[id]=z  

        index = QgsSpatialIndex(nodlay.getFeatures())
        k=0
        warnlis = []

        for f in seglay.getFeatures():
            try:
                lid = f['lid']
                wid = f['wid']
            except:
                raise QgsProcessingException('Error! Field: lid or  wid not found in input segment layer')
    
            geom = f.geometry()
            lin = geom.constGet()
            leng = lin.length()
            
            pgeom = QgsGeometry(lin[0])
            nearest = index.nearestNeighbor(pgeom, 1)
            sid = nearest[0]

            sz = d_idz[sid]
            
            pgeom = QgsGeometry(lin[-1])
            nearest = index.nearestNeighbor(pgeom, 1)
            eid = nearest[0]
            ez = d_idz[eid]
            
            lin.addZValue(0)               
            lin.setZAt(0,sz)
            lin.setZAt(-1,ez)
           
            if ez<sz:
                
                geom=QgsGeometry(lin.reversed())
                lin = geom.constGet()
                
                temp = eid
                eid = sid
                sid = temp

                temp = ez
                ez = sz
                sz = temp
            

            
            # insert z into vertices
            n = lin.numPoints()   
            if n > 2:
                for i in range(1,n-1):
                    v = QgsVertexId(0,0,i)
                    d = QgsGeometryUtils.distanceToVertex(lin,v)
                    z = d/leng * (ez-sz) + sz
                    lin.setZAt(i,z)

            seglay.changeGeometry(f.id(), geom)
            
            
            # gradient            
            if ez==sz:
                grad = 9999
            else:
                grad = round(leng/(ez-sz),1)
                
            if grad<(self.gradlim-0.5):
                warnlis.append([lid,grad])
                k+=1
                styl = 1
            else:
                styl = 0
            
            g = QgsFeature()
            g.setGeometry(geom)

            g.setAttributes([lid,wid,grad,styl])
            sink.addFeature(g, QgsFeatureSink.FastInsert)    
            
        feedback.pushInfo( '\n#############################\n\n')
        
        if warnlis:
            for w in warnlis:
                feedback.pushInfo( 'Segment {} gradient  1: {}'.format(w[0],w[1]) )
            
            feedback.pushInfo( '\n' + str(k) + ' STEEP SEGMENTS' ) 
            
        feedback.pushInfo( '\nGRADIENTS CALCULATED FOR {} SEGMENTS'.format(seglay.featureCount()) )

        feedback.pushInfo( '\n\nOshSegmentGradient.py v2.1\n'
                           '#############################\n\n')

        return {self.OUTPUT: self.dest_id}   
        
        
 
    def postProcessAlgorithm(self, context, feedback):
 
        project = QgsProject.instance()
        scope = QgsExpressionContextUtils.projectScope(project)
        path = scope.variable('project_folder')      
        segqml = path + '\\qsettings\\Segment_gradient.qml'

        layer = QgsProcessingUtils.mapLayerFromString(self.dest_id, context)
        layer.loadNamedStyle(segqml)


        # necessary to customize categories based on self.gradlim input
        # default style is only for self.gradlim = 25
        catren = QgsCategorizedSymbolRenderer()
        catren.setClassAttribute('styl')

        linsym1 = QgsLineSymbol.createSimple( {'width':'1','color':'pink'} )
        linsym2 = QgsLineSymbol.createSimple( {'width':'.8','color':'green'} )
        linsym3 = QgsLineSymbol.createSimple( {'width':'.1','color':'blue'} )

        exp1 = 'grad<'+str(self.gradlim-0.5)
        exp2 = 'grad changed'        
        cat1 = QgsRendererCategory('1', linsym1, exp1)
        cat2 = QgsRendererCategory('2', linsym2, exp2)
        cat3 = QgsRendererCategory('0', linsym3, '')

        catren.addCategory(cat1)
        catren.addCategory(cat2)
        catren.addCategory(cat3)

        layer.setRenderer(catren)
        layer.triggerRepaint()  

        

        return {self.OUTPUT: self.dest_id}               
            
            
            
            
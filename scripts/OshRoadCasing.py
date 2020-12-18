
"""
***************************************************************************
    OshRoadCasing.py
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
			 QgsProcessingMultiStepFeedback,
			 QgsProcessingParameterFeatureSink,
			 QgsProcessingParameterMapLayer,
			 QgsProcessingParameterNumber,
			 QgsProcessingParameterVectorDestination,
			 QgsProcessingUtils,
             QgsCoordinateReferenceSystem,
             QgsExpressionContextUtils,
			 QgsField, QgsFields,
			 QgsFeature, QgsFeatureSink,
			 QgsGeometry, QgsGeometryUtils,
			 QgsPointXY, QgsProject, QgsProperty,
			 QgsVector, QgsVectorLayer)
import processing, math

class RoadCasing(QgsProcessingAlgorithm):

    INPUT = 'INPUT'
    INPUT2 = 'INPUT2'
    DISTANCE = 'DISTANCE'
    OUTPUT = 'OUTPUT'
    # OUTPUT2 = 'CHAMFER'
    # OUTPUT3 = 'CHAMFER_POINT'

    def name(self):
        return 'roadcasing'

    def displayName(self):
        return 'Road casing'

    def group(self):
        return 'Quantum IPMP Tools'

    def groupId(self):
        return 'ipmp'

    def createInstance(self):
        return RoadCasing()

    def shortHelpString(self):
        return ( 'Create road casing from road segment center line'
                 '\n'
                 'There should not be any vertex within 50 meters of road nodes, '
                 'otherwise the casings may not be created correctly.'  )



    def initAlgorithm(self, config=None):

        self.addParameter(QgsProcessingParameterMapLayer(
            self.INPUT, 'INPUT: Road segment', 
            types=[QgsProcessing.TypeVectorLine],defaultValue='Segment'))
        self.addParameter(QgsProcessingParameterMapLayer(
            self.INPUT2, 'INPUT2: Road node (junction)',
            types=[QgsProcessing.TypeVectorPoint],defaultValue='Node'))
                
        self.addParameter(QgsProcessingParameterNumber(
            self.DISTANCE, 'Chamfer distance',
            defaultValue='15'))
        
        self.addParameter(QgsProcessingParameterVectorDestination(
            self.OUTPUT, 'Casing', 
            type=QgsProcessing.TypeVectorLine))



    def processAlgorithm(self, parameters, context, feedback):
    
    
        # ignore segment vertex within novtxdis meters of node
        novtxdis = 50
        
        # Project variables
        project = QgsProject.instance()
        scope = QgsExpressionContextUtils.projectScope(project)
        projfold = scope.variable('project_folder')
        try:
            projcrs = QgsCoordinateReferenceSystem( scope.variable('project_crs') )
        except:
            raise QgsProcessingException ('Project coordinate reference system not set')
        
        seglay = self.parameterAsVectorLayer(parameters, 
            self.INPUT, context )
        nodlay = self.parameterAsVectorLayer(parameters,
            self.INPUT2, context )  
        chamdis = self.parameterAsDouble(parameters,
            self.DISTANCE, context )


        chxlay = QgsVectorLayer("point", "chxlay", "memory")
        chxlay.setCrs( nodlay.sourceCrs() )
        pr = chxlay.dataProvider()
        pr.addAttributes([QgsField("id", QVariant.Int),
                          QgsField("chxid",  QVariant.Int)])
        chxlay.updateFields()

        
        
        # Offset lines
        layer = processing.run('native:offsetline', 
                {'DISTANCE' : QgsProperty.fromExpression('wid/2'),
                'INPUT': seglay,       
                'JOIN_STYLE': 1,
                'MITER_LIMIT': 2,
                'SEGMENTS': 1,
                'OUTPUT': 'TEMPORARY_OUTPUT' }, 
                context=context, feedback=feedback, is_child_algorithm=True) ['OUTPUT']

        # ofid
        alg_params = {
            'FIELDS_MAPPING': [
                {'expression': '\"lid\"','length': 0,'name': 'segid','precision': 0,'type': 4},
                {'expression': '\"lid\" + 1000', 'length': 0,'name': 'ofid','precision': 0,'type': 4}
                ],
            'INPUT': layer,
            'OUTPUT': 'TEMPORARY_OUTPUT'
        }
        lay1 = processing.run('native:refactorfields', alg_params,
            context=context, feedback=feedback, is_child_algorithm=True)['OUTPUT']

    
        # Offset lines
        alg_params = {
            'DISTANCE' : QgsProperty.fromExpression('-wid/2'),
            'INPUT': seglay,       
            'JOIN_STYLE': 1,
            'MITER_LIMIT': 2,
            'SEGMENTS': 1,
            'OUTPUT': 'TEMPORARY_OUTPUT'
        }
        layer = processing.run('native:offsetline', alg_params, 
            context=context, feedback=feedback, is_child_algorithm=True) ['OUTPUT']

        # ofid2
        alg_params = {
            'FIELDS_MAPPING': [
                {'expression': '\"lid\"','length': 0,'name': 'segid','precision': 0,'type': 4},
                {'expression': '\"lid\" + 2000','length': 0,'name': 'ofid','precision': 0,'type': 4}
                ],
            'INPUT': layer,
            'OUTPUT': 'TEMPORARY_OUTPUT'
        }
        lay2 = processing.run('native:refactorfields', alg_params,
            context=context, feedback=feedback, is_child_algorithm=True)['OUTPUT']
            
        # Merge vector layers
        alg_params = {
            'CRS': projcrs,
            'LAYERS': [ lay1, lay2 ],
             'OUTPUT': 'TEMPORARY_OUTPUT'
        }
        layer = processing.run('native:mergevectorlayers', alg_params,
            context=context, feedback=feedback, is_child_algorithm=True) ['OUTPUT']
            
        oflay = processing.run("native:createspatialindex", {'INPUT': layer},
            context=context, feedback=feedback, is_child_algorithm=True) ['OUTPUT']
        
        # context.addLayerToLoadOnCompletion(oflay, context.LayerDetails( name='ofl',project=context.project() ))


        
        # Buffer
        alg_params = {
            'DISSOLVE': False,
            'DISTANCE': novtxdis,
            'END_CAP_STYLE': 0,
            'INPUT': nodlay,
            'JOIN_STYLE': 0,
            'MITER_LIMIT': 2,
            'SEGMENTS': 16,
            'OUTPUT': QgsProcessing.TEMPORARY_OUTPUT
        }
        buflay = processing.run('native:buffer', alg_params, 
            context=context, feedback=feedback, is_child_algorithm=True) ['OUTPUT']
            
        # check if intermediate vertices within the novtxdis buffer
        # warning list
        
        layer = processing.run("native:clip", 
            {'INPUT': oflay,
            'OVERLAY': buflay,
            'OUTPUT':'TEMPORARY_OUTPUT'},
            context=context, feedback=feedback, is_child_algorithm=True) ['OUTPUT']

        layer = processing.run("native:multiparttosingleparts", 
            {'INPUT': layer,
            'OUTPUT':'TEMPORARY_OUTPUT'},
            context=context, feedback=feedback, is_child_algorithm=True) ['OUTPUT']
            
        # Calcuate number of vertices
        alg_params = {
            'FIELD_LENGTH': 0,
            'FIELD_NAME': 'numvtx',
            'FIELD_PRECISION': 0,
            'FIELD_TYPE': 1,
            'FORMULA': 'num_points($geometry)',
            'INPUT': layer,
            'OUTPUT': QgsProcessing.TEMPORARY_OUTPUT
            }
        layer = processing.run('native:fieldcalculator', alg_params,
            context=context, feedback=feedback, is_child_algorithm=True) ['OUTPUT']
        
        layer = QgsProcessingUtils.mapLayerFromString(layer, context)
        layer.selectByExpression('numvtx > 2')
        sf= layer.selectedFeatures()
        warnlis = []
        if sf:
            for f in sf:
                warnlis.append( f['segid'] )


        # spoke with angl from seg
        
        # Boundary
        alg_params = {
            'INPUT': buflay,
            'OUTPUT': QgsProcessing.TEMPORARY_OUTPUT
        }
        layer = processing.run('native:boundary', alg_params,
            context=context, feedback=feedback, is_child_algorithm=True)['OUTPUT']
        
        # Line intersections
        alg_params = {
            'INPUT': layer,
            'INPUT_FIELDS': [''],
            'INTERSECT': seglay,
            'INTERSECT_FIELDS': [''],
            'INTERSECT_FIELDS_PREFIX': '',
            'OUTPUT': QgsProcessing.TEMPORARY_OUTPUT
        }
        layer = processing.run('native:lineintersections', alg_params, 
            context=context, feedback=feedback, is_child_algorithm=True)['OUTPUT']
            
        # Field calculator
        alg_params = {
            'FIELD_LENGTH': 0,
            'FIELD_NAME': 'spid',
            'FIELD_PRECISION': 0,
            'FIELD_TYPE': 1,
            'FORMULA': '$id',
            'INPUT': layer,
            'OUTPUT': QgsProcessing.TEMPORARY_OUTPUT
            }
        layer = processing.run('native:fieldcalculator', alg_params,
            context=context, feedback=feedback, is_child_algorithm=True) ['OUTPUT']


        # spoke
        alg_params = {
            'ANTIMERIDIAN_SPLIT': False,
            'GEODESIC': False,
            'GEODESIC_DISTANCE': 1000,
            'HUBS': nodlay,
            #'HUB_FIELDS': '',
            'HUB_FIELDS': 'id',
            'HUB_FIELD': 'id',
            'SPOKES': layer,
            'SPOKE_FIELD': 'id',
            #'SPOKE_FIELDS': '',
            'SPOKE_FIELDS': ['lid','wid','ofid','spid'],
            'OUTPUT': QgsProcessing.TEMPORARY_OUTPUT
        }
        layer = processing.run('native:hublines', alg_params, 
            context=context, feedback=feedback, is_child_algorithm=True) ['OUTPUT']

        # spoke angle
        alg_params = {
            'FIELD_LENGTH': 0,
            'FIELD_NAME': 'angl',
            'FIELD_PRECISION': 0,
            'FIELD_TYPE': 1,
            'FORMULA': 'round( (angle_at_vertex( $geometry,0) ),1)',
            'INPUT': layer,
            'OUTPUT': QgsProcessing.TEMPORARY_OUTPUT
            }
        spklay = processing.run('native:fieldcalculator', alg_params,
            context=context, feedback=feedback, is_child_algorithm=True) ['OUTPUT']
        # context.addLayerToLoadOnCompletion(spklay, context.LayerDetails(
            # name='spk',project=context.project() ))
        
        spklay = QgsProcessingUtils.mapLayerFromString(spklay, context)

        # Offset spoke
        alg_params = {
            'DISTANCE' : QgsProperty.fromExpression('wid/2'),
            'INPUT': spklay,       
            'JOIN_STYLE': 1,
            'MITER_LIMIT': 2,
            'SEGMENTS': 1,
            'OUTPUT': 'TEMPORARY_OUTPUT'
        }
        layer = processing.run('native:offsetline', alg_params, 
            context=context, feedback=feedback, is_child_algorithm=True) ['OUTPUT']                
        
        oflay1 = QgsProcessingUtils.mapLayerFromString(layer, context)
            
        # Offset spoke 2
        alg_params = {
            'DISTANCE' : QgsProperty.fromExpression('-wid/2'),
            #'DISTANCE' : QgsProperty.fromExpression('-wid/2'),
            'INPUT': spklay,       
            'JOIN_STYLE': 1,
            'MITER_LIMIT': 2,
            'SEGMENTS': 1,
            'OUTPUT': 'TEMPORARY_OUTPUT'
        }
        layer= processing.run('native:offsetline', alg_params, 
            context=context, feedback=feedback, is_child_algorithm=True) ['OUTPUT']
            
        
        oflay2 = QgsProcessingUtils.mapLayerFromString(layer, context)
            
        lis = []
        lisid = []
        for f in spklay.getFeatures():
            lis.append (f.attributes() )    
            lisid.append (f['id'] )    
        lisid = list( dict.fromkeys(lisid) )
        
        
        # ofx, chx
        chxlay.startEditing()
        xid = 0
        midpoint = False
        for id in lisid:
        
            exp = 'id=' + str(id)
            
            oflay1.selectByExpression(exp)
            sf = oflay1.selectedFeatures()
            def att(f):
                return f['angl']
            fs1 = sorted(sf, key=att) 
            
        
            # exp = 'id=' + str(id)
            oflay2.selectByExpression(exp)
            sf = oflay2.selectedFeatures()            
            def att(f):
                return f['angl']
            fs2 = sorted(sf, key=att)  

            nseg = len(sf)
            if nseg == 1:       # end Node
                chx = fs1[0].geometry().constGet()[0]
                nf = QgsFeature()
                g = QgsGeometry( chx )
                nf.setGeometry( g )
                nf.setAttributes( [id, xid ] )
                chxlay.addFeature(nf)      
                xid += 1
                
                chx = fs2[0].geometry().constGet()[0]
                nf = QgsFeature()
                g = QgsGeometry( chx )
                nf.setGeometry( g )
                nf.setAttributes( [id, xid ] )
                chxlay.addFeature(nf)      
                xid += 1  
                
                
            else:    
                for n in range(0,nseg): 
                    if nseg>1000:
                        raise QgsProcessingException ('Error: Feature in input layer has more than 1000 vertices')
                        
                    p1 = fs2[n].geometry().constGet()[0]
                    p2 = fs2[n].geometry().constGet()[-1]   
                    segid = fs2[n]['lid']   
                    angtwo = fs2[n]['angl']
                    
                    if n == nseg-1 :
                        feat = fs1[0]
                    else:
                        feat = fs1[n+1]                   

                    segid_2 = feat['lid']  
                    if segid == segid_2:
                        continue
                    angone = feat['angl']  

                    p3 = feat.geometry().constGet()[0] 
                    p4 = feat.geometry().constGet()[-1]             
                   
                    ofx_tup = QgsGeometryUtils.segmentIntersection( p1, p2, p3, p4 ) 
                    p = ofx_tup[1]
                    


                    # 1st intersection: false+point, empty, true+point
                    # if con1.empty   
                        # 2nd intersection: condition2: false+point, empty, true+point
                            # if con2.empty:
                                # create midpoint continue

                    # if not con2.empty:
                        # if almost parallel and p outside bbox
                            # replace with midpoint continue
                        # else not parallel
                            # with true point continue  
                 
                    if p.isEmpty() : # no segment intersection, try line intersection
                        
                        lip_tup = QgsGeometryUtils.lineIntersection(
                            p1, QgsVector( p2.x(),p2.y() ),
                            p3, QgsVector( p4.x(),p4.y() ) )
                        p = lip_tup[1]
                        
                        if p.isEmpty():  
                            # create midpoint and change angl
                            p = QgsGeometryUtils.midpoint( p1, p3 )
                            chamdisadj = chamdis * 1.5
                            temchx = p3.project(chamdisadj,angone)                            
                            a = QgsGeometryUtils.lineAngle( p.x(), p.y(), temchx.x(), temchx.y() )
                            angone = angtwo = math.degrees (a)
                            midpoint = True
                            
                        
                    if not midpoint:
                        if abs( abs(angone - angtwo) - 180) < 7:
                        # almost parallel lines will have faraway intersections
                            bbox = oflay1.boundingBoxOfSelected()
                            bbox.scale(2)
                            # if outside bbox
                            if not bbox.contains( QgsPointXY(p) ) :  
                                # create midpoint and change angl
                                p = QgsGeometryUtils.midpoint( p1, p3 )
                                chamdisadj = chamdis * 1.5
                                temchx = p3.project(chamdisadj,angone)                            
                                a = QgsGeometryUtils.lineAngle( p.x(), p.y(), temchx.x(), temchx.y() )
                                angone = angtwo = math.degrees (a)
                                midpoint = True         
                    
                    ofx = p
                    
                    # nf = QgsFeature()
                    # g = QgsGeometry( ofx )
                    # nf.setGeometry( g )
                    # nf.setAttributes( [id ] )
                    # ofx sink
                    # sink2.addFeature(nf, QgsFeatureSink.FastInsert)
                    

                    if midpoint:
                        temchx = ofx.project ( -chamdisadj, angtwo )
                        chx_tup = QgsGeometryUtils.segmentIntersection( p1, p2, ofx, temchx ) 
                        chx = chx_tup[1]
                    else:
                        chx = ofx.project ( chamdis, angtwo )
               
                    nf = QgsFeature()
                    g = QgsGeometry( chx )
                    nf.setGeometry( g )
                    nf.setAttributes( [id,  xid ] )
                    chxlay.addFeature(nf)
                    xid += 1    
                    
                    if midpoint:
                        temchx = ofx.project ( chamdisadj, angone )
                        chx_tup = QgsGeometryUtils.segmentIntersection( p3, p4, ofx, temchx ) 
                        chx = chx_tup[1]

                        midpoint = False
                        
                    else:
                        chx = ofx.project ( chamdis, angone )

                    nf = QgsFeature()
                    g = QgsGeometry( chx )
                    nf.setGeometry( g )
                    nf.setAttributes( [id, xid ] )
                    chxlay.addFeature(nf)      
                    xid += 1
                    
        chxlay.commitChanges()
        
        # context.addLayerToLoadOnCompletion(chxlay.id(), context.LayerDetails(
            # name='chx',project=context.project() ))                    
                
        # Points to path

        alg_params = {
            'INPUT': chxlay,
            'ORDER_FIELD': 'chxid',
            'GROUP_FIELD': 'id',
            'CLOSE_PATH': True,
            'DATE_FORMAT': '',
            'OUTPUT': 'TEMPORARY_OUTPUT'
        }
        chlay = processing.run('qgis:pointstopath', alg_params, 
            context=context,feedback=feedback, is_child_algorithm=True) ['OUTPUT']
  
        # context.addLayerToLoadOnCompletion(chlay, context.LayerDetails(
            # name='chl',project=context.project() ))         


       
        # ofs Casing
        layer = processing.run("native:difference", {
            'INPUT': oflay,
            'OVERLAY': chlay,
            'OUTPUT': 'TEMPORARY_OUTPUT'} ,
            context=context,feedback=feedback, is_child_algorithm=True) ['OUTPUT']        
        
        layer = processing.run("native:multiparttosingleparts", {
            'INPUT': layer,
            'OUTPUT': 'TEMPORARY_OUTPUT'},
            context=context,feedback=feedback, is_child_algorithm=True) ['OUTPUT'] 
            
        alg_params = {
            'FIELDS_MAPPING': [
                {'expression': '\"segid\"','length': 0,'name': 'segid','precision': 0,'type': 4},
                {'expression': '\"ofid\"', 'length': 0,'name': 'ofid','precision': 0,'type': 4},
                {'expression': '$length', 'length': 0,'name': 'leng','precision': 0,'type': 4}
                ],
            'INPUT': layer,
            'OUTPUT': 'TEMPORARY_OUTPUT'
        }
        layer = processing.run('native:refactorfields', alg_params,
            context=context, feedback=feedback, is_child_algorithm=True)['OUTPUT']
        
        layer = processing.run("qgis:executesql", {
            'INPUT_DATASOURCES': [layer],
            'INPUT_QUERY':'select max(leng),ofid,geometry from input1 group by ofid',
             'INPUT_UID_FIELD':'',
            'INPUT_GEOMETRY_FIELD':'geometry',
            'INPUT_GEOMETRY_TYPE':3,
            'INPUT_GEOMETRY_CRS': projcrs,
            # 'INPUT_GEOMETRY_CRS': projcrs,   error! default to WGS84!
            'OUTPUT': 'TEMPORARY_OUTPUT'},
            context=context,feedback=feedback, is_child_algorithm=True) ['OUTPUT']    
        
        
        ofslay = processing.run("native:snapgeometries", 
                { 'INPUT': layer,
                'REFERENCE_LAYER': chxlay,
                'TOLERANCE': novtxdis,
                'BEHAVIOR':5,
                'OUTPUT': 'TEMPORARY_OUTPUT' },
                context=context,feedback=feedback, is_child_algorithm=True) ['OUTPUT'] 
       
        # context.addLayerToLoadOnCompletion(ofslay,context.LayerDetails(
            # name='ofs',project=context.project() )) 
        

        

        alg_params = {
            'CRS': projcrs,
            'LAYERS': [ chlay, ofslay ],
             'OUTPUT': 'TEMPORARY_OUTPUT'
        }
        layer = processing.run('native:mergevectorlayers', alg_params,
            context=context, feedback=feedback, is_child_algorithm=True) ['OUTPUT'] 
            
        algout = self.parameterAsOutputLayer(parameters, self.OUTPUT, context)
        
        alg_params = {
            'FIELDS_MAPPING': [
                {'expression': '\"fid\"','length': 0,'name': 'fid','precision': 0,'type': 4},
                {'expression': '\"id\"', 'length': 0,'name': 'id','precision': 0,'type': 4},
                {'expression': '\"ofid\"', 'length': 0,'name': 'ofid','precision': 0,'type': 4}
                ],
            'INPUT': layer,
            'OUTPUT': algout
        }
        algoutlay = processing.run('native:refactorfields', alg_params,
            context=context, feedback=feedback, is_child_algorithm=True)['OUTPUT']

        context.addLayerToLoadOnCompletion(algoutlay,context.LayerDetails(
                name='Casing',project=context.project() )) 
            
        feedback.pushInfo( '\n\n #########################################\n')
        
        if warnlis:
            for w in warnlis:
                feedback.pushInfo( 'Segment {} casing has vertex within {} meters of node (junction)'.format(w,novtxdis) )
            
            feedback.pushInfo( '\nWarning: Road casing(s) created may not be correct')

        feedback.pushInfo( '\n\nROAD CASINGS CREATED FOR {} SEGMENTS AND {} NODES'.format(seglay.featureCount(), nodlay.featureCount() ) )
        
        feedback.pushInfo( '\n\nOshRoadCasing.py v2.1\n'
                           '#########################################\n\n')


        
        return {self.OUTPUT: algoutlay} 

        
        


"""
***************************************************************************
    OshNodeSegmentFromRCL.py
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

"""
Create road center line junctions and other road nodes
    Extract road center line start and end points
    + create points at intersection of road center lines
    Create buffer around points
    Dissolve to amalgamate overlapping or nearly overlapping points 
    Create nodes using buffer centroids
    Clip road center lines around junctions to form segments
    
Create road center line segments   
    Delete duplicate geometry 
    Remove duplicate vertices
    Discard lines shorter than 20
    Break road center lines into segments around road nodes with 5m buffer
"""

from qgis.PyQt.QtCore import QCoreApplication, QVariant
from qgis.core import (QgsProcessing, 
        QgsProcessingAlgorithm, 
        QgsProcessingContext,
        QgsProcessingException, 
        QgsProcessingParameterMapLayer,
        QgsProcessingParameterField,
        QgsProcessingParameterFeatureSink,
        QgsFeatureSink,
        QgsProcessingUtils, 
        QgsCoordinateReferenceSystem,
        QgsException,
        QgsExpressionContextUtils,
        QgsFeature, 
        QgsField, QgsFields,
        QgsProject
       )
from qgis import processing

class NodeSegmentFromRCL(QgsProcessingAlgorithm):
    INPUT = 'INPUT' 
    FIELD = 'FIELD'
    # INPUT3 = 'INPUT3' 

    OUTPUT = 'OUTPUT'
    OUTPUT2 = 'OUTPUT2'
    # OUTPUT3 = 'OUTPUT3'

    def name(self):
        return 'nodesegmentfromrcl'
    def displayName(self):
        return 'Node and segment from road center line'
    def createInstance(self):
        return NodeSegmentFromRCL()
        
    def group(self):
        return 'IMP Tools'
    def groupId(self):
        return 'imp'

    def shortHelpString(self):
        return ( 'Create nodes (junctions) and segments from road center lines'
                 ' \n\n'
                 ' The input road center line map layer can be an AutoCAD DXF'
                ' with road lines of different road widths placed in different layers'
               ' with names indicating the road widths, for example, 20, 30, 40 et cetera.  '
                 'For a QGIS map layer, the input road width field should be a string type.  '
                ' \n' 
                 'The input road center lines are broken up to create output road segments and road nodes.  '
                 'Nodes are created around the segment endpoints.'
                 '\n'
                 'The output lines (Segment) and points (Node) do not have z values. '   
                 )

                 
    def initAlgorithm(self, config=None):
        self.addParameter(QgsProcessingParameterMapLayer(
            self.INPUT, 'INPUT: Road center line', 
            types=[QgsProcessing.TypeVectorLine],defaultValue='RCL'))
            
        self.addParameter(QgsProcessingParameterField(
            self.FIELD, 'Road width field', 
            type=QgsProcessingParameterField.String, 
            parentLayerParameterName=self.INPUT,
            allowMultiple=False, defaultValue='Layer'))
 

        self.addParameter(QgsProcessingParameterFeatureSink(
            self.OUTPUT, 'Node' ) )
        self.addParameter(QgsProcessingParameterFeatureSink(
            self.OUTPUT2, 'Segment' ) )
  
            
            
    def processAlgorithm(self, parameters, context, feedback):
    
        # Buffer distance for merge points
        bufdis = 2
        
        # Project variables
        project = QgsProject.instance()
        scope = QgsExpressionContextUtils.projectScope(project)
        projfold = scope.variable('project_folder')
        try:
            projcrs = QgsCoordinateReferenceSystem( scope.variable('project_crs') )
        except:
            raise QgsProcessingException ('Project coordinate reference system not set')
        
        rclay = self.parameterAsVectorLayer(parameters,
            self.INPUT, context )
        widfld = self.parameterAsFields(parameters,
            self.FIELD, context )
        
        # Node
        flds = QgsFields()
        flds.append( QgsField("id", QVariant.Int))
        (sink, dest_id) = self.parameterAsSink ( parameters,
            self.OUTPUT, context,
            flds,
            1, # Point 
            projcrs )
            
        # seg
        flds = QgsFields()
        flds.append( QgsField("lid", QVariant.Int))
        flds.append( QgsField("wid", QVariant.Double))              
        flds.append( QgsField("leng", QVariant.Int))
        (sink2, dest_id2) = self.parameterAsSink ( parameters,
            self.OUTPUT2, context,
            flds,
            2, # linestring
            projcrs  )




        # Extract start end points of road center lines
        endlay = processing.run('native:extractspecificvertices', 
                {'INPUT': rclay, 
                 'VERTICES': '0,-1',
                 'OUTPUT': 'TEMPORARY_OUTPUT' },
                context=context, feedback=feedback, is_child_algorithm=True                 
                ) ['OUTPUT']
        # Intersect road center lines
        layer = processing.run('native:lineintersections',
                {'INPUT': rclay, 'INTERSECT': rclay,
                'INPUT_FIELDS': [''],
                'INTERSECT_FIELDS': [''],
                'INTERSECT_FIELDS_PREFIX': '',
                'OUTPUT': 'TEMPORARY_OUTPUT' },
                context=context, feedback=feedback, is_child_algorithm=True
                ) ['OUTPUT']

        # Merge points
        layer = processing.run('native:mergevectorlayers', 
                {'LAYERS': [endlay,layer],
                'CRS': projcrs,
                'OUTPUT': 'TEMPORARY_OUTPUT' },
                context=context, feedback=feedback, is_child_algorithm=True
                ) ['OUTPUT']

        # Create small dissolved buffer around points
        # to handle multiple points at junctions from not well aligned endpoints
        layer = processing.run('native:buffer', 
                {'INPUT': layer,
                'DISSOLVE': True,
                'DISTANCE': bufdis,
                'END_CAP_STYLE': 0,
                'JOIN_STYLE': 0,
                'MITER_LIMIT': 2,
                'SEGMENTS': 5,
                'OUTPUT': 'TEMPORARY_OUTPUT' },
                context=context, feedback=feedback, is_child_algorithm=True                
                ) ['OUTPUT']
                
        layer = processing.run("native:multiparttosingleparts", 
                {'INPUT': layer,
                'OUTPUT':'TEMPORARY_OUTPUT'},
                context=context, feedback=feedback, is_child_algorithm=True                
                ) ['OUTPUT']

        # Create Node points at buffer centroids
        layer = processing.run('native:centroids', 
                {'INPUT': layer, 
                'ALL_PARTS': True,
                'OUTPUT': 'TEMPORARY_OUTPUT' } ,
                context=context, feedback=feedback, is_child_algorithm=True                
                ) ['OUTPUT']
                
        layer = processing.run("native:deleteduplicategeometries", 
                {'INPUT':layer,
                'OUTPUT': 'TEMPORARY_OUTPUT' },
                context=context, feedback=feedback, is_child_algorithm=True
                ) ['OUTPUT']        


        # Refactor fields
        layer = processing.run('native:refactorfields',
                {'INPUT': layer, 
                 'FIELDS_MAPPING': [
                    {'expression': '$id','length': 0,'name': 'id','precision': 0,'type': 4}
                    #,
                    # {'expression': 'z($geometry)','length': 0,'name': 'z','precision': 0,'type': 6}
                    ],
                 'OUTPUT': 'TEMPORARY_OUTPUT'},
                context=context, feedback=feedback, is_child_algorithm=True
                ) ['OUTPUT']

        nodlay = QgsProcessingUtils.mapLayerFromString(layer, context)
        nodlay.selectAll()
        sink.addFeatures(nodlay.selectedFeatures(),QgsFeatureSink.FastInsert)
        
        
        # Delete duplicate lines
        layer = processing.run("native:deleteduplicategeometries", 
                {'INPUT':rclay,
                'OUTPUT':'TEMPORARY_OUTPUT'}
                ) ['OUTPUT']      

        # Remove duplicate vertices
        layer = processing.run('native:removeduplicatevertices', 
                {'INPUT': layer,
                'TOLERANCE': 5,
                'USE_Z_VALUE': False,
                'OUTPUT': 'TEMPORARY_OUTPUT' },
                context=context, feedback=feedback, is_child_algorithm=True
                )['OUTPUT']

        # Delete shorter than 20
        layer1 = processing.run('native:extractbyexpression', 
                {'EXPRESSION': '$length>20',
                'INPUT': layer,
                'OUTPUT': 'TEMPORARY_OUTPUT' },
                context=context, feedback=feedback, is_child_algorithm=True
                )['OUTPUT']

        # Buffer 5
        layer2 = processing.run('native:buffer', 
                {'INPUT': nodlay,
                'DISSOLVE': False,
                'DISTANCE': 5,
                'END_CAP_STYLE': 0,
                'JOIN_STYLE': 0,
                'MITER_LIMIT': 2,
                'SEGMENTS': 5,
                'OUTPUT': 'TEMPORARY_OUTPUT' },
                context=context, feedback=feedback, is_child_algorithm=True                
                ) ['OUTPUT']
                
        # Trim 5 off segments
        layer = processing.run('native:difference', 
                {'INPUT': layer1,
                'OVERLAY': layer2,
                'OUTPUT': 'TEMPORARY_OUTPUT' },
                context=context, feedback=feedback, is_child_algorithm=True                
                ) ['OUTPUT']

        # Multipart to singleparts
        layer = processing.run('native:multiparttosingleparts', 
                {'INPUT': layer,
                'OUTPUT': 'TEMPORARY_OUTPUT' },
                context=context, feedback=feedback, is_child_algorithm=True                
                ) ['OUTPUT']

        # Refactor fields
        layer = processing.run('native:refactorfields', 
                {'FIELDS_MAPPING': [
                    {'expression': '$id','length': 0,'name': 'lid','precision': 0,'type': 4},
                    {'expression': 'to_real(Layer)','length': 0,'name': 'wid','precision': 0,'type': 6},
                    {'expression': 'round($length,0)','length': 0,'name': 'leng','precision': 0,'type': 4} ],
                'INPUT': layer,
                'OUTPUT': 'TEMPORARY_OUTPUT'},
                context=context, feedback=feedback, is_child_algorithm=True                
                ) ['OUTPUT']
        
        seglay = QgsProcessingUtils.mapLayerFromString(layer, context)
        sink2.addFeatures(seglay.getFeatures(),QgsFeatureSink.FastInsert)       


            
        feedback.pushInfo( '\n\n ####################################\n\n')
        
        feedback.pushInfo( '\n{} SEGMENTS AND {} NODES CREATED'.format(seglay.featureCount(),nodlay.featureCount() ) )

        feedback.pushInfo( '\n\nOshNodeSegmentFromRCL.py v2.1\n' 
                           '####################################\n\n')

        
        return {self.OUTPUT: dest_id, self.OUTPUT2: dest_id2 }



"""
***************************************************************************
    OshPlatformx.py
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

from qgis.core import (QgsProcessing, 
                    QgsProcessingAlgorithm,           
                    QgsProcessingParameterVectorLayer, 
                    QgsProcessingParameterMapLayer, 
                    QgsProcessingParameterVectorDestination,
                    QgsProcessingParameterRasterLayer,
                    QgsProcessingException,
                    QgsProcessingUtils, 
                    QgsExpressionContextUtils,
                    QgsCoordinateReferenceSystem,
                    QgsProject, QgsProperty)
import processing


class Platformx (QgsProcessingAlgorithm):

    INPUT = 'INPUT'
    INPUT2 = 'INPUT2'
    INPUT3 = 'INPUT3'
    INPUT4 = 'INPUT4'
    OUTPUT = 'OUTPUT'

    def name(self):
        return 'platformx'

    def displayName(self):
        return 'Platform extended to road center line'

    def group(self):
        return 'IMP Tools'

    def groupId(self):
        return 'imp'

    def createInstance(self):
        return Platformx()
        
    def shortHelpString(self):
        return ('Create platform polygons extended to road center lines (platformx)  '
               ' and calculate platform elevation ' 
               ' based on a slightly lower value than the mean z value of the Digital elevation model cells'
               '\n'
               'The Plot line input map layer can be an AutoCAD DXF file.'
               '\n'
               'The meanz field in the output map layer is the mean z value of DEM cells covered by the polygon. ' 
               )


    def initAlgorithm(self, config=None):
    
        self.addParameter(QgsProcessingParameterVectorLayer(
            self.INPUT, 'INPUT: Road node', 
            defaultValue='Node',types=[QgsProcessing.TypeVectorPoint]) )
            
        self.addParameter(QgsProcessingParameterVectorLayer(
            self.INPUT2, 'INPUT2: Road segment', 
            defaultValue='Segment',types=[QgsProcessing.TypeVectorLine]) )
            
        self.addParameter(QgsProcessingParameterVectorLayer(
            self.INPUT3, 'INPUT3: Plot line', 
            defaultValue='Plot_line',types=[QgsProcessing.TypeVectorLine]) ) 
            
        self.addParameter(QgsProcessingParameterRasterLayer(
            self.INPUT4, 'INPUT4: Digital elevation model',
            defaultValue='DEM_SRTM') ) 
     
        self.addParameter(QgsProcessingParameterVectorDestination(
            self.OUTPUT, 'Platformx') )
        


    def processAlgorithm(self, parameters, context, feedback):
        
        # Project variables
        project = QgsProject.instance()
        scope = QgsExpressionContextUtils.projectScope(project)
        projfold = scope.variable('project_folder')
        try:
            projcrs = QgsCoordinateReferenceSystem( scope.variable('project_crs') )
        except:
            raise QgsProcessingException ('Project coordinate reference system not set')

            
        # Buffer and boundary nodes to connect to segment lines 
        layer = processing.run('native:buffer', 
                {'DISSOLVE': False,
                'DISTANCE': 6,
                'END_CAP_STYLE': 0,
                'INPUT': parameters[self.INPUT],
                'JOIN_STYLE': 0,
                'MITER_LIMIT': 2,
                'SEGMENTS': 5,
                'OUTPUT': 'TEMPORARY_OUTPUT' },
				context=context, feedback=feedback, is_child_algorithm=True
				) ['OUTPUT']

        # Boundary
        layer = processing.run('native:boundary', 
                {'INPUT': layer,
                'OUTPUT': 'TEMPORARY_OUTPUT' },
				context=context, feedback=feedback, is_child_algorithm=True
				) ['OUTPUT']

        # Merge vector layers
        layer = processing.run('native:mergevectorlayers', 
                {'CRS': projcrs,
                'LAYERS': [ layer, parameters[self.INPUT3], parameters[self.INPUT2] ],
                'OUTPUT': 'TEMPORARY_OUTPUT' },
				context=context, feedback=feedback, is_child_algorithm=True
				) ['OUTPUT']

        # Polygonize
        layer = processing.run('native:polygonize', 
                {'INPUT': layer,
                'KEEP_FIELDS': False,
                'OUTPUT': 'TEMPORARY_OUTPUT' },
				context=context, feedback=feedback, is_child_algorithm=True
				) ['OUTPUT']
               
        # Remove small areas with Extract by expression
        layer = processing.run('native:extractbyexpression', 
                {'EXPRESSION': '$area>200',
                'INPUT': layer,
                'OUTPUT': 'TEMPORARY_OUTPUT' },
				context=context, feedback=feedback, is_child_algorithm=True
				) ['OUTPUT']
 
        # Mean elevation with Zonal statistics
        processing.run('native:zonalstatistics', 
                {'INPUT_RASTER': parameters[self.INPUT4],
                'INPUT_VECTOR': layer,
                'COLUMN_PREFIX': '_',
                'RASTER_BAND': 1,
                'STATISTICS': [2] },
				context=context, feedback=feedback, is_child_algorithm=True
				) 
        
        # Refactor fields
        layer = processing.run('native:refactorfields', 
                {'FIELDS_MAPPING': [
                    {'expression': '$id','length': 0,'name': 'platid','precision': 0,'type': 2},
                    {'expression': 'round( (\"_mean\" * .996 ) ,1)','length': 0,'name': 'platz','precision': 0,'type': 6},
                    {'expression': 'round(\"_mean\",1)','length': 0,'name': 'meanz','precision': 0,'type': 6} ],
                'INPUT': layer,
                'OUTPUT': 'TEMPORARY_OUTPUT' },
				context=context, feedback=feedback, is_child_algorithm=True
				) ['OUTPUT']
        
        # Set Z value
        algout = self.parameterAsOutputLayer(parameters, self.OUTPUT, context)

        algoutlay = processing.run('native:setzvalue', 
                {'INPUT': layer,
                'Z_VALUE': QgsProperty.fromExpression('"platz"'),
                'OUTPUT': algout },
				context=context, feedback=feedback, is_child_algorithm=True
				) ['OUTPUT']    

        
        # necc to overcome bug in runAndLoadResults in QPy console
        context.addLayerToLoadOnCompletion(algoutlay,context.LayerDetails(
                name='Platformx',project=context.project() ))  

        layer = QgsProcessingUtils.mapLayerFromString(algoutlay, context)
        platqml = projfold + '\\qsettings\\Platform_rdm_z_downcen.qml'
        layer.loadNamedStyle(platqml)
        

        feedback.pushInfo( '\n\n ##################################\n')
        feedback.pushInfo( '\n\n{} PLATFORMX CREATED'.format(layer.featureCount() ) )
        feedback.pushInfo( '\n\nOshPlatformx.py v2.1\n'
                           '##################################\n\n')            
        
        return {self.OUTPUT: algoutlay}
        
        



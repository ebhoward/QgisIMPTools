
"""
***************************************************************************
    OshLanduse.py
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
        QgsProcessingParameterFeatureSink,
        QgsProcessingParameterVectorDestination,
        QgsProcessingUtils, 
        QgsFeatureSink,
        QgsFeature, QgsField, QgsFields, 
        QgsProject,
        QgsExpressionContextUtils,
        QgsCoordinateReferenceSystem
       )
from qgis import processing

class Landuse(QgsProcessingAlgorithm):
    INPUT = 'INPUT' 
    INPUT2 = 'INPUT2'
    INPUT3 = 'INPUT3' 
    INPUT4 = 'INPUT4'
    INPUT5 = 'INPUT5'
    OUTPUT = 'OUTPUT'
    
    def name(self):
        return 'landuse'
    def displayName(self):
        return 'Landuse'
    def createInstance(self):
        return Landuse()
        
    def group(self):
        return 'IMP Tools'

    def groupId(self):
        return 'imp'

    def shortHelpString(self):
        return ( 'Create landuse polygons '
                    '\n'
                    'Road polygons are automatically identified and  '
                    'a road landuse code is inserted into the field luc.'
                    '\n'
                    'The Plot line and Site boundary line input map layers can be AutoCAD DXF files. '
                    '\n'
                    'After running this algorithm, the user can edit and insert other landuse codes with QGIS tools.'
                    '\n'
                    'If the landuse polygons do not form correctly, '
                    'snap and trim the intersecting lines from the '
                    'Road casing, Plot line and Site boundary line map layers.'
                    )

                 
    def initAlgorithm(self, config=None):
        self.addParameter(QgsProcessingParameterMapLayer(
            self.INPUT, 'INPUT: Road casing', 
            types=[QgsProcessing.TypeVectorLine],defaultValue='Casing'))
        self.addParameter(QgsProcessingParameterMapLayer(
            self.INPUT2, 'INPUT2: Plot line',
            types=[QgsProcessing.TypeVectorLine],defaultValue='Plot_line'))
        self.addParameter(QgsProcessingParameterMapLayer(
            self.INPUT3, 'INPUT3: Site boundary line',
            types=[QgsProcessing.TypeVectorLine],defaultValue='Site_boundary'))    
        self.addParameter(QgsProcessingParameterMapLayer(
            self.INPUT4, 'INPUT4: Road node',
            types=[QgsProcessing.TypeVectorPoint],defaultValue='Node'))
        self.addParameter(QgsProcessingParameterMapLayer(
            self.INPUT5, 'INPUT5: Road segment',
            types=[QgsProcessing.TypeVectorLine],defaultValue='Segment')) 
            
        self.addParameter(QgsProcessingParameterFeatureSink(
            self.OUTPUT, 'Landuse' ) )
            
            
            
    def processAlgorithm(self, parameters, context, feedback):

        caslay = self.parameterAsVectorLayer(parameters,
            self.INPUT, context )
        plolinlay = self.parameterAsVectorLayer(parameters,
            self.INPUT2, context )  
        sitbdylay = self.parameterAsVectorLayer(parameters,
            self.INPUT3, context )             
        nodlay = self.parameterAsVectorLayer(parameters,
            self.INPUT4, context )  
        seglay = self.parameterAsVectorLayer(parameters,
            self.INPUT5, context )
            
        
        # Project variables
        project = QgsProject.instance()
        scope = QgsExpressionContextUtils.projectScope(project)
        crs = scope.variable('project_crs')
        try:
            projcrs = QgsCoordinateReferenceSystem( crs )
        except:
            raise QgsProcessingException ('Project coordinate reference system not set')


        # Merge plot and site boundary lines
        layer = processing.run('native:mergevectorlayers', 
                {'CRS': projcrs,
                'LAYERS': [ caslay, plolinlay, sitbdylay ],
                'OUTPUT': 'TEMPORARY_OUTPUT'    } ,                
                context=context, feedback=feedback, is_child_algorithm=True
                ) ['OUTPUT'] 
        
        # Polygonize
        layer = processing.run( "native:polygonize", 
                {'INPUT':layer,'KEEP_FIELDS':False,
                'OUTPUT':'TEMPORARY_OUTPUT'} ,
                context=context, feedback=feedback, is_child_algorithm=True
                ) ['OUTPUT']
        layer = processing.run('native:refactorfields', 
                {'FIELDS_MAPPING': [
                    {'expression': '$id','length': 0,'name': 'plotid','precision': 0,'type': 4},
                    {'expression': '', 'length': 0,'name': 'luc','precision': 0,'type': 10}  ],
                'INPUT': layer,
                'OUTPUT': 'TEMPORARY_OUTPUT'},
                context=context, feedback=feedback, is_child_algorithm=True)['OUTPUT']
        
        processing.run("native:createspatialindex",
                {'INPUT': layer },
                context=context, feedback=feedback, is_child_algorithm=True) 
        
        processing.run("native:selectbylocation", 
                {'INPUT':layer,'INTERSECT':seglay,
                'PREDICATE':[0],'METHOD':0},        
                context=context, feedback=feedback, is_child_algorithm=True) 
        
        lulay = QgsProcessingUtils.mapLayerFromString(layer, context)
        sf = lulay.selectedFeatures()
        lulay.startEditing()
        for f in sf:
            f['luc'] = 'rod'
            lulay.updateFeature(f)
        lulay.commitChanges()
        lulay.removeSelection()
              
        
        totarea = totrdarea = 0
        for f in lulay.getFeatures():
            totarea = totarea + f.geometry().area()
            luc = f['luc']
            if luc:
                if luc in ('rod'):
                    totrdarea = totrdarea + f.geometry().area()
        totarea = totarea/10000
        totarea = round (totarea,1)
        totrdarea = totrdarea/10000
        totrdarea = round (totrdarea,1)        
        
        
        (sink, self.dest_id) = self.parameterAsSink(
            parameters,
            self.OUTPUT,
            context,
            lulay.fields(),
            lulay.wkbType(),
            lulay.sourceCrs()
        )
        
        sink.addFeatures(lulay.getFeatures(),QgsFeatureSink.FastInsert)
        
        
        feedback.pushInfo( '\n\n ######################################\n')
        feedback.pushInfo( '\n\n {} LANDUSE POLYGONS CREATED '.format(lulay.featureCount() ) )
        feedback.pushInfo( 'TOTAL AREA: {} HECTARES'.format(totarea) )       
        feedback.pushInfo( 'TOTAL ROAD AREA: {} HECTARES OR {}%'.format(totrdarea, round((totrdarea/totarea*100),1) ) )        
        feedback.pushInfo( '\n\nOshLanduse.py v2.1\n'
                           '######################################\n\n')
         
        return {self.OUTPUT: self.dest_id }
        
        
            
    def postProcessAlgorithm(self, context, feedback):

        project = QgsProject.instance()
        scope = QgsExpressionContextUtils.projectScope(project)
        projfold = scope.variable('project_folder')
        qml = projfold + '\\qsettings\\Landuse.qml'
        layer2 = QgsProcessingUtils.mapLayerFromString(self.dest_id, context)
        layer2.loadNamedStyle(qml)

        return {self.OUTPUT: self.dest_id} 
        
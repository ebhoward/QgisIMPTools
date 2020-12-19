
"""
***************************************************************************
    OshDeadspot.py
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

from qgis.PyQt.QtCore import QCoreApplication
from qgis.core import (QgsProcessing,
		QgsProcessingAlgorithm,
		QgsProcessingMultiStepFeedback,
		QgsProcessingParameterMapLayer,
		QgsProcessingParameterBoolean,
		QgsProcessingParameterFeatureSink,
		QgsProcessingParameterVectorDestination,        QgsFeatureSink,
        QgsProject,QgsProcessingUtils,
        QgsExpressionContextUtils)
from qgis import processing


class Deadspot(QgsProcessingAlgorithm):
    INPUT = 'INPUT' 
    INPUT2 = 'INPUT2'

    OUTPUT = 'OUTPUT'

    def name(self):
        return 'deadspot'

    def displayName(self):
        return 'Drainage deadspot'

    def group(self):
        return 'IMP Tools'

    def groupId(self):
        return 'imp'

    def createInstance(self):
        return Deadspot()

    def shortHelpString(self):
        return ( 'Identify drainage deadspot at road node '
                 '\n'
                 'Connected road segments have other endpoints that are higher\n'
                 '\n\n'
                 'Road segment endpoints must have z values\n'
                 'If not, output will be incorrect'  )

                 
    def initAlgorithm(self, config=None):
        self.addParameter(QgsProcessingParameterMapLayer(
        self.INPUT, 'INPUT: Road node', defaultValue='Nodez', types=[QgsProcessing.TypeVectorPoint]))

        self.addParameter(QgsProcessingParameterMapLayer(
        self.INPUT2, 'INPUT2: Road segment', defaultValue='Segmentz', types=[QgsProcessing.TypeVectorLine]))
        
        self.addParameter(QgsProcessingParameterVectorDestination(
        self.OUTPUT, 'Deadspot', type=QgsProcessing.TypeVectorAnyGeometry))

    def processAlgorithm(self, parameters, context, feedback):
    
        source = self.parameterAsSource(
            parameters,
            self.INPUT,
            context
        )
        
        # (sink, self.dest_id) = self.parameterAsSink(
            # parameters,
            # self.OUTPUT,
            # context,
            # source.fields(),
            # source.wkbType(),
            # source.sourceCrs()
        # )
        
        

        # Join attributes by nearest
        alg_params = {
            'DISCARD_NONMATCHING': False,
            'FIELDS_TO_COPY': [''],
            'INPUT': parameters[self.INPUT2],
            'INPUT_2': parameters[self.INPUT],
            'MAX_DISTANCE': 100,
            'NEIGHBORS': 2,
            'PREFIX': '',
            'OUTPUT': 'TEMPORARY_OUTPUT'
        }
        layer = processing.run('native:joinbynearest', alg_params, 
            context=context, feedback=feedback, is_child_algorithm=True
            ) ['OUTPUT'] 

        layer = processing.run('native:refactorfields', 
            {'FIELDS_MAPPING': [
                {'expression': 'lid','length': 0,'name': 'lid','precision': 0,'type': 4},
                {'expression': 'id', 'length': 0,'name': 'id','precision': 0,'type': 4},  
                {'expression': '\"z\"','length': 0,'name': 'z','precision': 0,'type': 6},                
                {'expression': 'z(start_point($geometry))','length': 0,'name': 'sz','precision': 0,'type': 6},
                {'expression': 'z(start_point($geometry))', 'length': 0,'name': 'ez','precision': 0,'type': 6}                   
                ],
            'INPUT': layer,
            'OUTPUT': 'TEMPORARY_OUTPUT'},
            context=context, feedback=feedback, is_child_algorithm=True
            )['OUTPUT']


        # Execute SQL 1
        alg_params = {
            'INPUT_DATASOURCES': layer,
            'INPUT_GEOMETRY_CRS': None,
            'INPUT_GEOMETRY_FIELD': '',
            'INPUT_GEOMETRY_TYPE': 1,
            'INPUT_QUERY': 'select count(*) as c,min(sz) as msz,min(ez) as mez,z,id from input1 group by id having c>1',
            'INPUT_UID_FIELD': '',
            'OUTPUT': 'TEMPORARY_OUTPUT'
        }
        layer = processing.run('qgis:executesql', alg_params, 
            context=context, feedback=feedback, is_child_algorithm=True
            ) ['OUTPUT']

        # Execute SQL 2
        alg_params = {
            'INPUT_DATASOURCES': layer,
            'INPUT_GEOMETRY_CRS': None,
            'INPUT_GEOMETRY_FIELD': '',
            'INPUT_GEOMETRY_TYPE': 1,
            'INPUT_QUERY': 'select id,( z - ( min(msz,mez) ) ) as zd from input1 where zd < 3',
            'INPUT_UID_FIELD': '',
            'OUTPUT': 'TEMPORARY_OUTPUT'
        }
        layer = processing.run('qgis:executesql', alg_params, 
            context=context, feedback=feedback, is_child_algorithm=True
            ) ['OUTPUT']

        # Join back geometry
        alg_params = {
            'INPUT': parameters[self.INPUT],
            'INPUT_2': layer,
            'DISCARD_NONMATCHING': True,
            'FIELD': 'id',
            'FIELDS_TO_COPY': [''],
            'FIELD_2': 'id',
            'METHOD': 1,
            'PREFIX': '',
            'OUTPUT': 'TEMPORARY_OUTPUT'
        }
        layer = processing.run('native:joinattributestable', alg_params, 
            context=context, feedback=None, is_child_algorithm=True
            ) ['OUTPUT']
            
        algout = self.parameterAsOutputLayer(parameters, self.OUTPUT, context)
        
        algoutlay = processing.run("native:deleteduplicategeometries", 
            {'INPUT':layer,'OUTPUT':algout},
            context=context, feedback=None, is_child_algorithm=True
            ) ['OUTPUT']
        

                
        project = QgsProject.instance()
        scope = QgsExpressionContextUtils.projectScope(project)
        projfold = scope.variable('project_folder')
        qml = projfold + '\\qsettings\\Deadspot.qml'
        
        layer = QgsProcessingUtils.mapLayerFromString(algoutlay, context)
        layer.loadNamedStyle(qml)      

        feedback.pushInfo( '\n\n ##################################\n')
        feedback.pushInfo( '\n{} DEADSPOTS FOUND'.format(layer.featureCount() ) )
        feedback.pushInfo( '\nOshDeadspot.py v2.1\n'
                           '##################################\n\n')    
                           
        # necc to overcome bug in runAndLoadResults in QPy console
        context.addLayerToLoadOnCompletion(algoutlay,context.LayerDetails(
                name='Deadspot',project=context.project() )) 
                
        return {self.OUTPUT: algoutlay}
        
        
        

        

"""
***************************************************************************
    OshCutFillRaster.py
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

from qgis.core import (QgsProcessing, QgsProcessingContext,
        QgsProcessingException, QgsProcessingAlgorithm, 
        QgsProcessingParameterVectorLayer,
        QgsProcessingParameterNumber,
        QgsProcessingParameterFeatureSink,
        QgsProcessingParameterRasterLayer,
        QgsProcessingUtils, QgsFeatureSink,
        QgsProcessingParameterRasterDestination,
        QgsProcessingParameterVectorDestination,
        QgsProcessingParameterMapLayer,
        QgsProcessingParameterBoolean,
        QgsCoordinateReferenceSystem,
        QgsExpressionContextUtils,
        QgsFeature, QgsField, QgsFields, 
        QgsGeometry, QgsProperty,
        QgsProject, QgsVectorLayer )
        
from qgis import processing

class CutFillRaster(QgsProcessingAlgorithm):

    INPUT = 'INPUT'
    INPUT2 = 'INPUT2'
    INPUT3 = 'INPUT3'


    def createInstance(self):
        return CutFillRaster()

    def name(self):
        return 'cutfillraster'

    def displayName(self):
        return 'Calculate cut and fill'
        
    def group(self):
        return 'IMP Tools'

    def groupId(self):
        return 'imp'

    def shortHelpString(self):
        return ('Calculate platform cut and fill volumes with the raster method\n' 
                    ' Platforms in the optional adjusted platform input layer will override underlying platforms'
                    ' in the first input layer for calculating cut and fill volumes. \n'
                    ' The results are presented in the Log tab.')


    def initAlgorithm(self, config=None):

        self.addParameter(QgsProcessingParameterVectorLayer(
                self.INPUT,'INPUT: Platform',
                [QgsProcessing.TypeVectorPolygon],'Platformx' ) )

        self.addParameter(QgsProcessingParameterVectorLayer(
                self.INPUT2,'INPUT2: Adjusted platform',
                [QgsProcessing.TypeVectorPolygon], defaultValue=None, optional=True) )
               
        self.addParameter(QgsProcessingParameterRasterLayer(
                self.INPUT3, 'INPUT3: Digital Elevation Model', 'DEM_SRTM' ) )
 

                
    def processAlgorithm(self, parameters, context, feedback):
        
        
        project = QgsProject.instance()
        scope = QgsExpressionContextUtils.projectScope(project)
        projfold = scope.variable('project_folder')
        
        try:
            projcrs = QgsCoordinateReferenceSystem( scope.variable('project_crs') )
        except:
            raise QgsProcessingException ('Project coordinate reference system not set')

        platlay = self.parameterAsVectorLayer(parameters, self.INPUT, context)   
        if platlay is None:
            raise QgsProcessingException(self.invalidSourceError(parameters, self.INPUT))    
        
        platlay2 = self.parameterAsVectorLayer(parameters, self.INPUT2, context)

        
        dic={}
        if platlay2:
            for f in platlay2.getFeatures():
                platid = f['platid']
                platz = f['platz']
                dic[platid] = platz
        
            t = tuple ( dic.keys()  ) 

            if ( len(t) >1 ):
                lisexp = 'platid not in ' + str ( t ) 
            else:
                lisexp = 'platid != ' + str( t[0] )

            
            platlay.selectByExpression(lisexp)
            
            platlaysel = processing.run("native:saveselectedfeatures", 
                    {'INPUT': platlay, 
                    'OUTPUT': 'TEMPORARY_OUTPUT' }, 
                    context = context, feedback=feedback, is_child_algorithm=True)['OUTPUT']
            platlay.removeSelection()
            
            layer = processing.run('native:mergevectorlayers', 
                    {'LAYERS': [platlaysel, platlay2], 
                    'OUTPUT': 'TEMPORARY_OUTPUT'},
                    context=context, feedback=feedback, is_child_algorithm=True)['OUTPUT']

            layer = processing.run('qgis:deletecolumn', 
                    {'INPUT': layer, 
                    'COLUMN' : ['fid','layer','projfold'], 
                    'OUTPUT': 'TEMPORARY_OUTPUT'},
                    context=context, feedback=feedback, is_child_algorithm=True)['OUTPUT']
           
            context.addLayerToLoadOnCompletion(layer,context.LayerDetails(
                name='Platform_updated',project=context.project() )) 
               
            layer = QgsProcessingUtils.mapLayerFromString(layer, context) 

    
            r = QgsProject.instance().layerTreeRoot()
            layers = r.checkedLayers()
            for lay in layers:
                if lay in (platlay,platlay2):
                    r.findLayer(lay.id()).setItemVisibilityChecked(False)   
       
        else:

            layer = platlay

        demlay = self.parameterAsRasterLayer(parameters, self.INPUT3, context)
        demcrs = demlay.crs()
        if demcrs != projcrs: 
            demlay = processing.run("gdal:warpreproject", 
                 {'INPUT': demlay,
                 'SOURCE_CRS': demcrs,
                 'TARGET_CRS': projcrs,
                 'RESAMPLING':0,'NODATA':None,
                 'TARGET_RESOLUTION':None, 'OPTIONS':'','DATA_TYPE':0,
                 'TARGET_EXTENT':None,'TARGET_EXTENT_CRS':None,
                 'MULTITHREADING':False,'EXTRA':'',
                 'OUTPUT':'TEMPORARY_OUTPUT'}
            ) ['OUTPUT']      
            demlay = QgsProcessingUtils.mapLayerFromString(demlay, context)
        
        ok = demlay.extent().contains(layer.extent())
        if not ok:
            raise QgsProcessingException ('\nError: Platform layer extends beyond DEM layer! \n')
        
        demx = demlay.rasterUnitsPerPixelX()
        demy = demlay.rasterUnitsPerPixelY()
        
        # Rasterize platform
        alg_params = {
            'INPUT': layer,
            'EXTENT': demlay.extent(),
            'FIELD': 'platz',
            'HEIGHT': demx,
            'WIDTH': demy,
            'BURN': 0,
            
            'DATA_TYPE': 5,
            'EXTRA': '',
            'INIT': None,
            'INVERT': False,
            'NODATA': 0,
            'OPTIONS': '',
            'UNITS': 1,
            'OUTPUT': 'TEMPORARY_OUTPUT'
            }
        R1 = processing.run('gdal:rasterize', alg_params, context=context, feedback=feedback, is_child_algorithm=True) ['OUTPUT']
        
        # context.addLayerToLoadOnCompletion(R1,context.LayerDetails(
            # name='R1',project=context.project() )) 

        # Raster calculator
        alg_params = {
            'INPUT_A': R1,
            'INPUT_B': demlay,
            'FORMULA': 'A-B',
            
            'BAND_A': 1,
            'BAND_B': None,
            'BAND_C': None,
            'BAND_D': None,
            'BAND_E': None,
            'BAND_F': None,
            'EXTRA': '',

            'INPUT_C': None,
            'INPUT_D': None,
            'INPUT_E': None,
            'INPUT_F': None,
            'NO_DATA': 0,
            'OPTIONS': '',
            'RTYPE': 5,
            'OUTPUT': 'TEMPORARY_OUTPUT'
        }
        R2 = processing.run('gdal:rastercalculator', alg_params, context=context, feedback=feedback, is_child_algorithm=True)['OUTPUT']

        # Cut
        alg_params = {
            'BAND': 1,
            'INPUT': R2,
            'LEVEL': 0,
            'METHOD': 1
        }
        results = processing.run('native:rastersurfacevolume', alg_params, context=context, feedback=feedback, is_child_algorithm=True)

        totcut = - results['VOLUME']  # a negative number

        # Fill
        alg_params = {
            'BAND': 1,
            'INPUT': R2,
            'LEVEL': 0,
            'METHOD': 0
        }
        results = processing.run('native:rastersurfacevolume', alg_params, context=context, feedback=feedback, is_child_algorithm=True)

        totfill = results['VOLUME']
                
        totarea = sum( [ f.geometry().area() for f in platlay.getFeatures() ] )
        
        feedback.pushInfo( '\n\n####################################\n\n' )
        feedback.pushInfo( 'TOTAL CUT VOLUME: {:,.0f} CUBIC METERS'.format(totcut) )
        feedback.pushInfo( 'TOTAL FILL VOLUME: {:,.0f} CUBIC METERS'.format(totfill) )
        feedback.pushInfo( 'TOTAL CUT AND FILL VOLUME: {:,.0f} CUBIC METERS'.format( (totfill + totcut) ) )
        # feedback.pushInfo( 'TOTAL CUT OVER TOTAL FILL PERCENTAGE: {:.1f} %'.format( ( totcut/totfill*100 ) ) )
        feedback.pushInfo( 'TOTAL AREA: {:,.1f} HECTARES'.format(totarea/10000) )

        feedback.pushInfo( 'AVERAGE CUTFILL HEIGHT (CBM:SQM): {:.1f} METERS'.format( (totfill+totcut) / totarea ) )
        feedback.pushInfo( '\n\nOshCutFillRaster.py v2.1\n'
                           '####################################\n\n' )    
         
      
   
   
    
        platqml = projfold + '\\qsettings\\Platform_platz_meanz.qml'    

        processing.run('native:setlayerstyle', 
            {'INPUT': layer, 'STYLE': platqml },
            context=context, feedback=feedback, is_child_algorithm=True)

        
        return {'OUTPUT': None}

     

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
        QgsProcessingParameterBoolean,
        QgsProcessingParameterVectorLayer,
        QgsProcessingParameterFeatureSink,
        QgsProcessingParameterNumber,
        QgsProcessingParameterString,
        QgsProcessingParameterVectorDestination,
        QgsProcessingUtils, 
        QgsFeatureSink,
       )
from qgis import processing
from qgis.core import (
        QgsFeature,QgsField, QgsFields, 
        QgsGeometry, QgsGeometryUtils,
        QgsProject, QgsProperty, QgsVectorLayer, 
        QgsExpressionContextUtils
        )


class AdjustPlatformAccess(QgsProcessingAlgorithm):

    INPUT = 'INPUT' 
    INPUT2 = 'INPUT2'
    INPUT3 = 'INPUT3' 
    INPUT4 = 'INPUT4'
    RATIO = 'RATIO'
    GRAD = 'GRAD' 
    AUTONAME = 'AUTONAME'
    VISOFF = 'VISOFF'

    OUTPUT = 'OUTPUT'
    OUTPUT2 = 'OUTPUT2' 

    def tr(self, string):
        return QCoreApplication.translate('Processing', string)

    def createInstance(self):
        return AdjustPlatformAccess()

    def name(self):
        return 'adjustplatformaccess'

    def displayName(self):
        return self.tr('Adjust platform and create access points')

    def group(self):
        return 'IMP Tools'

    def groupId(self):
        return 'imp'

    def shortHelpString(self):
        return self.tr('Adjust platform elevation minimally to enable access from at least one surrounding road\n  The maximum elevation difference between the access point and the platform is based on the input values for the internal ramp.' )

    def initAlgorithm(self, config=None):

        self.addParameter(
            QgsProcessingParameterVectorLayer(self.INPUT,
                self.tr('INPUT: Platform to adjust'),
                [QgsProcessing.TypeVectorPolygon],'Inaccessible_25' ) )
        self.addParameter(
            QgsProcessingParameterVectorLayer(self.INPUT2,
                self.tr('INPUT2: Platformx'),
                [QgsProcessing.TypeVectorPolygon],'Platformx' ) )
        self.addParameter(
            QgsProcessingParameterVectorLayer(self.INPUT3,
                self.tr('INPUT3: Segmentz'),
                [QgsProcessing.TypeVectorLine],'Segment_25' ) )
        self.addParameter(
            QgsProcessingParameterVectorLayer(self.INPUT4,
                self.tr('INPUT4: Nodez'),
                [QgsProcessing.TypeVectorPoint],'Node_25' ) )
                
        self.addParameter(
            QgsProcessingParameterNumber(self.RATIO,
                ( 'Ratio of perimeter to access ramp length'  ), 
               defaultValue= 5 ) )
        self.addParameter(
            QgsProcessingParameterNumber(self.GRAD,
                ( 'Gradient of internal access ramp  1 in '  ), 
               defaultValue= 30 ) )  
               
        self.addParameter(
            QgsProcessingParameterBoolean(self.AUTONAME,
                'Output auto naming ',
                defaultValue=True))   
        self.addParameter(
            QgsProcessingParameterBoolean(self.VISOFF,
                'Turn off other layers ',
                defaultValue=True))  
                
        self.addParameter(
                # QgsProcessingParameterFeatureSink(self.OUTPUT, 
                QgsProcessingParameterVectorDestination(self.OUTPUT, 
                self.tr('Platform_adjusted') ) )

        self.addParameter(
            QgsProcessingParameterFeatureSink(self.OUTPUT2,
                self.tr('Access_adjusted') ) )

    def processAlgorithm(self, parameters, context, feedback):

        fracperi = self.parameterAsInt(parameters, self.RATIO, context)  
        inramgrad = self.parameterAsInt(parameters, self.GRAD, context)

        inxslay = self.parameterAsVectorLayer(parameters, self.INPUT, context)
        if inxslay is None:
            raise QgsProcessingException(self.invalidSourceError(parameters, self.INPUT))
        platlay = self.parameterAsVectorLayer(parameters, self.INPUT2, context)
        if platlay is None:
            raise QgsProcessingException(self.invalidSourceError(parameters, self.INPUT2))                
            
        seglay = self.parameterAsVectorLayer(parameters, self.INPUT3, context)
        if seglay is None:
            raise QgsProcessingException(self.invalidSourceError(parameters, self.INPUT3)) 
            
        nodlay = self.parameterAsVectorLayer(parameters, self.INPUT4, context)
        if nodlay is None:
            raise QgsProcessingException(self.invalidSourceError(parameters, self.INPUT4))

        autonaming = self.parameterAsBoolean( parameters,  self.AUTONAME, context )
        visibleoff = self.parameterAsBoolean( parameters,  self.VISOFF, context )   

        

        newfields = QgsFields()
        newfields.append ( QgsField("platid", QVariant.Int) )
        newfields.append ( QgsField("platz", QVariant.Double) )
        newfields.append ( QgsField("id", QVariant.Int) )
        newfields.append ( QgsField('accz', QVariant.Double) )
        newfields.append ( QgsField("lid", QVariant.Int) )
        newfields.append ( QgsField('wid', QVariant.Double) ) 
        
        (sink2, self.dest_id2) = self.parameterAsSink(
            parameters,
            self.OUTPUT2,
            context,
            newfields,
            1001,       # wkbType: Pointz
            inxslay.sourceCrs()
            )

        # visible off 
        if visibleoff:
            r = QgsProject.instance().layerTreeRoot()
            layers = r.checkedLayers()
            for lay in layers:
                if lay not in (nodlay,seglay,platlay):
                    r.findLayer(lay.id()).setItemVisibilityChecked(False)

        # Create plot boundary layer 
        layer = processing.run('native:boundary',
                {'INPUT': inxslay,
                'OUTPUT': 'TEMPORARY_OUTPUT' } ,     
                is_child_algorithm=True, context=context, feedback=feedback
                ) ['OUTPUT']   

        # Buffer plot boundary layer to make intersection workable
        bufferdist = 1
        layer = processing.run('native:buffer', 
                {'INPUT': layer,
                'DISTANCE': bufferdist,
                'OUTPUT': 'TEMPORARY_OUTPUT' } ,           
                context=context, feedback=feedback, is_child_algorithm=True
                )['OUTPUT'] 

        # Intersect with road center line segment
        layer = processing.run('native:intersection', 
                {'INPUT': seglay,
                'OVERLAY': layer,
                'OUTPUT': 'TEMPORARY_OUTPUT' },
                context=context, feedback=feedback, is_child_algorithm=True
                )['OUTPUT']

        # Multipart to singleparts
        layer = processing.run('native:multiparttosingleparts', 
                {'INPUT': layer,
                'OUTPUT': 'TEMPORARY_OUTPUT'},
                context=context, feedback=feedback, is_child_algorithm=True
                )['OUTPUT']
       

        # Line substring
        exp1 = str(2 * bufferdist)
        exp2 = '$length - ' + exp1
        layer = processing.run('native:linesubstring', 
                {'INPUT': layer,
                'START_DISTANCE': QgsProperty.fromExpression(exp1),
                'END_DISTANCE': QgsProperty.fromExpression(exp2),
                'OUTPUT': 'TEMPORARY_OUTPUT'},        
                context=context, feedback=feedback, is_child_algorithm=True
                ) ['OUTPUT']
                

        segonplat = QgsProcessingUtils.mapLayerFromString(layer, context)


        dic = {}

        for f in segonplat.getFeatures():  
            geom = f.geometry()
            lin = geom.constGet() 
            if  lin.length() < 1:
                continue
            try:
                sz = lin.zAt(0)
            except:
                raise QgsProcessingException('Error! No z value in segment vertex')
            ez = lin.zAt(-1)
            platz = f['platz']
            
            platid = f['platid']
            lid = f['lid']
                        

            if abs(platz-sz) < abs(platz-ez):   
                pos = 0             # adjust to the startpoint: elevation and access
                accz = round(sz,1)
                adj = abs(platz-sz)
            else:    
                pos = -1
                accz = round (ez,1)
                adj = abs(platz-ez)

            lis = dic.get(platid) 
            if lis:
                adj_in_dic = lis[0]
                if adj < adj_in_dic:
                    dic[platid] = [adj,accz,lid,pos,sz,ez]
            else:
                dic[platid] = [adj,accz,lid,pos,sz,ez]
            
        inxslay.selectAll()
        clonelay = processing.run("native:saveselectedfeatures", 
                {'INPUT':inxslay, 'OUTPUT':'TEMPORARY_OUTPUT'}
                )['OUTPUT']
        inxslay.removeSelection()

        dic2 = {}
        clonelay.startEditing()        
        for f in clonelay.getFeatures():
            try:
                peri = f.geometry().constGet().boundary().length()
            except:
                continue
            maxdif = peri / fracperi / inramgrad
            maxdif = round (maxdif,1)
            
            platid = f['platid']
            lis = dic[platid]
            accz = lis[1]
            pos = lis[3]
            if pos==0:     # access at start point of segonplat
                adjz = accz - maxdif
            else:
                adjz = accz + maxdif
            adjz = round(adjz,1)
            f['platz'] = adjz
            dic2[platid] = adjz
                        
            clonelay.updateFeature(f)
            
        clonelay.commitChanges()


        algout = self.parameterAsOutputLayer(parameters, self.OUTPUT, context)
        
        # Set Z value       
        self.algoutlay = processing.run('native:setzvalue', 
                {'INPUT':clonelay,
                'Z_VALUE': QgsProperty.fromExpression('"platz"'),
                'OUTPUT': algout},
                context=context, feedback=feedback, is_child_algorithm=True) ['OUTPUT']       

        i=0
        for f in segonplat.getFeatures():
            platid = f['platid']
            lid = f['lid']
            lis = dic [platid]
            
            if lis[2] == lid:                
                accz = lis[1] 
                pos = lis[3]
                sz = lis[4]
                ez = lis[5]
                
                geom = f.geometry()               
                leng=geom.constGet().length()
                if pos ==0:
                    dist= 0.1* leng
                    accz = 0.1 * ez + 0.9 * sz
                else:
                    leng=geom.constGet().length()
                    dist = 0.9 * leng
                    accz = 0.1 * sz + 0.9 * ez
                
                accz = round(accz,1)
                pgeom = geom.interpolate(dist)    
                
                nf = QgsFeature()
                nf.setAttributes( [ platid, dic2[platid], i, accz, lid, f['wid'] ] )
                i+=1               
                nf.setGeometry(pgeom) 
                sink2.addFeature(nf, QgsFeatureSink.FastInsert)            

        num = str(inxslay.featureCount())
        feedback.pushInfo( '\n####################################\n' )
        feedback.pushInfo( '\nTOTAL ' + num + ' PLATFORMS ADJUSTED' )  
        feedback.pushInfo( '\n AND ' + num + ' ACCESS POINTS CREATED' ) 
        feedback.pushInfo( '\n\nOshAdjustPlatformAccess.py v2.1\n'
                           '####################################\n\n' )

        if autonaming: 
        
            num = seglay.name().split('_')[-1]
            if num.isnumeric():
                platname = 'Platform_' + str(num)
                accname = 'Access+_' + str(num)
            else:
                platname = 'Platform_adjusted'
                accname = 'Access_adjusted'                 
            
            context.addLayerToLoadOnCompletion(self.algoutlay,context.LayerDetails(
                name=platname,project=context.project() )) 
            
            context.addLayerToLoadOnCompletion(self.dest_id2,context.LayerDetails(
                name=accname,project=context.project() ))



        return {self.OUTPUT: self.algoutlay, self.OUTPUT2: self.dest_id2}


        

    def postProcessAlgorithm(self, context, feedback):
    
        project = QgsProject.instance()
        scope = QgsExpressionContextUtils.projectScope(project)
        projfold = scope.variable('project_folder')

        pointqml = projfold + '\\qsettings\\Platform_access.qml'
        platqml = projfold + '\\qsettings\\Platform_z_adjusted_upcen.qml'

        
        layer2 = QgsProcessingUtils.mapLayerFromString(self.algoutlay, context)
        layer2.loadNamedStyle(platqml)    
        
        layer3 = QgsProcessingUtils.mapLayerFromString(self.dest_id2, context)
        layer3.loadNamedStyle(pointqml)  



                 


        return {self.OUTPUT: self.algoutlay, self.OUTPUT2: self.dest_id2}
     
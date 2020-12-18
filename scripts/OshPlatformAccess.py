from qgis.PyQt.QtCore import QCoreApplication, QVariant
from qgis.core import (QgsProcessing, 
        QgsProcessingAlgorithm, 
        QgsProcessingContext,
        QgsProcessingException, 
        QgsProcessingParameterBoolean,
        QgsProcessingParameterVectorLayer,
        QgsProcessingParameterFeatureSink,
        QgsProcessingParameterNumber,
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

class PlatformAccess(QgsProcessingAlgorithm):

    INPUT = 'INPUT' 
    INPUT2 = 'INPUT2'
    INPUT3 = 'INPUT3' 

    RATIO = 'RATIO'
    GRAD = 'GRAD' 
    VISOFF = 'VISOFF'

    OUTPUT = 'OUTPUT'
    
    
    def tr(self, string):
        return QCoreApplication.translate('Processing', string)

    def createInstance(self):
        return PlatformAccess()

    def name(self):
        return 'platformaccess'

    def displayName(self):
        return self.tr('Platform access point')

    def group(self):
        return 'Quantum IPMP Tools'

    def groupId(self):
        return 'ipmp'

    def shortHelpString(self):
        return ( 'Create platform access points'
                    '\n'
                    'The access point elevation is firstly based on the platform elevation. '
                    '\n'
                    'If the platform elevation is higher or lower than the access road segment, the algorithm creates an access point at the elevation where the platform can be accessed via an internal ramp with gradient and length calculated based on the input values.'
                    '\n'
                    'If the elevation differences are too large, an Inaccessible map layer is created showing platforms that cannot be accessed from adjoining roads.'
                    )

    def initAlgorithm(self, config=None):

        self.addParameter(
            QgsProcessingParameterVectorLayer(self.INPUT,
                self.tr('INPUT: Platformx'),
                [QgsProcessing.TypeVectorPolygon],'Platformx' ) )
        self.addParameter(
            QgsProcessingParameterVectorLayer(self.INPUT2,
                self.tr('INPUT2: Segmentz'),
                [QgsProcessing.TypeVectorLine],'Segment_25' ) )
        self.addParameter(
            QgsProcessingParameterVectorLayer(self.INPUT3,
                self.tr('INPUT3: Nodez'),
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
            QgsProcessingParameterBoolean(self.VISOFF,
                'Turn off other layers ',
                defaultValue=True))  

        self.addParameter(
            QgsProcessingParameterFeatureSink(self.OUTPUT,
                self.tr('Access'),
                QgsProcessing.TypeVectorAnyGeometry ) )
                
         

                
    def processAlgorithm(self, parameters, context, feedback):
                 
        fracperi = self.parameterAsInt(parameters, self.RATIO, context)  
        inramgrad = self.parameterAsInt(parameters, self.GRAD, context)  
        
 
        nodelay = self.parameterAsVectorLayer(parameters, self.INPUT3, context)
        if nodelay is None:
            raise QgsProcessingException(self.invalidSourceError(parameters, self.INPUT3))
            
        seglay = self.parameterAsVectorLayer(parameters, self.INPUT2, context)
        if seglay is None:
            raise QgsProcessingException(self.invalidSourceError(parameters, self.INPUT2))

        platlay = self.parameterAsVectorLayer(parameters, self.INPUT, context)
        if platlay is None:
            raise QgsProcessingException(self.invalidSourceError(parameters, self.INPUT))
            
 
        # autonaming = self.parameterAsBoolean( parameters,  self.AUTONAME, context )
        autonaming = True

        visibleoff = self.parameterAsBoolean( parameters,  self.VISOFF, context )     


        
        newfields = QgsFields()
        newfields.append ( QgsField("platid", QVariant.Int) )
        newfields.append ( QgsField("platz", QVariant.Double) )
        newfields.append ( QgsField("id", QVariant.Int) )
        newfields.append ( QgsField('accz', QVariant.Double) )
        newfields.append ( QgsField("lid", QVariant.Int) )
        newfields.append ( QgsField('wid', QVariant.Double) )    

        (sink, self.dest_id) = self.parameterAsSink(
            parameters,
            self.OUTPUT,
            context,
            newfields,
            1001,       # wkbType: Pointz
            platlay.sourceCrs()
            )   
            
    
 
        # Create polygon boundary
        layer = processing.run('native:boundary',
                {'INPUT': platlay,
                'OUTPUT': 'TEMPORARY_OUTPUT' } ,     
                is_child_algorithm=True, context=context, feedback=feedback
                ) ['OUTPUT']        

        # Insert perimeter field
        layer = processing.run('native:fieldcalculator',
                {'INPUT': layer,
                'FIELD_LENGTH': 0,
                'FIELD_NAME': 'peri',
                'FIELD_PRECISION': 0,
                'FIELD_TYPE': 1,
                'FORMULA': '$length',
                'OUTPUT': 'TEMPORARY_OUTPUT' },
                context=context, feedback=feedback, is_child_algorithm=True
                )  ['OUTPUT'] 

        # Buffer boundary layer to make intersection workable
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
       
       
        segonplat= QgsProcessingUtils.mapLayerFromString(layer, context)        
      
        platlist=[]
        k=0
        
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
            accz = platz
            peri = f['peri']
            maxdif = peri / fracperi / inramgrad
            maxdif = round (maxdif,1)

            if sz - maxdif < accz <= sz:
                accz = sz + 0.1 * (ez-sz)
                
            if ez + maxdif > accz >= ez:
                accz = ez  - 0.1 * (ez-sz)
           
            if sz <= accz <= ez:                
                leng = lin.length()
                if sz!=ez:
                    dist = leng * (accz - sz) / (ez - sz)
                else:
                    dist = leng/2
                pgeom = geom.interpolate(dist)
                
                id = k
                platid = f['platid']
                lid = f['lid']
                wid = f['wid']
                
                nf = QgsFeature()
                accz = round(accz,1)
                nf.setAttributes( [ platid, platz, id, accz, lid, wid ] )
                nf.setGeometry(pgeom)       
                sink.addFeature(nf,QgsFeatureSink.FastInsert)               
                
                platlist.append(f['platid'])
                k+=1

  
    
        lis = list( dict.fromkeys(platlist) )
        m = len(lis) 
        
        lisexp = 'platid not in ' + str (tuple (lis) ) 


        # re-style input layers     
        project = QgsProject.instance()
        scope = QgsExpressionContextUtils.projectScope(project)
        path = scope.variable('project_folder')

        nodeqml = path + '\\qsettings\\Node_z.qml'
        segqml = path + '\\qsettings\\Segment_simple.qml'

        
        nodelay.loadNamedStyle(nodeqml)
        seglay.loadNamedStyle(segqml)
        

        # rename
        num = seglay.name().split('_')[-1]
        if num.isnumeric():
            accname = 'Access_' + str(num)
        else:
            accname = 'Access_' + str(num)           
        
        context.addLayerToLoadOnCompletion(self.dest_id,context.LayerDetails(
            name=accname,project=context.project() )) 
            
 
        platlay.selectByExpression(lisexp)
        sf = platlay.selectedFeatures()
        lensf = len(sf)        
        if lensf>0:
            inxslay = processing.run("native:saveselectedfeatures", 
                    { 'INPUT': platlay, 'OUTPUT': 'TEMPORARY_OUTPUT' },
                    context=context, feedback=feedback, is_child_algorithm=True
                    )  ['OUTPUT']
                    
            num = seglay.name().split('_')[-1]
            if num.isnumeric():
                inxsname = 'Inaccessible_' + str(num)
            else:
                inxsname = 'Inaccessible'               
                
            context.addLayerToLoadOnCompletion(inxslay,context.LayerDetails(
                name=inxsname,project=context.project() ))                    
                
            inxsqml = path + '\\qsettings\\Inaccessible.qml'                
            inxslay = QgsProcessingUtils.mapLayerFromString(inxslay, context)
            inxslay.loadNamedStyle(inxsqml)
            

                    
        # visible off other layers
        if visibleoff:
            r = QgsProject.instance().layerTreeRoot()
            layers = r.checkedLayers()
            for lay in layers:
                if lay not in (nodelay,seglay,platlay):
                    r.findLayer(lay.id()).setItemVisibilityChecked(False)
                    

            
        feedback.pushInfo( '\n##############################\n' )
        feedback.pushInfo( '\nTOTAL {} ACCESS POINTS'.format(k) )       
        feedback.pushInfo( '\nTOTAL ' + str(platlay.featureCount()) + ' PLATFORMS' )  
        feedback.pushInfo( str(m) + ' ACCESSIBLE' ) 
        feedback.pushInfo( '\n\nOshPlatformAccess.py v2.1\n'
                           '##############################\n\n' )

        return {self.OUTPUT: self.dest_id}
        
        
        
    def postProcessAlgorithm(self, context, feedback):
 
        project = QgsProject.instance()
        scope = QgsExpressionContextUtils.projectScope(project)
        path = scope.variable('project_folder')      
        accqml = path + '\\qsettings\\Platform_access.qml'
        
        layer = QgsProcessingUtils.mapLayerFromString(self.dest_id, context)
        layer.loadNamedStyle(accqml)


        return {self.OUTPUT: self.dest_id}               
            
        
        
            
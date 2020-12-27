from qgis.PyQt.QtCore import QCoreApplication, QVariant
from qgis.core import (QgsProcessing, 
        QgsProcessingAlgorithm, 
        QgsProcessingContext,
        QgsProcessingException, 
        QgsProcessingParameterBoolean,
        QgsProcessingParameterVectorLayer,
        QgsProcessingParameterNumber,
        QgsProcessingParameterFeatureSink,
        QgsProcessingParameterVectorDestination,
        QgsProcessingUtils, 
        QgsFeatureSink,
       )
from qgis import processing
from qgis.core import (
        QgsFeature,QgsField, QgsFields, 
        QgsGeometry, QgsGeometryUtils,
        QgsProject, QgsProperty, QgsVectorLayer, 
        QgsExpressionContextUtils,
        QgsSpatialIndex,QgsVertexId,
        QgsCategorizedSymbolRenderer,
        QgsLineSymbol, 
        QgsRendererCategory
        )

class AutoAdjustGradientPlatform(QgsProcessingAlgorithm):

    INPUT = 'INPUT'
    INPUT2 = 'INPUT2'
    INPUT3 = 'INPUT3'
    GRADLIM = 'GRADLIM'
    RATIO = 'RATIO'
    GRAD = 'GRAD'
    VISOFF = 'VISOFF'
    
    OUTPUT = 'OUTPUT'
    OUTPUT2 = 'OUTPUT2'
    OUTPUT3 = 'OUTPUT3'
    OUTPUT4 = 'OUTPUT4'

    def createInstance(self):
        return AutoAdjustGradientPlatform()

    def name(self):
        return 'autoadjustgradientplatform'

    def displayName(self):
        return 'Auto adjust road gradient and platform elevation'

    def group(self):
        return 'IMP Tools'

    def groupId(self):
        return 'imp'

    def shortHelpString(self):
        return 'Auto adjust road gradient to satisfy input gradient limit and auto adjust platform elevation to enable access'
        
        

    def initAlgorithm(self, config=None):

        self.addParameter(
            QgsProcessingParameterVectorLayer(self.INPUT,
                'INPUT: Segmentz',
                [QgsProcessing.TypeVectorLine],'Segmentz' ) )
        self.addParameter(
            QgsProcessingParameterVectorLayer(self.INPUT2,
                'INPUT2: Nodez',
                [QgsProcessing.TypeVectorPoint],'Nodez' ) )
        self.addParameter(
            QgsProcessingParameterVectorLayer(self.INPUT3,
                'INPUT3: Platformx',
                [QgsProcessing.TypeVectorPolygon],'Platformx' ) )                

        self.addParameter(
            QgsProcessingParameterNumber(self.GRADLIM,
                'Road segments not steeper than 1:' , defaultValue= 25) )
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
                'Node_adjusted',
                QgsProcessing.TypeVectorAnyGeometry ) )
                
        self.addParameter(
            QgsProcessingParameterFeatureSink(self.OUTPUT2,
                'Segment_adjusted',
                QgsProcessing.TypeVectorAnyGeometry ) )
                
        self.addParameter(
            QgsProcessingParameterVectorDestination(self.OUTPUT3,
                'Platform_adjusted',
                QgsProcessing.TypeVectorAnyGeometry ) )
                
        self.addParameter(
            QgsProcessingParameterFeatureSink(self.OUTPUT4,
                'Access',
                QgsProcessing.TypeVectorAnyGeometry ) ) 

                
                
    def processAlgorithm(self, parameters, context, feedback):

        # SETTINGS
        
        maxitera = 9    # maximum number of iterations (repeat for all segments)

        gradlim = self.parameterAsInt(parameters, self.GRADLIM, context) 
        fracperi = self.parameterAsInt(parameters, self.RATIO, context)  
        inramgrad = self.parameterAsInt(parameters, self.GRAD, context)              
            
        segmentlay = self.parameterAsVectorLayer(parameters, self.INPUT, context)
        if segmentlay is None:
            raise QgsProcessingException(self.invalidSourceError(parameters, self.RATIO))

        nodelay = self.parameterAsVectorLayer(parameters, self.INPUT2, context)
        if nodelay is None:
            raise QgsProcessingException(self.invalidSourceError(parameters, self.GRAD))
 
        platlay = self.parameterAsVectorLayer(parameters, self.INPUT3, context)
        if platlay is None:
            raise QgsProcessingException(self.invalidSourceError(parameters, self.INPUT))
        
        
        autonaming = True
        visibleoff = self.parameterAsBoolean( parameters,  self.VISOFF, context )
        
        # Node_adjusted output
        newfields = QgsFields()
        newfields.append(QgsField('id', QVariant.Int)) 
        newfields.append(QgsField('z', QVariant.Double))
        newfields.append(QgsField('oldz', QVariant.Double)) 
        newfields.append(QgsField('adj', QVariant.Double))
        (sink, self.dest_id) = self.parameterAsSink(
            parameters,
            self.OUTPUT,
            context,
            newfields,
            1001,  # PointZ wkbType
            nodelay.sourceCrs()
            )

        # Segment_adjusted output
        newfields = QgsFields()
        newfields.append(QgsField('lid', QVariant.Int)) 
        newfields.append(QgsField('wid', QVariant.Double)) 
        newfields.append(QgsField('grad', QVariant.Double)) 
        newfields.append(QgsField('styl', QVariant.Int)) 
        newfields.append(QgsField('oldgrad', QVariant.Double)) 
       
        (sink2, self.dest_id2) = self.parameterAsSink(
            parameters,
            self.OUTPUT2,
            context,
            newfields,
            1002,  # LineStringZ wkbType
            segmentlay.sourceCrs()
            )


        # Access point layer output
        newfields = QgsFields()
        newfields.append ( QgsField("platid", QVariant.Int) )
        newfields.append ( QgsField("platz", QVariant.Double) )
        newfields.append ( QgsField("id", QVariant.Int) )
        newfields.append ( QgsField('accz', QVariant.Double) )
        newfields.append ( QgsField("lid", QVariant.Int) )
        newfields.append ( QgsField('wid', QVariant.Double) )    
        (sink4, self.dest_id4) = self.parameterAsSink(
            parameters,
            self.OUTPUT4,
            context,
            newfields,
            nodelay.wkbType(),      
            nodelay.sourceCrs()
            )     

        
        # visible off layers
        if visibleoff:
            r = QgsProject.instance().layerTreeRoot()
            layers = r.checkedLayers()
            for lay in layers:
                r.findLayer(lay.id()).setItemVisibilityChecked(False)



        
        # PART 1: ADJUST GRADIENT
        
        
        # Store into memory        
        d_idz={}
        for f in nodelay.getFeatures():
            id=f.id()
            z=f['z']
            d_idz[id]=z  
        
        d_lidgrad={}
        d_lidleng={}
        lislidwkg=[]
        d_lidgradwkg={}
        d_lideid={}
        d_lidsid={}
        
        index = QgsSpatialIndex(nodelay.getFeatures())
        
        for f in segmentlay.getFeatures():
            lid=f['lid']
            grad=f['grad']
            if not grad: 
                grad=9999
            d_lidgrad[lid]=grad
            lislidwkg.append(lid)
            d_lidgradwkg[lid]=grad
            
            lin = f.geometry().constGet()            
            pgeom = QgsGeometry(lin[0])
            nearest = index.nearestNeighbor(pgeom, 1)
            sid = nearest[0]
            sz = d_idz[sid]            
            pgeom = QgsGeometry(lin[-1])
            nearest = index.nearestNeighbor(pgeom, 1)
            eid = nearest[0]
            ez = d_idz[eid]
            
            d_lidleng[lid]=f.geometry().constGet().length()
            d_lidsid[lid]=sid
            d_lideid[lid]=eid    
      
        
        # adjust next (steepest)            
        for itera in range(0,maxitera):
                         
            for lid in lislidwkg:
                lid = min(d_lidgradwkg, key=d_lidgradwkg.get)
                if d_lidgrad[lid] > gradlim:
                    break   
                d_lidgradwkg.pop(lid)
                leng = d_lidleng[lid]
                grad = d_lidgrad[lid]
                ej = round( -(leng/grad - leng/gradlim),1)

                eid = d_lideid[lid]
                ez = d_idz[eid]
                sid = d_lidsid[lid]
                sz = d_idz[sid]
                
                if ez<sz:   # skip adjusting ez down if ez<sz
                    break
                ezj = round((ez + ej),1)            

                newgrad = abs(leng/(ezj-sz))
                ng = round(newgrad,1)
                d_lidgrad[lid]=ng

                # update d_idz
                d_idz[eid]=ezj  
            
                # update grad of connected segments
                lidlisteid = [l for l,i in d_lideid.items() if i == eid]
                lidlistsid = [l for l,i in d_lidsid.items() if i == eid]
                lidlist = lidlisteid + lidlistsid
                lidlist = list(dict.fromkeys(lidlist))
                lidlist.remove(lid)
                # print('lid',lid,'eid',eid,'connected lid\n',lidlist)
                
                for lid in lidlist:
                    eid = d_lideid[lid]
                    sid = d_lidsid[lid]
                    ez = d_idz[eid]
                    sz = d_idz[sid]
                    leng = d_lidleng[lid]
                    oldgrad = d_lidgrad[lid]
                    if ez==sz:
                        newgrad=9999
                    else:
                        newgrad = abs(leng/(ez-sz))
                    d_lidgrad[lid] = round(newgrad,1)


                # refill dict for next iteration
                d_lidgradwkg = d_lidgrad.copy()


        
        for f in segmentlay.getFeatures():
            geom = f.geometry()
            lin = geom.constGet()
            
            lid = f['lid']
            wid = f['wid']
            leng = lin.length()
            
            eid = d_lideid[lid]
            ez = d_idz[eid]
            sid = d_lidsid[lid]
            sz = d_idz[sid]
       
            # reverse if ez<sz
            
            if ez<sz: 
                # workaround to overcome Qgis crashing
                geom=QgsGeometry(lin.reversed())
                lin = geom.constGet()
                temp = eid
                eid = sid
                sid = temp
                d_lideid[lid] = eid
                d_lidsid[lid] = sid
                
                temp = ez
                ez = sz
                sz = temp

            # insert z into vertices
           
            lin.addZValue(0)               
            lin.setZAt(0,sz)
            lin.setZAt(-1,ez)
            n = lin.numPoints()   
            if n > 2:
                for i in range(1,n-1):
                    v = QgsVertexId(0,0,i)
                    d = QgsGeometryUtils.distanceToVertex(lin,v)
                    z = d/leng * (ez-sz) + sz
                    lin.setZAt(i,z)           
                
            oldgrad = f['grad']            
            if not oldgrad:
                oldgrad = 9999
            grad = d_lidgrad[lid]
            if grad<(gradlim-0.5):
                styl = 1
            elif grad!=oldgrad:
                styl = 2
            else:
                styl = 0
            
            if grad>50:
                grad = round(grad,0)
            if oldgrad>50:
                oldgrad = round(oldgrad,0)
                
                
            # add features to sink2 (Segment_adjusted)
            g = QgsFeature()
            g.setGeometry(geom)
            g.setAttributes([lid,wid,grad,styl,oldgrad])
            sink2.addFeature(g, QgsFeatureSink.FastInsert)  


            
        numnode=0
        for f in nodelay.getFeatures():
            id = f.id()
            oldz = f['z']
            z = d_idz[id]
            adj = round( (oldz - z), 1 )
            if adj !=0:
                numnode += 1
            geom = f.geometry()
            p = geom.constGet()
            p.setZ(z)            
            
            # add features to sink (Node_adjusted)
            g = QgsFeature()
            g.setGeometry(geom)
            g.setAttributes([id,z,oldz,adj])
            sink.addFeature(g, QgsFeatureSink.FastInsert)
 



        #   PART 2: access points
        
        
        # Create polygon boundary
        layer = processing.run('native:boundary', {'INPUT': platlay, 'OUTPUT': 'memory:' },
                    is_child_algorithm=True, context=context, feedback=feedback
                    ) ['OUTPUT']

        # Insert perimeter field
        alg_params = {
            'FIELD_LENGTH': 0,
            'FIELD_NAME': 'peri',
            'FIELD_PRECISION': 0,
            'FIELD_TYPE': 1,
            'FORMULA': '$length',
            'INPUT': layer,
            'OUTPUT': 'TEMPORARY_OUTPUT'
        }
        layer = processing.run('native:fieldcalculator', alg_params,
                    context=context, feedback=feedback, is_child_algorithm=True
                    )  ['OUTPUT']
          
               
        # Buffer boundary layer to make intersection workable
        bufferdist = 1
        alg_params = {
                    'DISTANCE': bufferdist,
                    'INPUT': layer,
                    'OUTPUT': 'TEMPORARY_OUTPUT'
                    }
        layer = processing.run('native:buffer', alg_params,
                    context=context, feedback=feedback, is_child_algorithm=True
                    )['OUTPUT'] 

        # Intersect with road center line segment
        alg_params = {
                    'INPUT': self.dest_id2,
                    'OVERLAY': layer,
                    'OUTPUT': 'TEMPORARY_OUTPUT'
                }
        layer = processing.run('native:intersection', alg_params,
                    context=context, feedback=feedback, is_child_algorithm=True
                    )['OUTPUT']
                    
        # Multipart to singleparts
        alg_params = {
                    'INPUT': layer,
                    'OUTPUT': 'TEMPORARY_OUTPUT'
                }
        layer = processing.run('native:multiparttosingleparts', alg_params,
                    context=context, feedback=feedback, is_child_algorithm=True
                    )['OUTPUT']
        
        # Line substring
        exp1 = str(2 * bufferdist)
        exp2 = '$length - ' + exp1

        alg_params = {
            'INPUT': layer,
            'START_DISTANCE': QgsProperty.fromExpression(exp1),
            'END_DISTANCE': QgsProperty.fromExpression(exp2),
            'OUTPUT': 'TEMPORARY_OUTPUT'
        }
        layer = processing.run('native:linesubstring', alg_params,
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
            # print(f['lid'], f['platid'], lin.length() )
            sz = lin.zAt(0)
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
                            
            if sz < accz < ez:                
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
                
                platz = round(platz,1)
                accz = round(accz,1)
                
                nf = QgsFeature()
                nf.setAttributes( [ platid, platz, id, accz, lid, wid ] )
                nf.setGeometry(pgeom)       
                sink4.addFeature(nf,QgsFeatureSink.FastInsert)               
                
                platlist.append(f['platid'])
                k+=1 
        
        # list of unique platids with access
        platacclis = list( dict.fromkeys(platlist) )
        lisexp = 'platid not in ' + str (tuple (platacclis) ) 

        
        
        
        #   PART 3: ADJUST PLATFORM FOR ACCESS
        
        segonplat.selectByExpression(lisexp)
        sf = segonplat.selectedFeatures()
        if (len(sf)>0):
            
            dic = {}

            for f in sf:  
                geom = f.geometry()
                lin = geom.constGet() 
                if  lin.length() < 1:
                    continue
                sz = lin.zAt(0)
                ez = lin.zAt(-1)
                platz = f['platz']
                
                platid = f['platid']
                lid = f['lid']
                print (platid,dic)
                
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


        platlay.selectAll()
        clonelay = processing.run("native:saveselectedfeatures", 
            {'INPUT': platlay, 'OUTPUT': 'memory:'},
            context=context, feedback=feedback, is_child_algorithm=True
            )['OUTPUT']
        platlay.removeSelection()

        dic2 = {}
        clonelay = QgsProcessingUtils.mapLayerFromString(clonelay, context)
        clonelay.startEditing() 
        
        clonelay.selectByExpression(lisexp)
        sf = clonelay.selectedFeatures()
        numplat = len(sf)

        for f in sf:
            peri = f.geometry().constGet().boundary().length()
            maxdif = peri / fracperi / inramgrad
            maxdif = round (maxdif,1)        
                
            platid = f['platid']
            try:
                lis = dic[platid]
            except:
                feedback.reportError('\nWarning: Unable to adjust platform ' + str(platid) + '\n')
                continue
            accz = lis[1]
            pos = lis[3]
            if pos==0:     # access at start point of segonplat
                adjz = accz - maxdif
            else:
                adjz = accz + maxdif
            f['platz'] = round(adjz,1)
            dic2[platid] = adjz
            
            clonelay.updateFeature(f)
            
        clonelay.commitChanges()
        

                
        # Set Z value 
        algout = self.parameterAsOutputLayer(parameters, self.OUTPUT3, context)        
        alg_params = {
            'INPUT': clonelay,
            'Z_VALUE': QgsProperty.fromExpression('"platz"'),
            'OUTPUT': algout
        }
        self.algoutlay3 = processing.run('native:setzvalue', alg_params,
            context=context, feedback=feedback, is_child_algorithm=True) ['OUTPUT']   


        i=0
        segonplat.selectByExpression(lisexp)
        sf = segonplat.selectedFeatures()
        
        for f in sf:
            platid = f['platid']
            lid = f['lid']
            
            lis = dic [platid]

            if lis[2] == lid:                
                accz = lis[1]
                pos = lis[3]
                sz = lis[4]
                ez = lis[5]

                geom = f.geometry()
                if pos ==0:
                    dist= 0.1* leng
                    accz = 0.1 * ez + 0.9 * sz
                else:
                    leng=geom.constGet().length()
                    dist = 0.9 * leng
                    accz = 0.1 * sz + 0.9 * ez
                           
                accz = round(accz,1)
                pgeom = geom.interpolate(dist)    
                
                platz = dic2[platid]
                platz = round (platz,1)
                nf = QgsFeature()
                nf.setAttributes( [ platid, platz, i, accz, lid, f['wid'] ] )
                nf.setGeometry(pgeom) 
                i+=1
                sink4.addFeature(nf, QgsFeatureSink.FastInsert)

        
        
        feedback.pushInfo( '\n###################################\n\n' )
        feedback.pushInfo( str(numnode) + ' NODE ELEVATIONS ADJUSTED' )  
        feedback.pushInfo( str( k) + ' ACCESS POINTS CREATED' )
        feedback.pushInfo( str( numplat ) + ' PLATFORMS ADJUSTED' )
        feedback.pushInfo( 'ANOTHER ' + str( i) + ' ACCESS POINTS CREATED' )
        feedback.pushInfo( '\n\nOshAutoAdjust.py v2.1'
                           '\n###################################\n\n' )
        
       
        if autonaming: 
            nodename = 'Node_' + str(gradlim)
            segname = 'Segment_' + str(gradlim)
            platname = 'Platform_updated_' + str(gradlim)
            accname = 'Access_' + str(gradlim) 
 
            context.addLayerToLoadOnCompletion(self.algoutlay3,context.LayerDetails(
                name=platname,project=context.project() )) 
            context.addLayerToLoadOnCompletion(self.dest_id4,context.LayerDetails(
                name=accname,project=context.project() )) 
            context.addLayerToLoadOnCompletion(self.dest_id2,context.LayerDetails(
                name=segname,project=context.project() )) 
            context.addLayerToLoadOnCompletion(self.dest_id,context.LayerDetails(
                name=nodename,project=context.project() ))
                
                      
            
        return {self.OUTPUT: self.dest_id, self.OUTPUT2: self.dest_id2, self.OUTPUT3: self.algoutlay3, self.OUTPUT4: self.dest_id4 }



    def postProcessAlgorithm(self, context, feedback):
        
        project = QgsProject.instance()
        scope = QgsExpressionContextUtils.projectScope(project)
        projfold = scope.variable('project_folder')

        nodeqml = projfold + '\\qsettings\\Node_adjusted.qml'      
        segqml = projfold + '\\qsettings\\Segment_adjusted.qml'  
        platqml = projfold + '\\qsettings\\Platform_rdm_z_downcen.qml'          
        accqml = projfold + '\\qsettings\\Platform_access.qml' 
 

        layer = QgsProcessingUtils.mapLayerFromString(self.dest_id, context)
        layer.loadNamedStyle(nodeqml)    
        layer = QgsProcessingUtils.mapLayerFromString(self.dest_id2, context)
        layer.loadNamedStyle(segqml)
        layer = QgsProcessingUtils.mapLayerFromString(self.algoutlay3, context)
        layer.loadNamedStyle(platqml)           
        layer = QgsProcessingUtils.mapLayerFromString(self.dest_id4, context)
        layer.loadNamedStyle(accqml) 
        
        return {self.OUTPUT: self.dest_id, self.OUTPUT2: self.dest_id2, self.OUTPUT3: self.algoutlay3, self.OUTPUT4: self.dest_id4 }

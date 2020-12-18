"""
***************************************************************************
    OshAdjustGradient.py
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
        QgsProcessingException,
        QgsFeatureSink,
       )
from qgis import processing
from qgis.core import (
        QgsFeature,QgsField, QgsFields, 
        QgsGeometry, QgsGeometryUtils,
        QgsProject, QgsProperty, QgsVectorLayer, 
        QgsExpressionContextUtils,
        QgsLineSymbol, 
        QgsRendererCategory,
        QgsCategorizedSymbolRenderer,
        QgsSpatialIndex,
        QgsVertexId, 
        QgsGeometryUtils )
        

class AdjustGradient(QgsProcessingAlgorithm):

    INPUT = 'INPUT' 
    INPUT2 = 'INPUT2'
    GRADLIM = 'GRADLIM' 
    AUTONAME = 'AUTONAME'
    VISOFF = 'VISOFF'

    OUTPUT = 'OUTPUT'
    OUTPUT2 = 'OUTPUT2'    

    def createInstance(self):
        return AdjustGradient()

    def name(self):
        return 'adjustgradient'

    def displayName(self):
        return ('Adjust segment gradient')

    def group(self):
        return ('Quantum IPMP Tools')

    def groupId(self):
        return 'ipmp'

    def shortHelpString(self):
        return ('Adjust all road segment gradients and junction node elevations'
                    '\n'
                    'Adjust all road segment gradients to be not steeper than the input value.  '
                    'Z values of segment endpoints and intermediate vertices are adjusted in the output layer.  '
                    'Z values of nodes around adjusted segments are also adjusted in the output layer.  '
                    '\n'
                    'The input Segmentz map layer must have a grad field.'
                    '\n'                    
                    'The algorithm works by adjusting the steepest segment down to the input steepness value.  '
                    'Connected segments are then adjusted.  '
                    'Following that, the algorithm adjusts the next steepest unconnected segment.  '
                    '\n'
                    'If there are still steep segments after the algorithm have passed through all segments, the process is repeated.  '
                    'A maximum of three iterations has been coded in the algorithm.'
                    )

    def initAlgorithm(self, config=None):

        self.addParameter(QgsProcessingParameterVectorLayer(
                self.INPUT,'INPUT: Segment',
                [QgsProcessing.TypeVectorLine],'Segmentz' ) )

        self.addParameter(QgsProcessingParameterVectorLayer(
                self.INPUT2,'INPUT2: Node',
                [QgsProcessing.TypeVectorPoint],'Nodez' ) )
            
        self.addParameter(QgsProcessingParameterNumber(
                self.GRADLIM,'Not steeper than 1:' ,
                defaultValue= 25) )

        self.addParameter(QgsProcessingParameterBoolean(
                self.AUTONAME,'Output auto naming ',
                defaultValue=True))   
    
        self.addParameter(QgsProcessingParameterBoolean(
                self.VISOFF,'Turn off other layers ',
                defaultValue=True))  
            
        self.addParameter(QgsProcessingParameterFeatureSink(
                self.OUTPUT,'Node_adjusted',
                QgsProcessing.TypeVectorAnyGeometry ) )
            
        self.addParameter(QgsProcessingParameterFeatureSink(
                self.OUTPUT2,'Segment_adjusted',
                QgsProcessing.TypeVectorAnyGeometry ) )
                
              
                
    def processAlgorithm(self, parameters, context, feedback):

       
        
        maxitera = 3    # maximum number of iterations (repeat for all segments)
        
        
            
        seglay = self.parameterAsVectorLayer(parameters, self.INPUT, context)
        if seglay is None:
            raise QgsProcessingException(self.InvalidSourceError(parameters, self.INPUT))

        nodelay = self.parameterAsVectorLayer(parameters, self.INPUT2, context)
        if nodelay is None:
            raise QgsProcessingException(self.InvalidSourceError(parameters, self.INPUT2))

        self.gradlim = self.parameterAsInt(parameters, self.GRADLIM, context)  
        if self.gradlim is None:
            raise QgsProcessingException(self.InvalidSourceError(parameters, self.gradlim))

        autonaming = self.parameterAsBoolean( parameters,  self.AUTONAME, context )

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
            seglay.sourceCrs()
            )



        # visible off 
        if visibleoff:
            r = QgsProject.instance().layerTreeRoot()
            layers = r.checkedLayers()
            for lay in layers:
                r.findLayer(lay.id()).setItemVisibilityChecked(False)
              

            
        # Store into memory
        d_idz={}
        for f in nodelay.getFeatures():
            id=f.id()
            try:
                z=f['z']
            except:
                raise QgsProcessingException('Error! Field: z not found in input node layer')
            d_idz[id]=z  
        
        d_lidgrad={}
        d_lidleng={}
        lislidwkg=[]
        d_lidgradwkg={}
        d_lideid={}
        d_lidsid={}
        
        index = QgsSpatialIndex(nodelay.getFeatures())
        
        for f in seglay.getFeatures():
            lid=f['lid']
            try:
                grad=f['grad']
            except:
                raise QgsProcessingException('Error! Field: grad not found in input segment layer')
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
                if d_lidgrad[lid] > self.gradlim:
                    break   
                d_lidgradwkg.pop(lid)
                leng = d_lidleng[lid]
                grad = d_lidgrad[lid]
                ej = round( -(leng/grad - leng/self.gradlim),1)

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


        
        #       adjust
        
        for f in seglay.getFeatures():
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
            lin.dropZValue()
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

            seglay.changeGeometry(f.id(), geom)        
                
            oldgrad = f['grad']            
            if not oldgrad:
                oldgrad = 9999
            grad = d_lidgrad[lid]
            if grad<(self.gradlim-0.5):
                styl = 1
            elif grad!=oldgrad:
                styl = 2
            else:
                styl = 0
            
            if grad>50:
                grad = round(grad,0)
            if oldgrad>50:
                oldgrad = round(oldgrad,0)
                
            g = QgsFeature()
            g.setGeometry(geom)

            g.setAttributes([lid,wid, grad,styl,oldgrad])
            sink2.addFeature(g, QgsFeatureSink.FastInsert)  
            
        i=0
        feedback.pushInfo( '\n####################################\n' )
        for f in nodelay.getFeatures():
            id = f.id()
            oldz = f['z']
            z = d_idz[id]
            adj = round( (oldz - z), 1 )
            if adj !=0:
                feedback.pushInfo( 'Node {} elevation adjusted {} meters'.format(id,adj) ) 
                i+=1
            geom = f.geometry()
            p = geom.constGet()
            p.setZ(z)
            
            g = QgsFeature()
            g.setGeometry(geom)
            g.setAttributes([id,z,oldz,adj])
            sink.addFeature(g, QgsFeatureSink.FastInsert)
            
        feedback.pushInfo( '\nSEGMENTS AND ' + str(i) + ' NODES ADJUSTED' ) 
        
        feedback.pushInfo( '\n\nOshAdjustGradient.py v2.1\n' 
                           '####################################\n\n' )


        if autonaming: 
            nodename = 'Node_' + str(self.gradlim)
            segname = 'Segment_' + str(self.gradlim)
 
            context.addLayerToLoadOnCompletion(self.dest_id,context.LayerDetails(
                name=nodename,project=context.project() ))
            context.addLayerToLoadOnCompletion(self.dest_id2,context.LayerDetails(
                name=segname,project=context.project() )) 
                
        return {self.OUTPUT: self.dest_id, self.OUTPUT2: self.dest_id2}


    def postProcessAlgorithm(self, context, feedback):
    
        project = QgsProject.instance()
        scope = QgsExpressionContextUtils.projectScope(project)
        projfold = scope.variable('project_folder')
        nodeqml = projfold + '\\qsettings\\Node_adjusted.qml'
        segqml = projfold + '\\qsettings\\Segment_adjusted.qml' 
        
        layer2 = QgsProcessingUtils.mapLayerFromString(self.dest_id, context)
        layer2.loadNamedStyle(nodeqml)

        layer3 = QgsProcessingUtils.mapLayerFromString(self.dest_id2, context)
        layer3.loadNamedStyle(segqml) 
        
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

        layer3.setRenderer(catren)
        layer3.triggerRepaint()   

        return {self.OUTPUT: self.dest_id, self.OUTPUT2: self.dest_id2}
        
   
            
            
            
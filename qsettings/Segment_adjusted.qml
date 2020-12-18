<!DOCTYPE qgis PUBLIC 'http://mrcc.com/qgis.dtd' 'SYSTEM'>
<qgis simplifyAlgorithm="0" simplifyMaxScale="1" maxScale="0" labelsEnabled="1" styleCategories="AllStyleCategories" simplifyLocal="1" simplifyDrawingTol="1" readOnly="0" version="3.16.0-Hannover" minScale="100000000" hasScaleBasedVisibilityFlag="0" simplifyDrawingHints="1">
  <flags>
    <Identifiable>1</Identifiable>
    <Removable>1</Removable>
    <Searchable>1</Searchable>
  </flags>
  <temporal enabled="0" mode="0" startExpression="" durationField="" startField="" fixedDuration="0" endExpression="" durationUnit="min" accumulate="0" endField="">
    <fixedRange>
      <start></start>
      <end></end>
    </fixedRange>
  </temporal>
  <renderer-v2 symbollevels="0" enableorderby="0" type="categorizedSymbol" forceraster="0" attr="styl">
    <categories>
      <category render="true" value="1" symbol="0" label="grad&lt;24.5"/>
      <category render="true" value="2" symbol="1" label="grad changed"/>
      <category render="true" value="0" symbol="2" label=""/>
    </categories>
    <symbols>
      <symbol force_rhr="0" name="0" clip_to_extent="1" type="line" alpha="1">
        <layer enabled="1" locked="0" class="SimpleLine" pass="0">
          <prop k="align_dash_pattern" v="0"/>
          <prop k="capstyle" v="square"/>
          <prop k="customdash" v="5;2"/>
          <prop k="customdash_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="customdash_unit" v="MM"/>
          <prop k="dash_pattern_offset" v="0"/>
          <prop k="dash_pattern_offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="dash_pattern_offset_unit" v="MM"/>
          <prop k="draw_inside_polygon" v="0"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="line_color" v="255,192,203,255"/>
          <prop k="line_style" v="solid"/>
          <prop k="line_width" v="1"/>
          <prop k="line_width_unit" v="MM"/>
          <prop k="offset" v="0"/>
          <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_unit" v="MM"/>
          <prop k="ring_filter" v="0"/>
          <prop k="tweak_dash_pattern_on_corners" v="0"/>
          <prop k="use_custom_dash" v="0"/>
          <prop k="width_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <data_defined_properties>
            <Option type="Map">
              <Option name="name" value="" type="QString"/>
              <Option name="properties"/>
              <Option name="type" value="collection" type="QString"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
      <symbol force_rhr="0" name="1" clip_to_extent="1" type="line" alpha="1">
        <layer enabled="1" locked="0" class="SimpleLine" pass="0">
          <prop k="align_dash_pattern" v="0"/>
          <prop k="capstyle" v="square"/>
          <prop k="customdash" v="5;2"/>
          <prop k="customdash_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="customdash_unit" v="MM"/>
          <prop k="dash_pattern_offset" v="0"/>
          <prop k="dash_pattern_offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="dash_pattern_offset_unit" v="MM"/>
          <prop k="draw_inside_polygon" v="0"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="line_color" v="0,128,0,255"/>
          <prop k="line_style" v="solid"/>
          <prop k="line_width" v="0.8"/>
          <prop k="line_width_unit" v="MM"/>
          <prop k="offset" v="0"/>
          <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_unit" v="MM"/>
          <prop k="ring_filter" v="0"/>
          <prop k="tweak_dash_pattern_on_corners" v="0"/>
          <prop k="use_custom_dash" v="0"/>
          <prop k="width_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <data_defined_properties>
            <Option type="Map">
              <Option name="name" value="" type="QString"/>
              <Option name="properties"/>
              <Option name="type" value="collection" type="QString"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
      <symbol force_rhr="0" name="2" clip_to_extent="1" type="line" alpha="1">
        <layer enabled="1" locked="0" class="SimpleLine" pass="0">
          <prop k="align_dash_pattern" v="0"/>
          <prop k="capstyle" v="square"/>
          <prop k="customdash" v="5;2"/>
          <prop k="customdash_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="customdash_unit" v="MM"/>
          <prop k="dash_pattern_offset" v="0"/>
          <prop k="dash_pattern_offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="dash_pattern_offset_unit" v="MM"/>
          <prop k="draw_inside_polygon" v="0"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="line_color" v="0,0,255,255"/>
          <prop k="line_style" v="solid"/>
          <prop k="line_width" v="0.1"/>
          <prop k="line_width_unit" v="MM"/>
          <prop k="offset" v="0"/>
          <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_unit" v="MM"/>
          <prop k="ring_filter" v="0"/>
          <prop k="tweak_dash_pattern_on_corners" v="0"/>
          <prop k="use_custom_dash" v="0"/>
          <prop k="width_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <data_defined_properties>
            <Option type="Map">
              <Option name="name" value="" type="QString"/>
              <Option name="properties"/>
              <Option name="type" value="collection" type="QString"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
    </symbols>
    <rotation/>
    <sizescale/>
  </renderer-v2>
  <labeling type="rule-based">
    <rules key="{82714ebb-48d4-4da3-ab4a-fc6680036207}">
      <rule description="grad" filter="grad=oldgrad" key="{e4750319-e811-4473-9f72-d4651925a62e}">
        <settings calloutType="simple">
          <text-style fontWeight="50" fontSize="6" fontUnderline="0" textOpacity="0.5" textOrientation="horizontal" textColor="31,120,180,255" isExpression="0" fontItalic="0" namedStyle="Regular" fieldName="grad" fontSizeMapUnitScale="3x:0,0,0,0,0,0" fontWordSpacing="0" fontSizeUnit="Point" fontLetterSpacing="0" useSubstitutions="0" multilineHeight="1" fontFamily="MS Shell Dlg 2" fontKerning="1" blendMode="0" previewBkgrdColor="255,255,255,255" allowHtml="0" fontStrikeout="0" capitalization="0">
            <text-buffer bufferSizeMapUnitScale="3x:0,0,0,0,0,0" bufferDraw="0" bufferNoFill="1" bufferOpacity="1" bufferBlendMode="0" bufferColor="255,255,255,255" bufferJoinStyle="128" bufferSize="1" bufferSizeUnits="MM"/>
            <text-mask maskSizeUnits="MM" maskSizeMapUnitScale="3x:0,0,0,0,0,0" maskedSymbolLayers="" maskSize="1.5" maskOpacity="1" maskEnabled="0" maskJoinStyle="128" maskType="0"/>
            <background shapeDraw="0" shapeOffsetX="0" shapeType="0" shapeSizeX="0" shapeSizeMapUnitScale="3x:0,0,0,0,0,0" shapeBlendMode="0" shapeBorderWidthMapUnitScale="3x:0,0,0,0,0,0" shapeRotation="0" shapeRadiiUnit="MM" shapeBorderColor="128,128,128,255" shapeBorderWidth="0" shapeJoinStyle="64" shapeOffsetMapUnitScale="3x:0,0,0,0,0,0" shapeSVGFile="" shapeOffsetUnit="MM" shapeSizeUnit="MM" shapeRadiiMapUnitScale="3x:0,0,0,0,0,0" shapeFillColor="255,255,255,255" shapeBorderWidthUnit="MM" shapeRadiiX="0" shapeRotationType="0" shapeSizeY="0" shapeOffsetY="0" shapeRadiiY="0" shapeOpacity="1" shapeSizeType="0">
              <symbol force_rhr="0" name="markerSymbol" clip_to_extent="1" type="marker" alpha="1">
                <layer enabled="1" locked="0" class="SimpleMarker" pass="0">
                  <prop k="angle" v="0"/>
                  <prop k="color" v="255,158,23,255"/>
                  <prop k="horizontal_anchor_point" v="1"/>
                  <prop k="joinstyle" v="bevel"/>
                  <prop k="name" v="circle"/>
                  <prop k="offset" v="0,0"/>
                  <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
                  <prop k="offset_unit" v="MM"/>
                  <prop k="outline_color" v="35,35,35,255"/>
                  <prop k="outline_style" v="solid"/>
                  <prop k="outline_width" v="0"/>
                  <prop k="outline_width_map_unit_scale" v="3x:0,0,0,0,0,0"/>
                  <prop k="outline_width_unit" v="MM"/>
                  <prop k="scale_method" v="diameter"/>
                  <prop k="size" v="2"/>
                  <prop k="size_map_unit_scale" v="3x:0,0,0,0,0,0"/>
                  <prop k="size_unit" v="MM"/>
                  <prop k="vertical_anchor_point" v="1"/>
                  <data_defined_properties>
                    <Option type="Map">
                      <Option name="name" value="" type="QString"/>
                      <Option name="properties"/>
                      <Option name="type" value="collection" type="QString"/>
                    </Option>
                  </data_defined_properties>
                </layer>
              </symbol>
            </background>
            <shadow shadowOffsetGlobal="1" shadowColor="0,0,0,255" shadowDraw="0" shadowOffsetUnit="MM" shadowScale="100" shadowUnder="0" shadowBlendMode="6" shadowRadiusMapUnitScale="3x:0,0,0,0,0,0" shadowRadiusUnit="MM" shadowRadiusAlphaOnly="0" shadowOpacity="0.7" shadowOffsetAngle="135" shadowOffsetDist="1" shadowOffsetMapUnitScale="3x:0,0,0,0,0,0" shadowRadius="1.5"/>
            <dd_properties>
              <Option type="Map">
                <Option name="name" value="" type="QString"/>
                <Option name="properties"/>
                <Option name="type" value="collection" type="QString"/>
              </Option>
            </dd_properties>
            <substitutions/>
          </text-style>
          <text-format decimals="3" placeDirectionSymbol="0" autoWrapLength="0" multilineAlign="0" formatNumbers="0" plussign="0" rightDirectionSymbol=">" addDirectionSymbol="0" reverseDirectionSymbol="0" wrapChar="" leftDirectionSymbol="&lt;" useMaxLineLengthForAutoWrap="1"/>
          <placement overrunDistanceMapUnitScale="3x:0,0,0,0,0,0" predefinedPositionOrder="TR,TL,BR,BL,R,L,TSR,BSR" offsetUnits="MM" repeatDistanceMapUnitScale="3x:0,0,0,0,0,0" lineAnchorType="0" distMapUnitScale="3x:0,0,0,0,0,0" geometryGenerator="" placement="2" distUnits="MM" priority="5" dist="0" geometryGeneratorEnabled="0" xOffset="0" yOffset="0" centroidInside="0" polygonPlacementFlags="2" quadOffset="4" geometryGeneratorType="PointGeometry" layerType="LineGeometry" maxCurvedCharAngleIn="25" repeatDistance="0" overrunDistanceUnit="MM" fitInPolygonOnly="0" labelOffsetMapUnitScale="3x:0,0,0,0,0,0" rotationAngle="0" preserveRotation="1" lineAnchorPercent="0.5" overrunDistance="0" repeatDistanceUnits="MM" placementFlags="10" offsetType="0" centroidWhole="0" maxCurvedCharAngleOut="-25"/>
          <rendering maxNumLabels="2000" zIndex="0" fontMinPixelSize="3" labelPerPart="0" scaleVisibility="0" minFeatureSize="0" mergeLines="0" obstacle="1" drawLabels="1" limitNumLabels="0" obstacleFactor="1" scaleMax="0" upsidedownLabels="0" fontLimitPixelSize="0" scaleMin="0" fontMaxPixelSize="10000" displayAll="0" obstacleType="1"/>
          <dd_properties>
            <Option type="Map">
              <Option name="name" value="" type="QString"/>
              <Option name="properties"/>
              <Option name="type" value="collection" type="QString"/>
            </Option>
          </dd_properties>
          <callout type="simple">
            <Option type="Map">
              <Option name="anchorPoint" value="pole_of_inaccessibility" type="QString"/>
              <Option name="ddProperties" type="Map">
                <Option name="name" value="" type="QString"/>
                <Option name="properties"/>
                <Option name="type" value="collection" type="QString"/>
              </Option>
              <Option name="drawToAllParts" value="false" type="bool"/>
              <Option name="enabled" value="0" type="QString"/>
              <Option name="labelAnchorPoint" value="point_on_exterior" type="QString"/>
              <Option name="lineSymbol" value="&lt;symbol force_rhr=&quot;0&quot; name=&quot;symbol&quot; clip_to_extent=&quot;1&quot; type=&quot;line&quot; alpha=&quot;1&quot;>&lt;layer enabled=&quot;1&quot; locked=&quot;0&quot; class=&quot;SimpleLine&quot; pass=&quot;0&quot;>&lt;prop k=&quot;align_dash_pattern&quot; v=&quot;0&quot;/>&lt;prop k=&quot;capstyle&quot; v=&quot;square&quot;/>&lt;prop k=&quot;customdash&quot; v=&quot;5;2&quot;/>&lt;prop k=&quot;customdash_map_unit_scale&quot; v=&quot;3x:0,0,0,0,0,0&quot;/>&lt;prop k=&quot;customdash_unit&quot; v=&quot;MM&quot;/>&lt;prop k=&quot;dash_pattern_offset&quot; v=&quot;0&quot;/>&lt;prop k=&quot;dash_pattern_offset_map_unit_scale&quot; v=&quot;3x:0,0,0,0,0,0&quot;/>&lt;prop k=&quot;dash_pattern_offset_unit&quot; v=&quot;MM&quot;/>&lt;prop k=&quot;draw_inside_polygon&quot; v=&quot;0&quot;/>&lt;prop k=&quot;joinstyle&quot; v=&quot;bevel&quot;/>&lt;prop k=&quot;line_color&quot; v=&quot;60,60,60,255&quot;/>&lt;prop k=&quot;line_style&quot; v=&quot;solid&quot;/>&lt;prop k=&quot;line_width&quot; v=&quot;0.3&quot;/>&lt;prop k=&quot;line_width_unit&quot; v=&quot;MM&quot;/>&lt;prop k=&quot;offset&quot; v=&quot;0&quot;/>&lt;prop k=&quot;offset_map_unit_scale&quot; v=&quot;3x:0,0,0,0,0,0&quot;/>&lt;prop k=&quot;offset_unit&quot; v=&quot;MM&quot;/>&lt;prop k=&quot;ring_filter&quot; v=&quot;0&quot;/>&lt;prop k=&quot;tweak_dash_pattern_on_corners&quot; v=&quot;0&quot;/>&lt;prop k=&quot;use_custom_dash&quot; v=&quot;0&quot;/>&lt;prop k=&quot;width_map_unit_scale&quot; v=&quot;3x:0,0,0,0,0,0&quot;/>&lt;data_defined_properties>&lt;Option type=&quot;Map&quot;>&lt;Option name=&quot;name&quot; value=&quot;&quot; type=&quot;QString&quot;/>&lt;Option name=&quot;properties&quot;/>&lt;Option name=&quot;type&quot; value=&quot;collection&quot; type=&quot;QString&quot;/>&lt;/Option>&lt;/data_defined_properties>&lt;/layer>&lt;/symbol>" type="QString"/>
              <Option name="minLength" value="0" type="double"/>
              <Option name="minLengthMapUnitScale" value="3x:0,0,0,0,0,0" type="QString"/>
              <Option name="minLengthUnit" value="MM" type="QString"/>
              <Option name="offsetFromAnchor" value="0" type="double"/>
              <Option name="offsetFromAnchorMapUnitScale" value="3x:0,0,0,0,0,0" type="QString"/>
              <Option name="offsetFromAnchorUnit" value="MM" type="QString"/>
              <Option name="offsetFromLabel" value="0" type="double"/>
              <Option name="offsetFromLabelMapUnitScale" value="3x:0,0,0,0,0,0" type="QString"/>
              <Option name="offsetFromLabelUnit" value="MM" type="QString"/>
            </Option>
          </callout>
        </settings>
      </rule>
      <rule description="grad changed" filter="grad!=oldgrad" key="{9783884b-0375-4d3d-a80a-824070d8298c}">
        <settings calloutType="simple">
          <text-style fontWeight="50" fontSize="8" fontUnderline="0" textOpacity="1" textOrientation="horizontal" textColor="31,120,180,255" isExpression="0" fontItalic="0" namedStyle="Regular" fieldName="grad" fontSizeMapUnitScale="3x:0,0,0,0,0,0" fontWordSpacing="0" fontSizeUnit="Point" fontLetterSpacing="0" useSubstitutions="0" multilineHeight="1" fontFamily="Arial" fontKerning="1" blendMode="0" previewBkgrdColor="255,255,255,255" allowHtml="0" fontStrikeout="0" capitalization="0">
            <text-buffer bufferSizeMapUnitScale="3x:0,0,0,0,0,0" bufferDraw="0" bufferNoFill="1" bufferOpacity="1" bufferBlendMode="0" bufferColor="255,255,255,255" bufferJoinStyle="128" bufferSize="1" bufferSizeUnits="MM"/>
            <text-mask maskSizeUnits="MM" maskSizeMapUnitScale="3x:0,0,0,0,0,0" maskedSymbolLayers="" maskSize="1.5" maskOpacity="1" maskEnabled="0" maskJoinStyle="128" maskType="0"/>
            <background shapeDraw="0" shapeOffsetX="0" shapeType="0" shapeSizeX="0" shapeSizeMapUnitScale="3x:0,0,0,0,0,0" shapeBlendMode="0" shapeBorderWidthMapUnitScale="3x:0,0,0,0,0,0" shapeRotation="0" shapeRadiiUnit="MM" shapeBorderColor="128,128,128,255" shapeBorderWidth="0" shapeJoinStyle="64" shapeOffsetMapUnitScale="3x:0,0,0,0,0,0" shapeSVGFile="" shapeOffsetUnit="MM" shapeSizeUnit="MM" shapeRadiiMapUnitScale="3x:0,0,0,0,0,0" shapeFillColor="255,255,255,255" shapeBorderWidthUnit="MM" shapeRadiiX="0" shapeRotationType="0" shapeSizeY="0" shapeOffsetY="0" shapeRadiiY="0" shapeOpacity="1" shapeSizeType="0">
              <symbol force_rhr="0" name="markerSymbol" clip_to_extent="1" type="marker" alpha="1">
                <layer enabled="1" locked="0" class="SimpleMarker" pass="0">
                  <prop k="angle" v="0"/>
                  <prop k="color" v="243,166,178,255"/>
                  <prop k="horizontal_anchor_point" v="1"/>
                  <prop k="joinstyle" v="bevel"/>
                  <prop k="name" v="circle"/>
                  <prop k="offset" v="0,0"/>
                  <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
                  <prop k="offset_unit" v="MM"/>
                  <prop k="outline_color" v="35,35,35,255"/>
                  <prop k="outline_style" v="solid"/>
                  <prop k="outline_width" v="0"/>
                  <prop k="outline_width_map_unit_scale" v="3x:0,0,0,0,0,0"/>
                  <prop k="outline_width_unit" v="MM"/>
                  <prop k="scale_method" v="diameter"/>
                  <prop k="size" v="2"/>
                  <prop k="size_map_unit_scale" v="3x:0,0,0,0,0,0"/>
                  <prop k="size_unit" v="MM"/>
                  <prop k="vertical_anchor_point" v="1"/>
                  <data_defined_properties>
                    <Option type="Map">
                      <Option name="name" value="" type="QString"/>
                      <Option name="properties"/>
                      <Option name="type" value="collection" type="QString"/>
                    </Option>
                  </data_defined_properties>
                </layer>
              </symbol>
            </background>
            <shadow shadowOffsetGlobal="1" shadowColor="0,0,0,255" shadowDraw="0" shadowOffsetUnit="MM" shadowScale="100" shadowUnder="0" shadowBlendMode="6" shadowRadiusMapUnitScale="3x:0,0,0,0,0,0" shadowRadiusUnit="MM" shadowRadiusAlphaOnly="0" shadowOpacity="0.7" shadowOffsetAngle="135" shadowOffsetDist="1" shadowOffsetMapUnitScale="3x:0,0,0,0,0,0" shadowRadius="1.5"/>
            <dd_properties>
              <Option type="Map">
                <Option name="name" value="" type="QString"/>
                <Option name="properties"/>
                <Option name="type" value="collection" type="QString"/>
              </Option>
            </dd_properties>
            <substitutions/>
          </text-style>
          <text-format decimals="3" placeDirectionSymbol="0" autoWrapLength="0" multilineAlign="0" formatNumbers="0" plussign="0" rightDirectionSymbol=">" addDirectionSymbol="0" reverseDirectionSymbol="0" wrapChar="" leftDirectionSymbol="&lt;" useMaxLineLengthForAutoWrap="1"/>
          <placement overrunDistanceMapUnitScale="3x:0,0,0,0,0,0" predefinedPositionOrder="TR,TL,BR,BL,R,L,TSR,BSR" offsetUnits="MM" repeatDistanceMapUnitScale="3x:0,0,0,0,0,0" lineAnchorType="0" distMapUnitScale="3x:0,0,0,0,0,0" geometryGenerator="" placement="2" distUnits="MM" priority="5" dist="0" geometryGeneratorEnabled="0" xOffset="0" yOffset="0" centroidInside="0" polygonPlacementFlags="2" quadOffset="4" geometryGeneratorType="PointGeometry" layerType="LineGeometry" maxCurvedCharAngleIn="25" repeatDistance="0" overrunDistanceUnit="MM" fitInPolygonOnly="0" labelOffsetMapUnitScale="3x:0,0,0,0,0,0" rotationAngle="0" preserveRotation="1" lineAnchorPercent="0.5" overrunDistance="0" repeatDistanceUnits="MM" placementFlags="10" offsetType="0" centroidWhole="0" maxCurvedCharAngleOut="-25"/>
          <rendering maxNumLabels="2000" zIndex="0" fontMinPixelSize="3" labelPerPart="0" scaleVisibility="0" minFeatureSize="0" mergeLines="0" obstacle="1" drawLabels="1" limitNumLabels="0" obstacleFactor="1" scaleMax="0" upsidedownLabels="0" fontLimitPixelSize="0" scaleMin="0" fontMaxPixelSize="10000" displayAll="0" obstacleType="1"/>
          <dd_properties>
            <Option type="Map">
              <Option name="name" value="" type="QString"/>
              <Option name="properties" type="Map">
                <Option name="Size" type="Map">
                  <Option name="active" value="true" type="bool"/>
                  <Option name="expression" value="@project_font_size" type="QString"/>
                  <Option name="type" value="3" type="int"/>
                </Option>
              </Option>
              <Option name="type" value="collection" type="QString"/>
            </Option>
          </dd_properties>
          <callout type="simple">
            <Option type="Map">
              <Option name="anchorPoint" value="pole_of_inaccessibility" type="QString"/>
              <Option name="ddProperties" type="Map">
                <Option name="name" value="" type="QString"/>
                <Option name="properties"/>
                <Option name="type" value="collection" type="QString"/>
              </Option>
              <Option name="drawToAllParts" value="false" type="bool"/>
              <Option name="enabled" value="0" type="QString"/>
              <Option name="labelAnchorPoint" value="point_on_exterior" type="QString"/>
              <Option name="lineSymbol" value="&lt;symbol force_rhr=&quot;0&quot; name=&quot;symbol&quot; clip_to_extent=&quot;1&quot; type=&quot;line&quot; alpha=&quot;1&quot;>&lt;layer enabled=&quot;1&quot; locked=&quot;0&quot; class=&quot;SimpleLine&quot; pass=&quot;0&quot;>&lt;prop k=&quot;align_dash_pattern&quot; v=&quot;0&quot;/>&lt;prop k=&quot;capstyle&quot; v=&quot;square&quot;/>&lt;prop k=&quot;customdash&quot; v=&quot;5;2&quot;/>&lt;prop k=&quot;customdash_map_unit_scale&quot; v=&quot;3x:0,0,0,0,0,0&quot;/>&lt;prop k=&quot;customdash_unit&quot; v=&quot;MM&quot;/>&lt;prop k=&quot;dash_pattern_offset&quot; v=&quot;0&quot;/>&lt;prop k=&quot;dash_pattern_offset_map_unit_scale&quot; v=&quot;3x:0,0,0,0,0,0&quot;/>&lt;prop k=&quot;dash_pattern_offset_unit&quot; v=&quot;MM&quot;/>&lt;prop k=&quot;draw_inside_polygon&quot; v=&quot;0&quot;/>&lt;prop k=&quot;joinstyle&quot; v=&quot;bevel&quot;/>&lt;prop k=&quot;line_color&quot; v=&quot;60,60,60,255&quot;/>&lt;prop k=&quot;line_style&quot; v=&quot;solid&quot;/>&lt;prop k=&quot;line_width&quot; v=&quot;0.3&quot;/>&lt;prop k=&quot;line_width_unit&quot; v=&quot;MM&quot;/>&lt;prop k=&quot;offset&quot; v=&quot;0&quot;/>&lt;prop k=&quot;offset_map_unit_scale&quot; v=&quot;3x:0,0,0,0,0,0&quot;/>&lt;prop k=&quot;offset_unit&quot; v=&quot;MM&quot;/>&lt;prop k=&quot;ring_filter&quot; v=&quot;0&quot;/>&lt;prop k=&quot;tweak_dash_pattern_on_corners&quot; v=&quot;0&quot;/>&lt;prop k=&quot;use_custom_dash&quot; v=&quot;0&quot;/>&lt;prop k=&quot;width_map_unit_scale&quot; v=&quot;3x:0,0,0,0,0,0&quot;/>&lt;data_defined_properties>&lt;Option type=&quot;Map&quot;>&lt;Option name=&quot;name&quot; value=&quot;&quot; type=&quot;QString&quot;/>&lt;Option name=&quot;properties&quot;/>&lt;Option name=&quot;type&quot; value=&quot;collection&quot; type=&quot;QString&quot;/>&lt;/Option>&lt;/data_defined_properties>&lt;/layer>&lt;/symbol>" type="QString"/>
              <Option name="minLength" value="0" type="double"/>
              <Option name="minLengthMapUnitScale" value="3x:0,0,0,0,0,0" type="QString"/>
              <Option name="minLengthUnit" value="MM" type="QString"/>
              <Option name="offsetFromAnchor" value="0" type="double"/>
              <Option name="offsetFromAnchorMapUnitScale" value="3x:0,0,0,0,0,0" type="QString"/>
              <Option name="offsetFromAnchorUnit" value="MM" type="QString"/>
              <Option name="offsetFromLabel" value="0" type="double"/>
              <Option name="offsetFromLabelMapUnitScale" value="3x:0,0,0,0,0,0" type="QString"/>
              <Option name="offsetFromLabelUnit" value="MM" type="QString"/>
            </Option>
          </callout>
        </settings>
      </rule>
      <rule description="oldgrad" filter="grad!=oldgrad" key="{c5b580e8-ba06-4ef3-99e2-3f40584c2238}">
        <settings calloutType="simple">
          <text-style fontWeight="50" fontSize="7" fontUnderline="0" textOpacity="1" textOrientation="horizontal" textColor="31,120,180,255" isExpression="1" fontItalic="0" namedStyle="Regular" fieldName="'('||oldgrad||')'" fontSizeMapUnitScale="3x:0,0,0,0,0,0" fontWordSpacing="0" fontSizeUnit="Point" fontLetterSpacing="0" useSubstitutions="0" multilineHeight="1" fontFamily="Arial" fontKerning="1" blendMode="0" previewBkgrdColor="255,255,255,255" allowHtml="0" fontStrikeout="0" capitalization="0">
            <text-buffer bufferSizeMapUnitScale="3x:0,0,0,0,0,0" bufferDraw="0" bufferNoFill="1" bufferOpacity="1" bufferBlendMode="0" bufferColor="255,255,255,255" bufferJoinStyle="128" bufferSize="1" bufferSizeUnits="MM"/>
            <text-mask maskSizeUnits="MM" maskSizeMapUnitScale="3x:0,0,0,0,0,0" maskedSymbolLayers="" maskSize="1.5" maskOpacity="1" maskEnabled="0" maskJoinStyle="128" maskType="0"/>
            <background shapeDraw="0" shapeOffsetX="0" shapeType="0" shapeSizeX="0" shapeSizeMapUnitScale="3x:0,0,0,0,0,0" shapeBlendMode="0" shapeBorderWidthMapUnitScale="3x:0,0,0,0,0,0" shapeRotation="0" shapeRadiiUnit="MM" shapeBorderColor="128,128,128,255" shapeBorderWidth="0" shapeJoinStyle="64" shapeOffsetMapUnitScale="3x:0,0,0,0,0,0" shapeSVGFile="" shapeOffsetUnit="MM" shapeSizeUnit="MM" shapeRadiiMapUnitScale="3x:0,0,0,0,0,0" shapeFillColor="255,255,255,255" shapeBorderWidthUnit="MM" shapeRadiiX="0" shapeRotationType="0" shapeSizeY="0" shapeOffsetY="0" shapeRadiiY="0" shapeOpacity="1" shapeSizeType="0">
              <symbol force_rhr="0" name="markerSymbol" clip_to_extent="1" type="marker" alpha="1">
                <layer enabled="1" locked="0" class="SimpleMarker" pass="0">
                  <prop k="angle" v="0"/>
                  <prop k="color" v="243,166,178,255"/>
                  <prop k="horizontal_anchor_point" v="1"/>
                  <prop k="joinstyle" v="bevel"/>
                  <prop k="name" v="circle"/>
                  <prop k="offset" v="0,0"/>
                  <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
                  <prop k="offset_unit" v="MM"/>
                  <prop k="outline_color" v="35,35,35,255"/>
                  <prop k="outline_style" v="solid"/>
                  <prop k="outline_width" v="0"/>
                  <prop k="outline_width_map_unit_scale" v="3x:0,0,0,0,0,0"/>
                  <prop k="outline_width_unit" v="MM"/>
                  <prop k="scale_method" v="diameter"/>
                  <prop k="size" v="2"/>
                  <prop k="size_map_unit_scale" v="3x:0,0,0,0,0,0"/>
                  <prop k="size_unit" v="MM"/>
                  <prop k="vertical_anchor_point" v="1"/>
                  <data_defined_properties>
                    <Option type="Map">
                      <Option name="name" value="" type="QString"/>
                      <Option name="properties"/>
                      <Option name="type" value="collection" type="QString"/>
                    </Option>
                  </data_defined_properties>
                </layer>
              </symbol>
            </background>
            <shadow shadowOffsetGlobal="1" shadowColor="0,0,0,255" shadowDraw="0" shadowOffsetUnit="MM" shadowScale="100" shadowUnder="0" shadowBlendMode="6" shadowRadiusMapUnitScale="3x:0,0,0,0,0,0" shadowRadiusUnit="MM" shadowRadiusAlphaOnly="0" shadowOpacity="0.7" shadowOffsetAngle="135" shadowOffsetDist="1" shadowOffsetMapUnitScale="3x:0,0,0,0,0,0" shadowRadius="1.5"/>
            <dd_properties>
              <Option type="Map">
                <Option name="name" value="" type="QString"/>
                <Option name="properties"/>
                <Option name="type" value="collection" type="QString"/>
              </Option>
            </dd_properties>
            <substitutions/>
          </text-style>
          <text-format decimals="3" placeDirectionSymbol="0" autoWrapLength="0" multilineAlign="0" formatNumbers="0" plussign="0" rightDirectionSymbol=">" addDirectionSymbol="0" reverseDirectionSymbol="0" wrapChar="" leftDirectionSymbol="&lt;" useMaxLineLengthForAutoWrap="1"/>
          <placement overrunDistanceMapUnitScale="3x:0,0,0,0,0,0" predefinedPositionOrder="TR,TL,BR,BL,R,L,TSR,BSR" offsetUnits="MM" repeatDistanceMapUnitScale="3x:0,0,0,0,0,0" lineAnchorType="0" distMapUnitScale="3x:0,0,0,0,0,0" geometryGenerator="" placement="2" distUnits="MM" priority="5" dist="0" geometryGeneratorEnabled="0" xOffset="0" yOffset="0" centroidInside="0" polygonPlacementFlags="2" quadOffset="4" geometryGeneratorType="PointGeometry" layerType="LineGeometry" maxCurvedCharAngleIn="25" repeatDistance="0" overrunDistanceUnit="MM" fitInPolygonOnly="0" labelOffsetMapUnitScale="3x:0,0,0,0,0,0" rotationAngle="0" preserveRotation="1" lineAnchorPercent="0.5" overrunDistance="0" repeatDistanceUnits="MM" placementFlags="12" offsetType="0" centroidWhole="0" maxCurvedCharAngleOut="-25"/>
          <rendering maxNumLabels="2000" zIndex="0" fontMinPixelSize="3" labelPerPart="0" scaleVisibility="0" minFeatureSize="0" mergeLines="0" obstacle="1" drawLabels="1" limitNumLabels="0" obstacleFactor="1" scaleMax="0" upsidedownLabels="0" fontLimitPixelSize="0" scaleMin="0" fontMaxPixelSize="10000" displayAll="0" obstacleType="1"/>
          <dd_properties>
            <Option type="Map">
              <Option name="name" value="" type="QString"/>
              <Option name="properties" type="Map">
                <Option name="Size" type="Map">
                  <Option name="active" value="false" type="bool"/>
                  <Option name="expression" value="@project_font_size" type="QString"/>
                  <Option name="type" value="3" type="int"/>
                </Option>
              </Option>
              <Option name="type" value="collection" type="QString"/>
            </Option>
          </dd_properties>
          <callout type="simple">
            <Option type="Map">
              <Option name="anchorPoint" value="pole_of_inaccessibility" type="QString"/>
              <Option name="ddProperties" type="Map">
                <Option name="name" value="" type="QString"/>
                <Option name="properties"/>
                <Option name="type" value="collection" type="QString"/>
              </Option>
              <Option name="drawToAllParts" value="false" type="bool"/>
              <Option name="enabled" value="0" type="QString"/>
              <Option name="labelAnchorPoint" value="point_on_exterior" type="QString"/>
              <Option name="lineSymbol" value="&lt;symbol force_rhr=&quot;0&quot; name=&quot;symbol&quot; clip_to_extent=&quot;1&quot; type=&quot;line&quot; alpha=&quot;1&quot;>&lt;layer enabled=&quot;1&quot; locked=&quot;0&quot; class=&quot;SimpleLine&quot; pass=&quot;0&quot;>&lt;prop k=&quot;align_dash_pattern&quot; v=&quot;0&quot;/>&lt;prop k=&quot;capstyle&quot; v=&quot;square&quot;/>&lt;prop k=&quot;customdash&quot; v=&quot;5;2&quot;/>&lt;prop k=&quot;customdash_map_unit_scale&quot; v=&quot;3x:0,0,0,0,0,0&quot;/>&lt;prop k=&quot;customdash_unit&quot; v=&quot;MM&quot;/>&lt;prop k=&quot;dash_pattern_offset&quot; v=&quot;0&quot;/>&lt;prop k=&quot;dash_pattern_offset_map_unit_scale&quot; v=&quot;3x:0,0,0,0,0,0&quot;/>&lt;prop k=&quot;dash_pattern_offset_unit&quot; v=&quot;MM&quot;/>&lt;prop k=&quot;draw_inside_polygon&quot; v=&quot;0&quot;/>&lt;prop k=&quot;joinstyle&quot; v=&quot;bevel&quot;/>&lt;prop k=&quot;line_color&quot; v=&quot;60,60,60,255&quot;/>&lt;prop k=&quot;line_style&quot; v=&quot;solid&quot;/>&lt;prop k=&quot;line_width&quot; v=&quot;0.3&quot;/>&lt;prop k=&quot;line_width_unit&quot; v=&quot;MM&quot;/>&lt;prop k=&quot;offset&quot; v=&quot;0&quot;/>&lt;prop k=&quot;offset_map_unit_scale&quot; v=&quot;3x:0,0,0,0,0,0&quot;/>&lt;prop k=&quot;offset_unit&quot; v=&quot;MM&quot;/>&lt;prop k=&quot;ring_filter&quot; v=&quot;0&quot;/>&lt;prop k=&quot;tweak_dash_pattern_on_corners&quot; v=&quot;0&quot;/>&lt;prop k=&quot;use_custom_dash&quot; v=&quot;0&quot;/>&lt;prop k=&quot;width_map_unit_scale&quot; v=&quot;3x:0,0,0,0,0,0&quot;/>&lt;data_defined_properties>&lt;Option type=&quot;Map&quot;>&lt;Option name=&quot;name&quot; value=&quot;&quot; type=&quot;QString&quot;/>&lt;Option name=&quot;properties&quot;/>&lt;Option name=&quot;type&quot; value=&quot;collection&quot; type=&quot;QString&quot;/>&lt;/Option>&lt;/data_defined_properties>&lt;/layer>&lt;/symbol>" type="QString"/>
              <Option name="minLength" value="0" type="double"/>
              <Option name="minLengthMapUnitScale" value="3x:0,0,0,0,0,0" type="QString"/>
              <Option name="minLengthUnit" value="MM" type="QString"/>
              <Option name="offsetFromAnchor" value="0" type="double"/>
              <Option name="offsetFromAnchorMapUnitScale" value="3x:0,0,0,0,0,0" type="QString"/>
              <Option name="offsetFromAnchorUnit" value="MM" type="QString"/>
              <Option name="offsetFromLabel" value="0" type="double"/>
              <Option name="offsetFromLabelMapUnitScale" value="3x:0,0,0,0,0,0" type="QString"/>
              <Option name="offsetFromLabelUnit" value="MM" type="QString"/>
            </Option>
          </callout>
        </settings>
      </rule>
      <rule active="0" description="lid" key="{ace7b92f-d757-4e05-b84e-f6cfd72468ab}">
        <settings calloutType="simple">
          <text-style fontWeight="50" fontSize="7" fontUnderline="0" textOpacity="1" textOrientation="horizontal" textColor="31,120,180,255" isExpression="0" fontItalic="0" namedStyle="Regular" fieldName="lid" fontSizeMapUnitScale="3x:0,0,0,0,0,0" fontWordSpacing="0" fontSizeUnit="Point" fontLetterSpacing="0" useSubstitutions="0" multilineHeight="1" fontFamily="MS Shell Dlg 2" fontKerning="1" blendMode="0" previewBkgrdColor="255,255,255,255" allowHtml="0" fontStrikeout="0" capitalization="0">
            <text-buffer bufferSizeMapUnitScale="3x:0,0,0,0,0,0" bufferDraw="0" bufferNoFill="1" bufferOpacity="1" bufferBlendMode="0" bufferColor="255,255,255,255" bufferJoinStyle="128" bufferSize="1" bufferSizeUnits="MM"/>
            <text-mask maskSizeUnits="MM" maskSizeMapUnitScale="3x:0,0,0,0,0,0" maskedSymbolLayers="" maskSize="1.5" maskOpacity="1" maskEnabled="0" maskJoinStyle="128" maskType="0"/>
            <background shapeDraw="0" shapeOffsetX="0" shapeType="0" shapeSizeX="0" shapeSizeMapUnitScale="3x:0,0,0,0,0,0" shapeBlendMode="0" shapeBorderWidthMapUnitScale="3x:0,0,0,0,0,0" shapeRotation="0" shapeRadiiUnit="MM" shapeBorderColor="128,128,128,255" shapeBorderWidth="0" shapeJoinStyle="64" shapeOffsetMapUnitScale="3x:0,0,0,0,0,0" shapeSVGFile="" shapeOffsetUnit="MM" shapeSizeUnit="MM" shapeRadiiMapUnitScale="3x:0,0,0,0,0,0" shapeFillColor="255,255,255,255" shapeBorderWidthUnit="MM" shapeRadiiX="0" shapeRotationType="0" shapeSizeY="0" shapeOffsetY="0" shapeRadiiY="0" shapeOpacity="1" shapeSizeType="0">
              <symbol force_rhr="0" name="markerSymbol" clip_to_extent="1" type="marker" alpha="1">
                <layer enabled="1" locked="0" class="SimpleMarker" pass="0">
                  <prop k="angle" v="0"/>
                  <prop k="color" v="141,90,153,255"/>
                  <prop k="horizontal_anchor_point" v="1"/>
                  <prop k="joinstyle" v="bevel"/>
                  <prop k="name" v="circle"/>
                  <prop k="offset" v="0,0"/>
                  <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
                  <prop k="offset_unit" v="MM"/>
                  <prop k="outline_color" v="35,35,35,255"/>
                  <prop k="outline_style" v="solid"/>
                  <prop k="outline_width" v="0"/>
                  <prop k="outline_width_map_unit_scale" v="3x:0,0,0,0,0,0"/>
                  <prop k="outline_width_unit" v="MM"/>
                  <prop k="scale_method" v="diameter"/>
                  <prop k="size" v="2"/>
                  <prop k="size_map_unit_scale" v="3x:0,0,0,0,0,0"/>
                  <prop k="size_unit" v="MM"/>
                  <prop k="vertical_anchor_point" v="1"/>
                  <data_defined_properties>
                    <Option type="Map">
                      <Option name="name" value="" type="QString"/>
                      <Option name="properties"/>
                      <Option name="type" value="collection" type="QString"/>
                    </Option>
                  </data_defined_properties>
                </layer>
              </symbol>
            </background>
            <shadow shadowOffsetGlobal="1" shadowColor="0,0,0,255" shadowDraw="0" shadowOffsetUnit="MM" shadowScale="100" shadowUnder="0" shadowBlendMode="6" shadowRadiusMapUnitScale="3x:0,0,0,0,0,0" shadowRadiusUnit="MM" shadowRadiusAlphaOnly="0" shadowOpacity="0.7" shadowOffsetAngle="135" shadowOffsetDist="1" shadowOffsetMapUnitScale="3x:0,0,0,0,0,0" shadowRadius="1.5"/>
            <dd_properties>
              <Option type="Map">
                <Option name="name" value="" type="QString"/>
                <Option name="properties"/>
                <Option name="type" value="collection" type="QString"/>
              </Option>
            </dd_properties>
            <substitutions/>
          </text-style>
          <text-format decimals="3" placeDirectionSymbol="0" autoWrapLength="0" multilineAlign="0" formatNumbers="0" plussign="0" rightDirectionSymbol=">" addDirectionSymbol="0" reverseDirectionSymbol="0" wrapChar="" leftDirectionSymbol="&lt;" useMaxLineLengthForAutoWrap="1"/>
          <placement overrunDistanceMapUnitScale="3x:0,0,0,0,0,0" predefinedPositionOrder="TR,TL,BR,BL,R,L,TSR,BSR" offsetUnits="MM" repeatDistanceMapUnitScale="3x:0,0,0,0,0,0" lineAnchorType="0" distMapUnitScale="3x:0,0,0,0,0,0" geometryGenerator="" placement="2" distUnits="MM" priority="5" dist="0" geometryGeneratorEnabled="0" xOffset="0" yOffset="0" centroidInside="0" polygonPlacementFlags="2" quadOffset="4" geometryGeneratorType="PointGeometry" layerType="LineGeometry" maxCurvedCharAngleIn="25" repeatDistance="0" overrunDistanceUnit="MM" fitInPolygonOnly="0" labelOffsetMapUnitScale="3x:0,0,0,0,0,0" rotationAngle="0" preserveRotation="1" lineAnchorPercent="0.5" overrunDistance="0" repeatDistanceUnits="MM" placementFlags="12" offsetType="0" centroidWhole="0" maxCurvedCharAngleOut="-25"/>
          <rendering maxNumLabels="2000" zIndex="0" fontMinPixelSize="3" labelPerPart="0" scaleVisibility="0" minFeatureSize="0" mergeLines="0" obstacle="1" drawLabels="1" limitNumLabels="0" obstacleFactor="1" scaleMax="0" upsidedownLabels="0" fontLimitPixelSize="0" scaleMin="0" fontMaxPixelSize="10000" displayAll="0" obstacleType="1"/>
          <dd_properties>
            <Option type="Map">
              <Option name="name" value="" type="QString"/>
              <Option name="properties"/>
              <Option name="type" value="collection" type="QString"/>
            </Option>
          </dd_properties>
          <callout type="simple">
            <Option type="Map">
              <Option name="anchorPoint" value="pole_of_inaccessibility" type="QString"/>
              <Option name="ddProperties" type="Map">
                <Option name="name" value="" type="QString"/>
                <Option name="properties"/>
                <Option name="type" value="collection" type="QString"/>
              </Option>
              <Option name="drawToAllParts" value="false" type="bool"/>
              <Option name="enabled" value="0" type="QString"/>
              <Option name="labelAnchorPoint" value="point_on_exterior" type="QString"/>
              <Option name="lineSymbol" value="&lt;symbol force_rhr=&quot;0&quot; name=&quot;symbol&quot; clip_to_extent=&quot;1&quot; type=&quot;line&quot; alpha=&quot;1&quot;>&lt;layer enabled=&quot;1&quot; locked=&quot;0&quot; class=&quot;SimpleLine&quot; pass=&quot;0&quot;>&lt;prop k=&quot;align_dash_pattern&quot; v=&quot;0&quot;/>&lt;prop k=&quot;capstyle&quot; v=&quot;square&quot;/>&lt;prop k=&quot;customdash&quot; v=&quot;5;2&quot;/>&lt;prop k=&quot;customdash_map_unit_scale&quot; v=&quot;3x:0,0,0,0,0,0&quot;/>&lt;prop k=&quot;customdash_unit&quot; v=&quot;MM&quot;/>&lt;prop k=&quot;dash_pattern_offset&quot; v=&quot;0&quot;/>&lt;prop k=&quot;dash_pattern_offset_map_unit_scale&quot; v=&quot;3x:0,0,0,0,0,0&quot;/>&lt;prop k=&quot;dash_pattern_offset_unit&quot; v=&quot;MM&quot;/>&lt;prop k=&quot;draw_inside_polygon&quot; v=&quot;0&quot;/>&lt;prop k=&quot;joinstyle&quot; v=&quot;bevel&quot;/>&lt;prop k=&quot;line_color&quot; v=&quot;60,60,60,255&quot;/>&lt;prop k=&quot;line_style&quot; v=&quot;solid&quot;/>&lt;prop k=&quot;line_width&quot; v=&quot;0.3&quot;/>&lt;prop k=&quot;line_width_unit&quot; v=&quot;MM&quot;/>&lt;prop k=&quot;offset&quot; v=&quot;0&quot;/>&lt;prop k=&quot;offset_map_unit_scale&quot; v=&quot;3x:0,0,0,0,0,0&quot;/>&lt;prop k=&quot;offset_unit&quot; v=&quot;MM&quot;/>&lt;prop k=&quot;ring_filter&quot; v=&quot;0&quot;/>&lt;prop k=&quot;tweak_dash_pattern_on_corners&quot; v=&quot;0&quot;/>&lt;prop k=&quot;use_custom_dash&quot; v=&quot;0&quot;/>&lt;prop k=&quot;width_map_unit_scale&quot; v=&quot;3x:0,0,0,0,0,0&quot;/>&lt;data_defined_properties>&lt;Option type=&quot;Map&quot;>&lt;Option name=&quot;name&quot; value=&quot;&quot; type=&quot;QString&quot;/>&lt;Option name=&quot;properties&quot;/>&lt;Option name=&quot;type&quot; value=&quot;collection&quot; type=&quot;QString&quot;/>&lt;/Option>&lt;/data_defined_properties>&lt;/layer>&lt;/symbol>" type="QString"/>
              <Option name="minLength" value="0" type="double"/>
              <Option name="minLengthMapUnitScale" value="3x:0,0,0,0,0,0" type="QString"/>
              <Option name="minLengthUnit" value="MM" type="QString"/>
              <Option name="offsetFromAnchor" value="0" type="double"/>
              <Option name="offsetFromAnchorMapUnitScale" value="3x:0,0,0,0,0,0" type="QString"/>
              <Option name="offsetFromAnchorUnit" value="MM" type="QString"/>
              <Option name="offsetFromLabel" value="0" type="double"/>
              <Option name="offsetFromLabelMapUnitScale" value="3x:0,0,0,0,0,0" type="QString"/>
              <Option name="offsetFromLabelUnit" value="MM" type="QString"/>
            </Option>
          </callout>
        </settings>
      </rule>
    </rules>
  </labeling>
  <customproperties>
    <property value="&quot;lid&quot;" key="dualview/previewExpressions"/>
  </customproperties>
  <blendMode>0</blendMode>
  <featureBlendMode>0</featureBlendMode>
  <layerOpacity>1</layerOpacity>
  <geometryOptions geometryPrecision="0" removeDuplicateNodes="0">
    <activeChecks type="StringList">
      <Option value="" type="QString"/>
    </activeChecks>
    <checkConfiguration/>
  </geometryOptions>
  <legend type="default-vector"/>
  <referencedLayers/>
  <fieldConfiguration>
    <field name="lid" configurationFlags="None">
      <editWidget type="">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="wid" configurationFlags="None">
      <editWidget type="">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="grad" configurationFlags="None">
      <editWidget type="">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="styl" configurationFlags="None">
      <editWidget type="">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="oldgrad" configurationFlags="None">
      <editWidget type="">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
  </fieldConfiguration>
  <aliases>
    <alias name="" index="0" field="lid"/>
    <alias name="" index="1" field="wid"/>
    <alias name="" index="2" field="grad"/>
    <alias name="" index="3" field="styl"/>
    <alias name="" index="4" field="oldgrad"/>
  </aliases>
  <defaults>
    <default applyOnUpdate="0" expression="" field="lid"/>
    <default applyOnUpdate="0" expression="" field="wid"/>
    <default applyOnUpdate="0" expression="" field="grad"/>
    <default applyOnUpdate="0" expression="" field="styl"/>
    <default applyOnUpdate="0" expression="" field="oldgrad"/>
  </defaults>
  <constraints>
    <constraint constraints="3" notnull_strength="1" exp_strength="0" unique_strength="1" field="lid"/>
    <constraint constraints="0" notnull_strength="0" exp_strength="0" unique_strength="0" field="wid"/>
    <constraint constraints="0" notnull_strength="0" exp_strength="0" unique_strength="0" field="grad"/>
    <constraint constraints="0" notnull_strength="0" exp_strength="0" unique_strength="0" field="styl"/>
    <constraint constraints="0" notnull_strength="0" exp_strength="0" unique_strength="0" field="oldgrad"/>
  </constraints>
  <constraintExpressions>
    <constraint exp="" desc="" field="lid"/>
    <constraint exp="" desc="" field="wid"/>
    <constraint exp="" desc="" field="grad"/>
    <constraint exp="" desc="" field="styl"/>
    <constraint exp="" desc="" field="oldgrad"/>
  </constraintExpressions>
  <expressionfields/>
  <attributeactions>
    <defaultAction value="{00000000-0000-0000-0000-000000000000}" key="Canvas"/>
  </attributeactions>
  <attributetableconfig actionWidgetStyle="dropDown" sortOrder="0" sortExpression="&quot;styl&quot;">
    <columns>
      <column name="lid" width="-1" hidden="0" type="field"/>
      <column name="wid" width="-1" hidden="0" type="field"/>
      <column name="leng" width="-1" hidden="0" type="field"/>
      <column name="ez" width="-1" hidden="0" type="field"/>
      <column name="sz" width="-1" hidden="0" type="field"/>
      <column name="grad" width="-1" hidden="0" type="field"/>
      <column name="styl" width="-1" hidden="0" type="field"/>
      <column name="oldgrad" width="-1" hidden="0" type="field"/>
      <column width="-1" hidden="1" type="actions"/>
    </columns>
  </attributetableconfig>
  <conditionalstyles>
    <rowstyles/>
    <fieldstyles/>
  </conditionalstyles>
  <storedexpressions/>
  <editform tolerant="1"></editform>
  <editforminit/>
  <editforminitcodesource>0</editforminitcodesource>
  <editforminitfilepath></editforminitfilepath>
  <editforminitcode><![CDATA[]]></editforminitcode>
  <featformsuppress>0</featformsuppress>
  <editorlayout>generatedlayout</editorlayout>
  <editable/>
  <labelOnTop/>
  <dataDefinedFieldProperties/>
  <widgets/>
  <previewExpression>"lid"</previewExpression>
  <mapTip></mapTip>
  <layerGeometryType>1</layerGeometryType>
</qgis>

<!DOCTYPE qgis PUBLIC 'http://mrcc.com/qgis.dtd' 'SYSTEM'>
<qgis maxScale="0" simplifyLocal="1" simplifyDrawingHints="1" version="3.16.0-Hannover" labelsEnabled="1" simplifyDrawingTol="1" minScale="100000000" styleCategories="AllStyleCategories" simplifyMaxScale="1" hasScaleBasedVisibilityFlag="0" readOnly="0" simplifyAlgorithm="0">
  <flags>
    <Identifiable>1</Identifiable>
    <Removable>1</Removable>
    <Searchable>1</Searchable>
  </flags>
  <temporal enabled="0" accumulate="0" endExpression="" fixedDuration="0" durationField="" mode="0" endField="" startExpression="" durationUnit="min" startField="">
    <fixedRange>
      <start></start>
      <end></end>
    </fixedRange>
  </temporal>
  <renderer-v2 enableorderby="0" type="RuleRenderer" symbollevels="0" forceraster="0">
    <rules key="{3514ed2b-7222-4941-8f88-0df6b8d9cb92}">
      <rule symbol="0" label="z adjusted" key="{03e8eb43-3ad1-40bb-9baf-9d89ee2bff36}" filter="z!=oldz"/>
      <rule symbol="1" key="{96f7707b-d512-4313-b050-c641f648999f}" filter="ELSE"/>
    </rules>
    <symbols>
      <symbol alpha="1" type="marker" name="0" force_rhr="0" clip_to_extent="1">
        <layer enabled="1" pass="0" locked="0" class="SimpleMarker">
          <prop v="0" k="angle"/>
          <prop v="190,207,80,255" k="color"/>
          <prop v="1" k="horizontal_anchor_point"/>
          <prop v="bevel" k="joinstyle"/>
          <prop v="circle" k="name"/>
          <prop v="0,0" k="offset"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
          <prop v="MM" k="offset_unit"/>
          <prop v="216,64,214,255" k="outline_color"/>
          <prop v="solid" k="outline_style"/>
          <prop v="1" k="outline_width"/>
          <prop v="3x:0,0,0,0,0,0" k="outline_width_map_unit_scale"/>
          <prop v="MM" k="outline_width_unit"/>
          <prop v="diameter" k="scale_method"/>
          <prop v="2" k="size"/>
          <prop v="3x:0,0,0,0,0,0" k="size_map_unit_scale"/>
          <prop v="MM" k="size_unit"/>
          <prop v="1" k="vertical_anchor_point"/>
          <data_defined_properties>
            <Option type="Map">
              <Option type="QString" name="name" value=""/>
              <Option name="properties"/>
              <Option type="QString" name="type" value="collection"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
      <symbol alpha="0.5" type="marker" name="1" force_rhr="0" clip_to_extent="1">
        <layer enabled="1" pass="0" locked="0" class="SimpleMarker">
          <prop v="0" k="angle"/>
          <prop v="190,207,80,255" k="color"/>
          <prop v="1" k="horizontal_anchor_point"/>
          <prop v="bevel" k="joinstyle"/>
          <prop v="circle" k="name"/>
          <prop v="0,0" k="offset"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
          <prop v="MM" k="offset_unit"/>
          <prop v="35,35,35,255" k="outline_color"/>
          <prop v="solid" k="outline_style"/>
          <prop v="0" k="outline_width"/>
          <prop v="3x:0,0,0,0,0,0" k="outline_width_map_unit_scale"/>
          <prop v="MM" k="outline_width_unit"/>
          <prop v="diameter" k="scale_method"/>
          <prop v="2" k="size"/>
          <prop v="3x:0,0,0,0,0,0" k="size_map_unit_scale"/>
          <prop v="MM" k="size_unit"/>
          <prop v="1" k="vertical_anchor_point"/>
          <data_defined_properties>
            <Option type="Map">
              <Option type="QString" name="name" value=""/>
              <Option name="properties"/>
              <Option type="QString" name="type" value="collection"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
    </symbols>
  </renderer-v2>
  <labeling type="rule-based">
    <rules key="{5243b553-723b-42dc-bd6b-82a09217869d}">
      <rule description="z" key="{e58a3b43-977e-4398-8900-f135b68180ff}" filter="adj=0">
        <settings calloutType="simple">
          <text-style fontSize="6" textOpacity="1" multilineHeight="1" fieldName="z" fontFamily="MS Shell Dlg 2" fontKerning="1" fontLetterSpacing="0" fontWordSpacing="0" fontSizeUnit="Point" textOrientation="horizontal" textColor="128,17,25,255" blendMode="0" fontWeight="50" capitalization="0" fontItalic="0" useSubstitutions="0" previewBkgrdColor="255,255,255,255" namedStyle="Regular" allowHtml="0" isExpression="0" fontUnderline="0" fontSizeMapUnitScale="3x:0,0,0,0,0,0" fontStrikeout="0">
            <text-buffer bufferSize="1" bufferColor="255,255,255,255" bufferNoFill="1" bufferJoinStyle="128" bufferSizeMapUnitScale="3x:0,0,0,0,0,0" bufferDraw="0" bufferOpacity="1" bufferSizeUnits="MM" bufferBlendMode="0"/>
            <text-mask maskSizeUnits="MM" maskEnabled="0" maskedSymbolLayers="" maskJoinStyle="128" maskOpacity="1" maskType="0" maskSize="1.5" maskSizeMapUnitScale="3x:0,0,0,0,0,0"/>
            <background shapeSizeY="0" shapeSizeUnit="MM" shapeSizeMapUnitScale="3x:0,0,0,0,0,0" shapeOffsetMapUnitScale="3x:0,0,0,0,0,0" shapeSVGFile="" shapeBorderWidth="0" shapeRadiiY="0" shapeBorderWidthUnit="MM" shapeBorderColor="128,128,128,255" shapeRadiiUnit="MM" shapeOffsetY="0" shapeRotationType="0" shapeRotation="0" shapeJoinStyle="64" shapeBlendMode="0" shapeOpacity="1" shapeType="0" shapeFillColor="255,255,255,255" shapeSizeType="0" shapeRadiiMapUnitScale="3x:0,0,0,0,0,0" shapeRadiiX="0" shapeDraw="0" shapeOffsetUnit="MM" shapeSizeX="0" shapeOffsetX="0" shapeBorderWidthMapUnitScale="3x:0,0,0,0,0,0">
              <symbol alpha="1" type="marker" name="markerSymbol" force_rhr="0" clip_to_extent="1">
                <layer enabled="1" pass="0" locked="0" class="SimpleMarker">
                  <prop v="0" k="angle"/>
                  <prop v="141,90,153,255" k="color"/>
                  <prop v="1" k="horizontal_anchor_point"/>
                  <prop v="bevel" k="joinstyle"/>
                  <prop v="circle" k="name"/>
                  <prop v="0,0" k="offset"/>
                  <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
                  <prop v="MM" k="offset_unit"/>
                  <prop v="35,35,35,255" k="outline_color"/>
                  <prop v="solid" k="outline_style"/>
                  <prop v="0" k="outline_width"/>
                  <prop v="3x:0,0,0,0,0,0" k="outline_width_map_unit_scale"/>
                  <prop v="MM" k="outline_width_unit"/>
                  <prop v="diameter" k="scale_method"/>
                  <prop v="2" k="size"/>
                  <prop v="3x:0,0,0,0,0,0" k="size_map_unit_scale"/>
                  <prop v="MM" k="size_unit"/>
                  <prop v="1" k="vertical_anchor_point"/>
                  <data_defined_properties>
                    <Option type="Map">
                      <Option type="QString" name="name" value=""/>
                      <Option name="properties"/>
                      <Option type="QString" name="type" value="collection"/>
                    </Option>
                  </data_defined_properties>
                </layer>
              </symbol>
            </background>
            <shadow shadowDraw="0" shadowRadiusMapUnitScale="3x:0,0,0,0,0,0" shadowOffsetAngle="135" shadowRadius="1.5" shadowOffsetUnit="MM" shadowRadiusAlphaOnly="0" shadowUnder="0" shadowColor="0,0,0,255" shadowOffsetGlobal="1" shadowRadiusUnit="MM" shadowOffsetMapUnitScale="3x:0,0,0,0,0,0" shadowScale="100" shadowOffsetDist="1" shadowBlendMode="6" shadowOpacity="0.7"/>
            <dd_properties>
              <Option type="Map">
                <Option type="QString" name="name" value=""/>
                <Option name="properties"/>
                <Option type="QString" name="type" value="collection"/>
              </Option>
            </dd_properties>
            <substitutions/>
          </text-style>
          <text-format wrapChar="" addDirectionSymbol="0" leftDirectionSymbol="&lt;" reverseDirectionSymbol="0" rightDirectionSymbol=">" decimals="3" plussign="0" formatNumbers="0" autoWrapLength="0" multilineAlign="3" useMaxLineLengthForAutoWrap="1" placeDirectionSymbol="0"/>
          <placement yOffset="-0.5" distUnits="MM" repeatDistanceMapUnitScale="3x:0,0,0,0,0,0" placementFlags="10" maxCurvedCharAngleOut="-25" labelOffsetMapUnitScale="3x:0,0,0,0,0,0" preserveRotation="1" geometryGenerator="" offsetUnits="MM" overrunDistanceUnit="MM" overrunDistanceMapUnitScale="3x:0,0,0,0,0,0" geometryGeneratorType="PointGeometry" polygonPlacementFlags="2" distMapUnitScale="3x:0,0,0,0,0,0" layerType="PointGeometry" predefinedPositionOrder="TR,TL,BR,BL,R,L,TSR,BSR" rotationAngle="0" dist="0" repeatDistanceUnits="MM" xOffset="0" offsetType="0" quadOffset="1" lineAnchorType="0" placement="1" geometryGeneratorEnabled="0" maxCurvedCharAngleIn="25" priority="5" centroidWhole="0" fitInPolygonOnly="0" repeatDistance="0" overrunDistance="0" lineAnchorPercent="0.5" centroidInside="0"/>
          <rendering scaleVisibility="0" minFeatureSize="0" fontMaxPixelSize="10000" upsidedownLabels="0" obstacleType="1" obstacleFactor="1" labelPerPart="0" obstacle="1" maxNumLabels="2000" fontMinPixelSize="3" mergeLines="0" drawLabels="1" scaleMax="0" fontLimitPixelSize="0" scaleMin="0" limitNumLabels="0" displayAll="0" zIndex="0"/>
          <dd_properties>
            <Option type="Map">
              <Option type="QString" name="name" value=""/>
              <Option type="Map" name="properties">
                <Option type="Map" name="Size">
                  <Option type="bool" name="active" value="false"/>
                  <Option type="QString" name="expression" value="@project_font_size"/>
                  <Option type="int" name="type" value="3"/>
                </Option>
              </Option>
              <Option type="QString" name="type" value="collection"/>
            </Option>
          </dd_properties>
          <callout type="simple">
            <Option type="Map">
              <Option type="QString" name="anchorPoint" value="pole_of_inaccessibility"/>
              <Option type="Map" name="ddProperties">
                <Option type="QString" name="name" value=""/>
                <Option name="properties"/>
                <Option type="QString" name="type" value="collection"/>
              </Option>
              <Option type="bool" name="drawToAllParts" value="false"/>
              <Option type="QString" name="enabled" value="0"/>
              <Option type="QString" name="labelAnchorPoint" value="point_on_exterior"/>
              <Option type="QString" name="lineSymbol" value="&lt;symbol alpha=&quot;1&quot; type=&quot;line&quot; name=&quot;symbol&quot; force_rhr=&quot;0&quot; clip_to_extent=&quot;1&quot;>&lt;layer enabled=&quot;1&quot; pass=&quot;0&quot; locked=&quot;0&quot; class=&quot;SimpleLine&quot;>&lt;prop v=&quot;0&quot; k=&quot;align_dash_pattern&quot;/>&lt;prop v=&quot;square&quot; k=&quot;capstyle&quot;/>&lt;prop v=&quot;5;2&quot; k=&quot;customdash&quot;/>&lt;prop v=&quot;3x:0,0,0,0,0,0&quot; k=&quot;customdash_map_unit_scale&quot;/>&lt;prop v=&quot;MM&quot; k=&quot;customdash_unit&quot;/>&lt;prop v=&quot;0&quot; k=&quot;dash_pattern_offset&quot;/>&lt;prop v=&quot;3x:0,0,0,0,0,0&quot; k=&quot;dash_pattern_offset_map_unit_scale&quot;/>&lt;prop v=&quot;MM&quot; k=&quot;dash_pattern_offset_unit&quot;/>&lt;prop v=&quot;0&quot; k=&quot;draw_inside_polygon&quot;/>&lt;prop v=&quot;bevel&quot; k=&quot;joinstyle&quot;/>&lt;prop v=&quot;60,60,60,255&quot; k=&quot;line_color&quot;/>&lt;prop v=&quot;solid&quot; k=&quot;line_style&quot;/>&lt;prop v=&quot;0.3&quot; k=&quot;line_width&quot;/>&lt;prop v=&quot;MM&quot; k=&quot;line_width_unit&quot;/>&lt;prop v=&quot;0&quot; k=&quot;offset&quot;/>&lt;prop v=&quot;3x:0,0,0,0,0,0&quot; k=&quot;offset_map_unit_scale&quot;/>&lt;prop v=&quot;MM&quot; k=&quot;offset_unit&quot;/>&lt;prop v=&quot;0&quot; k=&quot;ring_filter&quot;/>&lt;prop v=&quot;0&quot; k=&quot;tweak_dash_pattern_on_corners&quot;/>&lt;prop v=&quot;0&quot; k=&quot;use_custom_dash&quot;/>&lt;prop v=&quot;3x:0,0,0,0,0,0&quot; k=&quot;width_map_unit_scale&quot;/>&lt;data_defined_properties>&lt;Option type=&quot;Map&quot;>&lt;Option type=&quot;QString&quot; name=&quot;name&quot; value=&quot;&quot;/>&lt;Option name=&quot;properties&quot;/>&lt;Option type=&quot;QString&quot; name=&quot;type&quot; value=&quot;collection&quot;/>&lt;/Option>&lt;/data_defined_properties>&lt;/layer>&lt;/symbol>"/>
              <Option type="double" name="minLength" value="0"/>
              <Option type="QString" name="minLengthMapUnitScale" value="3x:0,0,0,0,0,0"/>
              <Option type="QString" name="minLengthUnit" value="MM"/>
              <Option type="double" name="offsetFromAnchor" value="0"/>
              <Option type="QString" name="offsetFromAnchorMapUnitScale" value="3x:0,0,0,0,0,0"/>
              <Option type="QString" name="offsetFromAnchorUnit" value="MM"/>
              <Option type="double" name="offsetFromLabel" value="0"/>
              <Option type="QString" name="offsetFromLabelMapUnitScale" value="3x:0,0,0,0,0,0"/>
              <Option type="QString" name="offsetFromLabelUnit" value="MM"/>
            </Option>
          </callout>
        </settings>
      </rule>
      <rule description="z" key="{cd0e3c7b-ba3d-4e19-b5c3-510e55286551}" filter="adj>0">
        <settings calloutType="simple">
          <text-style fontSize="8" textOpacity="1" multilineHeight="1" fieldName="z" fontFamily="MS Shell Dlg 2" fontKerning="1" fontLetterSpacing="0" fontWordSpacing="0" fontSizeUnit="Point" textOrientation="horizontal" textColor="128,17,25,255" blendMode="0" fontWeight="50" capitalization="0" fontItalic="0" useSubstitutions="0" previewBkgrdColor="255,255,255,255" namedStyle="Regular" allowHtml="0" isExpression="0" fontUnderline="0" fontSizeMapUnitScale="3x:0,0,0,0,0,0" fontStrikeout="0">
            <text-buffer bufferSize="1" bufferColor="255,255,255,255" bufferNoFill="1" bufferJoinStyle="128" bufferSizeMapUnitScale="3x:0,0,0,0,0,0" bufferDraw="1" bufferOpacity="0.5" bufferSizeUnits="MM" bufferBlendMode="0"/>
            <text-mask maskSizeUnits="MM" maskEnabled="0" maskedSymbolLayers="" maskJoinStyle="128" maskOpacity="1" maskType="0" maskSize="1.5" maskSizeMapUnitScale="3x:0,0,0,0,0,0"/>
            <background shapeSizeY="0" shapeSizeUnit="MM" shapeSizeMapUnitScale="3x:0,0,0,0,0,0" shapeOffsetMapUnitScale="3x:0,0,0,0,0,0" shapeSVGFile="" shapeBorderWidth="0" shapeRadiiY="0" shapeBorderWidthUnit="MM" shapeBorderColor="128,128,128,255" shapeRadiiUnit="MM" shapeOffsetY="0" shapeRotationType="0" shapeRotation="0" shapeJoinStyle="64" shapeBlendMode="0" shapeOpacity="1" shapeType="0" shapeFillColor="255,255,255,255" shapeSizeType="0" shapeRadiiMapUnitScale="3x:0,0,0,0,0,0" shapeRadiiX="0" shapeDraw="0" shapeOffsetUnit="MM" shapeSizeX="0" shapeOffsetX="0" shapeBorderWidthMapUnitScale="3x:0,0,0,0,0,0">
              <symbol alpha="1" type="marker" name="markerSymbol" force_rhr="0" clip_to_extent="1">
                <layer enabled="1" pass="0" locked="0" class="SimpleMarker">
                  <prop v="0" k="angle"/>
                  <prop v="141,90,153,255" k="color"/>
                  <prop v="1" k="horizontal_anchor_point"/>
                  <prop v="bevel" k="joinstyle"/>
                  <prop v="circle" k="name"/>
                  <prop v="0,0" k="offset"/>
                  <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
                  <prop v="MM" k="offset_unit"/>
                  <prop v="35,35,35,255" k="outline_color"/>
                  <prop v="solid" k="outline_style"/>
                  <prop v="0" k="outline_width"/>
                  <prop v="3x:0,0,0,0,0,0" k="outline_width_map_unit_scale"/>
                  <prop v="MM" k="outline_width_unit"/>
                  <prop v="diameter" k="scale_method"/>
                  <prop v="2" k="size"/>
                  <prop v="3x:0,0,0,0,0,0" k="size_map_unit_scale"/>
                  <prop v="MM" k="size_unit"/>
                  <prop v="1" k="vertical_anchor_point"/>
                  <data_defined_properties>
                    <Option type="Map">
                      <Option type="QString" name="name" value=""/>
                      <Option name="properties"/>
                      <Option type="QString" name="type" value="collection"/>
                    </Option>
                  </data_defined_properties>
                </layer>
              </symbol>
            </background>
            <shadow shadowDraw="0" shadowRadiusMapUnitScale="3x:0,0,0,0,0,0" shadowOffsetAngle="135" shadowRadius="1.5" shadowOffsetUnit="MM" shadowRadiusAlphaOnly="0" shadowUnder="0" shadowColor="0,0,0,255" shadowOffsetGlobal="1" shadowRadiusUnit="MM" shadowOffsetMapUnitScale="3x:0,0,0,0,0,0" shadowScale="100" shadowOffsetDist="1" shadowBlendMode="6" shadowOpacity="0.7"/>
            <dd_properties>
              <Option type="Map">
                <Option type="QString" name="name" value=""/>
                <Option name="properties"/>
                <Option type="QString" name="type" value="collection"/>
              </Option>
            </dd_properties>
            <substitutions/>
          </text-style>
          <text-format wrapChar="" addDirectionSymbol="0" leftDirectionSymbol="&lt;" reverseDirectionSymbol="0" rightDirectionSymbol=">" decimals="3" plussign="0" formatNumbers="0" autoWrapLength="0" multilineAlign="3" useMaxLineLengthForAutoWrap="1" placeDirectionSymbol="0"/>
          <placement yOffset="-0.5" distUnits="MM" repeatDistanceMapUnitScale="3x:0,0,0,0,0,0" placementFlags="10" maxCurvedCharAngleOut="-25" labelOffsetMapUnitScale="3x:0,0,0,0,0,0" preserveRotation="1" geometryGenerator="" offsetUnits="MM" overrunDistanceUnit="MM" overrunDistanceMapUnitScale="3x:0,0,0,0,0,0" geometryGeneratorType="PointGeometry" polygonPlacementFlags="2" distMapUnitScale="3x:0,0,0,0,0,0" layerType="PointGeometry" predefinedPositionOrder="TR,TL,BR,BL,R,L,TSR,BSR" rotationAngle="0" dist="0" repeatDistanceUnits="MM" xOffset="0" offsetType="0" quadOffset="1" lineAnchorType="0" placement="1" geometryGeneratorEnabled="0" maxCurvedCharAngleIn="25" priority="5" centroidWhole="0" fitInPolygonOnly="0" repeatDistance="0" overrunDistance="0" lineAnchorPercent="0.5" centroidInside="0"/>
          <rendering scaleVisibility="0" minFeatureSize="0" fontMaxPixelSize="10000" upsidedownLabels="0" obstacleType="1" obstacleFactor="1" labelPerPart="0" obstacle="1" maxNumLabels="2000" fontMinPixelSize="3" mergeLines="0" drawLabels="1" scaleMax="0" fontLimitPixelSize="0" scaleMin="0" limitNumLabels="0" displayAll="0" zIndex="0"/>
          <dd_properties>
            <Option type="Map">
              <Option type="QString" name="name" value=""/>
              <Option type="Map" name="properties">
                <Option type="Map" name="Size">
                  <Option type="bool" name="active" value="true"/>
                  <Option type="QString" name="expression" value="@project_font_size"/>
                  <Option type="int" name="type" value="3"/>
                </Option>
              </Option>
              <Option type="QString" name="type" value="collection"/>
            </Option>
          </dd_properties>
          <callout type="simple">
            <Option type="Map">
              <Option type="QString" name="anchorPoint" value="pole_of_inaccessibility"/>
              <Option type="Map" name="ddProperties">
                <Option type="QString" name="name" value=""/>
                <Option name="properties"/>
                <Option type="QString" name="type" value="collection"/>
              </Option>
              <Option type="bool" name="drawToAllParts" value="false"/>
              <Option type="QString" name="enabled" value="0"/>
              <Option type="QString" name="labelAnchorPoint" value="point_on_exterior"/>
              <Option type="QString" name="lineSymbol" value="&lt;symbol alpha=&quot;1&quot; type=&quot;line&quot; name=&quot;symbol&quot; force_rhr=&quot;0&quot; clip_to_extent=&quot;1&quot;>&lt;layer enabled=&quot;1&quot; pass=&quot;0&quot; locked=&quot;0&quot; class=&quot;SimpleLine&quot;>&lt;prop v=&quot;0&quot; k=&quot;align_dash_pattern&quot;/>&lt;prop v=&quot;square&quot; k=&quot;capstyle&quot;/>&lt;prop v=&quot;5;2&quot; k=&quot;customdash&quot;/>&lt;prop v=&quot;3x:0,0,0,0,0,0&quot; k=&quot;customdash_map_unit_scale&quot;/>&lt;prop v=&quot;MM&quot; k=&quot;customdash_unit&quot;/>&lt;prop v=&quot;0&quot; k=&quot;dash_pattern_offset&quot;/>&lt;prop v=&quot;3x:0,0,0,0,0,0&quot; k=&quot;dash_pattern_offset_map_unit_scale&quot;/>&lt;prop v=&quot;MM&quot; k=&quot;dash_pattern_offset_unit&quot;/>&lt;prop v=&quot;0&quot; k=&quot;draw_inside_polygon&quot;/>&lt;prop v=&quot;bevel&quot; k=&quot;joinstyle&quot;/>&lt;prop v=&quot;60,60,60,255&quot; k=&quot;line_color&quot;/>&lt;prop v=&quot;solid&quot; k=&quot;line_style&quot;/>&lt;prop v=&quot;0.3&quot; k=&quot;line_width&quot;/>&lt;prop v=&quot;MM&quot; k=&quot;line_width_unit&quot;/>&lt;prop v=&quot;0&quot; k=&quot;offset&quot;/>&lt;prop v=&quot;3x:0,0,0,0,0,0&quot; k=&quot;offset_map_unit_scale&quot;/>&lt;prop v=&quot;MM&quot; k=&quot;offset_unit&quot;/>&lt;prop v=&quot;0&quot; k=&quot;ring_filter&quot;/>&lt;prop v=&quot;0&quot; k=&quot;tweak_dash_pattern_on_corners&quot;/>&lt;prop v=&quot;0&quot; k=&quot;use_custom_dash&quot;/>&lt;prop v=&quot;3x:0,0,0,0,0,0&quot; k=&quot;width_map_unit_scale&quot;/>&lt;data_defined_properties>&lt;Option type=&quot;Map&quot;>&lt;Option type=&quot;QString&quot; name=&quot;name&quot; value=&quot;&quot;/>&lt;Option name=&quot;properties&quot;/>&lt;Option type=&quot;QString&quot; name=&quot;type&quot; value=&quot;collection&quot;/>&lt;/Option>&lt;/data_defined_properties>&lt;/layer>&lt;/symbol>"/>
              <Option type="double" name="minLength" value="0"/>
              <Option type="QString" name="minLengthMapUnitScale" value="3x:0,0,0,0,0,0"/>
              <Option type="QString" name="minLengthUnit" value="MM"/>
              <Option type="double" name="offsetFromAnchor" value="0"/>
              <Option type="QString" name="offsetFromAnchorMapUnitScale" value="3x:0,0,0,0,0,0"/>
              <Option type="QString" name="offsetFromAnchorUnit" value="MM"/>
              <Option type="double" name="offsetFromLabel" value="0"/>
              <Option type="QString" name="offsetFromLabelMapUnitScale" value="3x:0,0,0,0,0,0"/>
              <Option type="QString" name="offsetFromLabelUnit" value="MM"/>
            </Option>
          </callout>
        </settings>
      </rule>
      <rule description="id" active="0" key="{852c3cb0-4179-440e-a679-d90ee38f8754}" filter="adj=0">
        <settings calloutType="simple">
          <text-style fontSize="6" textOpacity="0.5" multilineHeight="1" fieldName="id" fontFamily="Arial" fontKerning="1" fontLetterSpacing="0" fontWordSpacing="0" fontSizeUnit="Point" textOrientation="horizontal" textColor="128,17,25,255" blendMode="0" fontWeight="50" capitalization="0" fontItalic="0" useSubstitutions="0" previewBkgrdColor="255,255,255,255" namedStyle="Regular" allowHtml="0" isExpression="0" fontUnderline="0" fontSizeMapUnitScale="3x:0,0,0,0,0,0" fontStrikeout="0">
            <text-buffer bufferSize="1" bufferColor="255,255,255,255" bufferNoFill="1" bufferJoinStyle="128" bufferSizeMapUnitScale="3x:0,0,0,0,0,0" bufferDraw="0" bufferOpacity="1" bufferSizeUnits="MM" bufferBlendMode="0"/>
            <text-mask maskSizeUnits="MM" maskEnabled="0" maskedSymbolLayers="" maskJoinStyle="128" maskOpacity="1" maskType="0" maskSize="1.5" maskSizeMapUnitScale="3x:0,0,0,0,0,0"/>
            <background shapeSizeY="0" shapeSizeUnit="MM" shapeSizeMapUnitScale="3x:0,0,0,0,0,0" shapeOffsetMapUnitScale="3x:0,0,0,0,0,0" shapeSVGFile="" shapeBorderWidth="0" shapeRadiiY="0" shapeBorderWidthUnit="MM" shapeBorderColor="128,128,128,255" shapeRadiiUnit="MM" shapeOffsetY="0" shapeRotationType="0" shapeRotation="0" shapeJoinStyle="64" shapeBlendMode="0" shapeOpacity="1" shapeType="0" shapeFillColor="255,255,255,255" shapeSizeType="0" shapeRadiiMapUnitScale="3x:0,0,0,0,0,0" shapeRadiiX="0" shapeDraw="0" shapeOffsetUnit="MM" shapeSizeX="0" shapeOffsetX="0" shapeBorderWidthMapUnitScale="3x:0,0,0,0,0,0">
              <symbol alpha="1" type="marker" name="markerSymbol" force_rhr="0" clip_to_extent="1">
                <layer enabled="1" pass="0" locked="0" class="SimpleMarker">
                  <prop v="0" k="angle"/>
                  <prop v="243,166,178,255" k="color"/>
                  <prop v="1" k="horizontal_anchor_point"/>
                  <prop v="bevel" k="joinstyle"/>
                  <prop v="circle" k="name"/>
                  <prop v="0,0" k="offset"/>
                  <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
                  <prop v="MM" k="offset_unit"/>
                  <prop v="35,35,35,255" k="outline_color"/>
                  <prop v="solid" k="outline_style"/>
                  <prop v="0" k="outline_width"/>
                  <prop v="3x:0,0,0,0,0,0" k="outline_width_map_unit_scale"/>
                  <prop v="MM" k="outline_width_unit"/>
                  <prop v="diameter" k="scale_method"/>
                  <prop v="2" k="size"/>
                  <prop v="3x:0,0,0,0,0,0" k="size_map_unit_scale"/>
                  <prop v="MM" k="size_unit"/>
                  <prop v="1" k="vertical_anchor_point"/>
                  <data_defined_properties>
                    <Option type="Map">
                      <Option type="QString" name="name" value=""/>
                      <Option name="properties"/>
                      <Option type="QString" name="type" value="collection"/>
                    </Option>
                  </data_defined_properties>
                </layer>
              </symbol>
            </background>
            <shadow shadowDraw="0" shadowRadiusMapUnitScale="3x:0,0,0,0,0,0" shadowOffsetAngle="135" shadowRadius="1.5" shadowOffsetUnit="MM" shadowRadiusAlphaOnly="0" shadowUnder="0" shadowColor="0,0,0,255" shadowOffsetGlobal="1" shadowRadiusUnit="MM" shadowOffsetMapUnitScale="3x:0,0,0,0,0,0" shadowScale="100" shadowOffsetDist="1" shadowBlendMode="6" shadowOpacity="0.7"/>
            <dd_properties>
              <Option type="Map">
                <Option type="QString" name="name" value=""/>
                <Option name="properties"/>
                <Option type="QString" name="type" value="collection"/>
              </Option>
            </dd_properties>
            <substitutions/>
          </text-style>
          <text-format wrapChar="" addDirectionSymbol="0" leftDirectionSymbol="&lt;" reverseDirectionSymbol="0" rightDirectionSymbol=">" decimals="3" plussign="0" formatNumbers="0" autoWrapLength="0" multilineAlign="3" useMaxLineLengthForAutoWrap="1" placeDirectionSymbol="0"/>
          <placement yOffset="1" distUnits="MM" repeatDistanceMapUnitScale="3x:0,0,0,0,0,0" placementFlags="10" maxCurvedCharAngleOut="-25" labelOffsetMapUnitScale="3x:0,0,0,0,0,0" preserveRotation="1" geometryGenerator="" offsetUnits="MM" overrunDistanceUnit="MM" overrunDistanceMapUnitScale="3x:0,0,0,0,0,0" geometryGeneratorType="PointGeometry" polygonPlacementFlags="2" distMapUnitScale="3x:0,0,0,0,0,0" layerType="PointGeometry" predefinedPositionOrder="TR,TL,BR,BL,R,L,TSR,BSR" rotationAngle="0" dist="0" repeatDistanceUnits="MM" xOffset="0" offsetType="0" quadOffset="7" lineAnchorType="0" placement="1" geometryGeneratorEnabled="0" maxCurvedCharAngleIn="25" priority="5" centroidWhole="0" fitInPolygonOnly="0" repeatDistance="0" overrunDistance="0" lineAnchorPercent="0.5" centroidInside="0"/>
          <rendering scaleVisibility="0" minFeatureSize="0" fontMaxPixelSize="10000" upsidedownLabels="0" obstacleType="1" obstacleFactor="1" labelPerPart="0" obstacle="1" maxNumLabels="2000" fontMinPixelSize="3" mergeLines="0" drawLabels="1" scaleMax="0" fontLimitPixelSize="0" scaleMin="0" limitNumLabels="0" displayAll="0" zIndex="0"/>
          <dd_properties>
            <Option type="Map">
              <Option type="QString" name="name" value=""/>
              <Option name="properties"/>
              <Option type="QString" name="type" value="collection"/>
            </Option>
          </dd_properties>
          <callout type="simple">
            <Option type="Map">
              <Option type="QString" name="anchorPoint" value="pole_of_inaccessibility"/>
              <Option type="Map" name="ddProperties">
                <Option type="QString" name="name" value=""/>
                <Option name="properties"/>
                <Option type="QString" name="type" value="collection"/>
              </Option>
              <Option type="bool" name="drawToAllParts" value="false"/>
              <Option type="QString" name="enabled" value="0"/>
              <Option type="QString" name="labelAnchorPoint" value="point_on_exterior"/>
              <Option type="QString" name="lineSymbol" value="&lt;symbol alpha=&quot;1&quot; type=&quot;line&quot; name=&quot;symbol&quot; force_rhr=&quot;0&quot; clip_to_extent=&quot;1&quot;>&lt;layer enabled=&quot;1&quot; pass=&quot;0&quot; locked=&quot;0&quot; class=&quot;SimpleLine&quot;>&lt;prop v=&quot;0&quot; k=&quot;align_dash_pattern&quot;/>&lt;prop v=&quot;square&quot; k=&quot;capstyle&quot;/>&lt;prop v=&quot;5;2&quot; k=&quot;customdash&quot;/>&lt;prop v=&quot;3x:0,0,0,0,0,0&quot; k=&quot;customdash_map_unit_scale&quot;/>&lt;prop v=&quot;MM&quot; k=&quot;customdash_unit&quot;/>&lt;prop v=&quot;0&quot; k=&quot;dash_pattern_offset&quot;/>&lt;prop v=&quot;3x:0,0,0,0,0,0&quot; k=&quot;dash_pattern_offset_map_unit_scale&quot;/>&lt;prop v=&quot;MM&quot; k=&quot;dash_pattern_offset_unit&quot;/>&lt;prop v=&quot;0&quot; k=&quot;draw_inside_polygon&quot;/>&lt;prop v=&quot;bevel&quot; k=&quot;joinstyle&quot;/>&lt;prop v=&quot;60,60,60,255&quot; k=&quot;line_color&quot;/>&lt;prop v=&quot;solid&quot; k=&quot;line_style&quot;/>&lt;prop v=&quot;0.3&quot; k=&quot;line_width&quot;/>&lt;prop v=&quot;MM&quot; k=&quot;line_width_unit&quot;/>&lt;prop v=&quot;0&quot; k=&quot;offset&quot;/>&lt;prop v=&quot;3x:0,0,0,0,0,0&quot; k=&quot;offset_map_unit_scale&quot;/>&lt;prop v=&quot;MM&quot; k=&quot;offset_unit&quot;/>&lt;prop v=&quot;0&quot; k=&quot;ring_filter&quot;/>&lt;prop v=&quot;0&quot; k=&quot;tweak_dash_pattern_on_corners&quot;/>&lt;prop v=&quot;0&quot; k=&quot;use_custom_dash&quot;/>&lt;prop v=&quot;3x:0,0,0,0,0,0&quot; k=&quot;width_map_unit_scale&quot;/>&lt;data_defined_properties>&lt;Option type=&quot;Map&quot;>&lt;Option type=&quot;QString&quot; name=&quot;name&quot; value=&quot;&quot;/>&lt;Option name=&quot;properties&quot;/>&lt;Option type=&quot;QString&quot; name=&quot;type&quot; value=&quot;collection&quot;/>&lt;/Option>&lt;/data_defined_properties>&lt;/layer>&lt;/symbol>"/>
              <Option type="double" name="minLength" value="0"/>
              <Option type="QString" name="minLengthMapUnitScale" value="3x:0,0,0,0,0,0"/>
              <Option type="QString" name="minLengthUnit" value="MM"/>
              <Option type="double" name="offsetFromAnchor" value="0"/>
              <Option type="QString" name="offsetFromAnchorMapUnitScale" value="3x:0,0,0,0,0,0"/>
              <Option type="QString" name="offsetFromAnchorUnit" value="MM"/>
              <Option type="double" name="offsetFromLabel" value="0"/>
              <Option type="QString" name="offsetFromLabelMapUnitScale" value="3x:0,0,0,0,0,0"/>
              <Option type="QString" name="offsetFromLabelUnit" value="MM"/>
            </Option>
          </callout>
        </settings>
      </rule>
      <rule description="id" key="{4b676fd6-7b9c-4c88-8dda-8ee160baa548}" filter="adj>0">
        <settings calloutType="simple">
          <text-style fontSize="7" textOpacity="0.5" multilineHeight="1" fieldName="id" fontFamily="Arial" fontKerning="1" fontLetterSpacing="0" fontWordSpacing="0" fontSizeUnit="Point" textOrientation="horizontal" textColor="128,17,25,255" blendMode="0" fontWeight="50" capitalization="0" fontItalic="0" useSubstitutions="0" previewBkgrdColor="255,255,255,255" namedStyle="Regular" allowHtml="0" isExpression="0" fontUnderline="0" fontSizeMapUnitScale="3x:0,0,0,0,0,0" fontStrikeout="0">
            <text-buffer bufferSize="0.9999999999999999" bufferColor="255,255,255,255" bufferNoFill="1" bufferJoinStyle="128" bufferSizeMapUnitScale="3x:0,0,0,0,0,0" bufferDraw="1" bufferOpacity="0.5" bufferSizeUnits="MM" bufferBlendMode="0"/>
            <text-mask maskSizeUnits="MM" maskEnabled="0" maskedSymbolLayers="" maskJoinStyle="128" maskOpacity="1" maskType="0" maskSize="1.5" maskSizeMapUnitScale="3x:0,0,0,0,0,0"/>
            <background shapeSizeY="0" shapeSizeUnit="MM" shapeSizeMapUnitScale="3x:0,0,0,0,0,0" shapeOffsetMapUnitScale="3x:0,0,0,0,0,0" shapeSVGFile="" shapeBorderWidth="0" shapeRadiiY="0" shapeBorderWidthUnit="MM" shapeBorderColor="128,128,128,255" shapeRadiiUnit="MM" shapeOffsetY="0" shapeRotationType="0" shapeRotation="0" shapeJoinStyle="64" shapeBlendMode="0" shapeOpacity="1" shapeType="0" shapeFillColor="255,255,255,255" shapeSizeType="0" shapeRadiiMapUnitScale="3x:0,0,0,0,0,0" shapeRadiiX="0" shapeDraw="0" shapeOffsetUnit="MM" shapeSizeX="0" shapeOffsetX="0" shapeBorderWidthMapUnitScale="3x:0,0,0,0,0,0">
              <symbol alpha="1" type="marker" name="markerSymbol" force_rhr="0" clip_to_extent="1">
                <layer enabled="1" pass="0" locked="0" class="SimpleMarker">
                  <prop v="0" k="angle"/>
                  <prop v="243,166,178,255" k="color"/>
                  <prop v="1" k="horizontal_anchor_point"/>
                  <prop v="bevel" k="joinstyle"/>
                  <prop v="circle" k="name"/>
                  <prop v="0,0" k="offset"/>
                  <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
                  <prop v="MM" k="offset_unit"/>
                  <prop v="35,35,35,255" k="outline_color"/>
                  <prop v="solid" k="outline_style"/>
                  <prop v="0" k="outline_width"/>
                  <prop v="3x:0,0,0,0,0,0" k="outline_width_map_unit_scale"/>
                  <prop v="MM" k="outline_width_unit"/>
                  <prop v="diameter" k="scale_method"/>
                  <prop v="2" k="size"/>
                  <prop v="3x:0,0,0,0,0,0" k="size_map_unit_scale"/>
                  <prop v="MM" k="size_unit"/>
                  <prop v="1" k="vertical_anchor_point"/>
                  <data_defined_properties>
                    <Option type="Map">
                      <Option type="QString" name="name" value=""/>
                      <Option name="properties"/>
                      <Option type="QString" name="type" value="collection"/>
                    </Option>
                  </data_defined_properties>
                </layer>
              </symbol>
            </background>
            <shadow shadowDraw="0" shadowRadiusMapUnitScale="3x:0,0,0,0,0,0" shadowOffsetAngle="135" shadowRadius="1.5" shadowOffsetUnit="MM" shadowRadiusAlphaOnly="0" shadowUnder="0" shadowColor="0,0,0,255" shadowOffsetGlobal="1" shadowRadiusUnit="MM" shadowOffsetMapUnitScale="3x:0,0,0,0,0,0" shadowScale="100" shadowOffsetDist="1" shadowBlendMode="6" shadowOpacity="0.7"/>
            <dd_properties>
              <Option type="Map">
                <Option type="QString" name="name" value=""/>
                <Option name="properties"/>
                <Option type="QString" name="type" value="collection"/>
              </Option>
            </dd_properties>
            <substitutions/>
          </text-style>
          <text-format wrapChar="" addDirectionSymbol="0" leftDirectionSymbol="&lt;" reverseDirectionSymbol="0" rightDirectionSymbol=">" decimals="3" plussign="0" formatNumbers="0" autoWrapLength="0" multilineAlign="3" useMaxLineLengthForAutoWrap="1" placeDirectionSymbol="0"/>
          <placement yOffset="1" distUnits="MM" repeatDistanceMapUnitScale="3x:0,0,0,0,0,0" placementFlags="10" maxCurvedCharAngleOut="-25" labelOffsetMapUnitScale="3x:0,0,0,0,0,0" preserveRotation="1" geometryGenerator="" offsetUnits="MM" overrunDistanceUnit="MM" overrunDistanceMapUnitScale="3x:0,0,0,0,0,0" geometryGeneratorType="PointGeometry" polygonPlacementFlags="2" distMapUnitScale="3x:0,0,0,0,0,0" layerType="PointGeometry" predefinedPositionOrder="TR,TL,BR,BL,R,L,TSR,BSR" rotationAngle="0" dist="0" repeatDistanceUnits="MM" xOffset="0" offsetType="0" quadOffset="7" lineAnchorType="0" placement="1" geometryGeneratorEnabled="0" maxCurvedCharAngleIn="25" priority="5" centroidWhole="0" fitInPolygonOnly="0" repeatDistance="0" overrunDistance="0" lineAnchorPercent="0.5" centroidInside="0"/>
          <rendering scaleVisibility="0" minFeatureSize="0" fontMaxPixelSize="10000" upsidedownLabels="0" obstacleType="1" obstacleFactor="1" labelPerPart="0" obstacle="1" maxNumLabels="2000" fontMinPixelSize="3" mergeLines="0" drawLabels="1" scaleMax="0" fontLimitPixelSize="0" scaleMin="0" limitNumLabels="0" displayAll="0" zIndex="0"/>
          <dd_properties>
            <Option type="Map">
              <Option type="QString" name="name" value=""/>
              <Option name="properties"/>
              <Option type="QString" name="type" value="collection"/>
            </Option>
          </dd_properties>
          <callout type="simple">
            <Option type="Map">
              <Option type="QString" name="anchorPoint" value="pole_of_inaccessibility"/>
              <Option type="Map" name="ddProperties">
                <Option type="QString" name="name" value=""/>
                <Option name="properties"/>
                <Option type="QString" name="type" value="collection"/>
              </Option>
              <Option type="bool" name="drawToAllParts" value="false"/>
              <Option type="QString" name="enabled" value="0"/>
              <Option type="QString" name="labelAnchorPoint" value="point_on_exterior"/>
              <Option type="QString" name="lineSymbol" value="&lt;symbol alpha=&quot;1&quot; type=&quot;line&quot; name=&quot;symbol&quot; force_rhr=&quot;0&quot; clip_to_extent=&quot;1&quot;>&lt;layer enabled=&quot;1&quot; pass=&quot;0&quot; locked=&quot;0&quot; class=&quot;SimpleLine&quot;>&lt;prop v=&quot;0&quot; k=&quot;align_dash_pattern&quot;/>&lt;prop v=&quot;square&quot; k=&quot;capstyle&quot;/>&lt;prop v=&quot;5;2&quot; k=&quot;customdash&quot;/>&lt;prop v=&quot;3x:0,0,0,0,0,0&quot; k=&quot;customdash_map_unit_scale&quot;/>&lt;prop v=&quot;MM&quot; k=&quot;customdash_unit&quot;/>&lt;prop v=&quot;0&quot; k=&quot;dash_pattern_offset&quot;/>&lt;prop v=&quot;3x:0,0,0,0,0,0&quot; k=&quot;dash_pattern_offset_map_unit_scale&quot;/>&lt;prop v=&quot;MM&quot; k=&quot;dash_pattern_offset_unit&quot;/>&lt;prop v=&quot;0&quot; k=&quot;draw_inside_polygon&quot;/>&lt;prop v=&quot;bevel&quot; k=&quot;joinstyle&quot;/>&lt;prop v=&quot;60,60,60,255&quot; k=&quot;line_color&quot;/>&lt;prop v=&quot;solid&quot; k=&quot;line_style&quot;/>&lt;prop v=&quot;0.3&quot; k=&quot;line_width&quot;/>&lt;prop v=&quot;MM&quot; k=&quot;line_width_unit&quot;/>&lt;prop v=&quot;0&quot; k=&quot;offset&quot;/>&lt;prop v=&quot;3x:0,0,0,0,0,0&quot; k=&quot;offset_map_unit_scale&quot;/>&lt;prop v=&quot;MM&quot; k=&quot;offset_unit&quot;/>&lt;prop v=&quot;0&quot; k=&quot;ring_filter&quot;/>&lt;prop v=&quot;0&quot; k=&quot;tweak_dash_pattern_on_corners&quot;/>&lt;prop v=&quot;0&quot; k=&quot;use_custom_dash&quot;/>&lt;prop v=&quot;3x:0,0,0,0,0,0&quot; k=&quot;width_map_unit_scale&quot;/>&lt;data_defined_properties>&lt;Option type=&quot;Map&quot;>&lt;Option type=&quot;QString&quot; name=&quot;name&quot; value=&quot;&quot;/>&lt;Option name=&quot;properties&quot;/>&lt;Option type=&quot;QString&quot; name=&quot;type&quot; value=&quot;collection&quot;/>&lt;/Option>&lt;/data_defined_properties>&lt;/layer>&lt;/symbol>"/>
              <Option type="double" name="minLength" value="0"/>
              <Option type="QString" name="minLengthMapUnitScale" value="3x:0,0,0,0,0,0"/>
              <Option type="QString" name="minLengthUnit" value="MM"/>
              <Option type="double" name="offsetFromAnchor" value="0"/>
              <Option type="QString" name="offsetFromAnchorMapUnitScale" value="3x:0,0,0,0,0,0"/>
              <Option type="QString" name="offsetFromAnchorUnit" value="MM"/>
              <Option type="double" name="offsetFromLabel" value="0"/>
              <Option type="QString" name="offsetFromLabelMapUnitScale" value="3x:0,0,0,0,0,0"/>
              <Option type="QString" name="offsetFromLabelUnit" value="MM"/>
            </Option>
          </callout>
        </settings>
      </rule>
    </rules>
  </labeling>
  <customproperties>
    <property key="dualview/previewExpressions" value="&quot;id&quot;"/>
  </customproperties>
  <blendMode>0</blendMode>
  <featureBlendMode>0</featureBlendMode>
  <layerOpacity>1</layerOpacity>
  <geometryOptions removeDuplicateNodes="0" geometryPrecision="0">
    <activeChecks type="StringList">
      <Option type="QString" value=""/>
    </activeChecks>
    <checkConfiguration/>
  </geometryOptions>
  <legend type="default-vector"/>
  <referencedLayers/>
  <fieldConfiguration>
    <field configurationFlags="None" name="id">
      <editWidget type="">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="z">
      <editWidget type="">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="oldz">
      <editWidget type="">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="adj">
      <editWidget type="">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
  </fieldConfiguration>
  <aliases>
    <alias index="0" name="" field="id"/>
    <alias index="1" name="" field="z"/>
    <alias index="2" name="" field="oldz"/>
    <alias index="3" name="" field="adj"/>
  </aliases>
  <defaults>
    <default expression="" applyOnUpdate="0" field="id"/>
    <default expression="" applyOnUpdate="0" field="z"/>
    <default expression="" applyOnUpdate="0" field="oldz"/>
    <default expression="" applyOnUpdate="0" field="adj"/>
  </defaults>
  <constraints>
    <constraint notnull_strength="1" exp_strength="0" constraints="3" unique_strength="1" field="id"/>
    <constraint notnull_strength="0" exp_strength="0" constraints="0" unique_strength="0" field="z"/>
    <constraint notnull_strength="0" exp_strength="0" constraints="0" unique_strength="0" field="oldz"/>
    <constraint notnull_strength="0" exp_strength="0" constraints="0" unique_strength="0" field="adj"/>
  </constraints>
  <constraintExpressions>
    <constraint desc="" exp="" field="id"/>
    <constraint desc="" exp="" field="z"/>
    <constraint desc="" exp="" field="oldz"/>
    <constraint desc="" exp="" field="adj"/>
  </constraintExpressions>
  <expressionfields/>
  <attributeactions>
    <defaultAction key="Canvas" value="{00000000-0000-0000-0000-000000000000}"/>
  </attributeactions>
  <attributetableconfig sortOrder="0" actionWidgetStyle="dropDown" sortExpression="&quot;id&quot;">
    <columns>
      <column width="-1" type="field" name="id" hidden="0"/>
      <column width="-1" type="field" name="z" hidden="0"/>
      <column width="-1" type="actions" hidden="1"/>
      <column width="-1" type="field" name="oldz" hidden="0"/>
      <column width="-1" type="field" name="adj" hidden="0"/>
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
  <previewExpression>"id"</previewExpression>
  <mapTip></mapTip>
  <layerGeometryType>0</layerGeometryType>
</qgis>

import processing 
import os 
#   PASTE THE LOCATION OF THE WORKING DIRECTORY HERE !!!!
dir = r"C:\Users\g.husband\Desktop\pygis"

layer = iface.activeLayer()
print(layer.name())
# split layer by attribute 
layer.selectByExpression('"portee"= \'G\'')
# save selection 
#fn = r'C:\Users\g.husband\sanef_pygis\cote_g.shp'
fn = os.path.join(dir, "sides", f"{layer.name()}_coteG.shp")
print(fn)
writer = QgsVectorFileWriter.writeAsVectorFormat(layer, fn, 'utf-8', driverName='ESRI Shapefile', onlySelected=True)
del(writer)
fn = os.path.join(dir, "sides", f"{layer.name()}_coteD.shp")

#fn = r'C:\Users\g.husband\sanef_pygis\cote_d.shp'
layer.selectByExpression('"portee"= \'D\'')
writer = QgsVectorFileWriter.writeAsVectorFormat(layer, fn, 'utf-8', driverName='ESRI Shapefile', onlySelected=True)
del(writer)

# dissolve cote_d and cote_g
#infn = r'C:\Users\g.husband\sanef_pygis\cote_g.shp'
infn = os.path.join(dir, "sides", f"{layer.name()}_coteG.shp")
outfn = os.path.join(dir, "sides", f"{layer.name()}_dissG.shp")
#outfn = r'C:\Users\g.husband\sanef_pygis\diss_g.shp'
processing.run("native:dissolve", {'INPUT':infn, 'OUTPUT':outfn})
# add modified vector to layer
selected_layer = iface.addVectorLayer(outfn, '', 'ogr')


#infn = r'C:\Users\g.husband\sanef_pygis\cote_d.shp'
#outfn = r'C:\Users\g.husband\sanef_pygis\diss_d.shp'

infn = os.path.join(dir, "sides", f"{layer.name()}_coteD.shp")
outfn = os.path.join(dir, "sides", f"{layer.name()}_dissD.shp")
processing.run("native:dissolve", {'INPUT':infn, 'OUTPUT':outfn})
# add modified shapefiles to canvas
selected_layer = iface.addVectorLayer(outfn, '', 'ogr')# select wanted layer


#========================QCHAINAGE================================
#infn = r'C:\Users\g.husband\sanef_pygis\diss_d.shp'
infn = os.path.join(dir, "sides", f"{layer.name()}_dissD.shp")
outfn = os.path.join(dir, "sides", f"{layer.name()}_dotsD.shp")
#outfn = r'C:\Users\g.husband\sanef_pygis\dots.shp'

#layer = iface.activeLayer()
processing.run("native:pointsalonglines", {'INPUT': infn,
'DISTANCE': 40,
'OUTPUT': outfn })

# creating points from path 
infn = os.path.join(dir, "sides", f"{layer.name()}_dotsD.shp")
#infn = r'C:\Users\g.husband\sanef_pygis\dots.shp'
outfn = os.path.join(dir, "sides", f"{layer.name()}_pathD.shp")
#outfn = r'C:\Users\g.husband\sanef_pygis\path.shp'
processing.run("qgis:pointstopath", {'INPUT': infn,
'ORDER_FIELD': 'distance',
'OUTPUT': outfn })

# explode lines 
#infn = r'C:\Users\g.husband\sanef_pygis\path.shp'
infn = os.path.join(dir, "sides", f"{layer.name()}_pathD.shp")
outfn = os.path.join(dir, "sides", f"{layer.name()}_exploded.shp")
#outfn = r'C:\Users\g.husband\sanef_pygis\exploded.shp'
processing.run("native:explodelines", {'INPUT': infn,
'OUTPUT': outfn})  
#selected_layer = iface.addVectorLayer(outfn, '', 'ogr')

# rotate exploded
#infn = r'C:\Users\g.husband\sanef_pygis\exploded.shp'
infn = os.path.join(dir, "sides", f"{layer.name()}_exploded.shp")
outfn = os.path.join(dir, "sides", f"{layer.name()}_rotated.shp")
#outfn = r'C:\Users\g.husband\sanef_pygis\rotated.shp'
processing.run("native:rotatefeatures", {'INPUT': infn,
'ANGLE': 90,
'OUTPUT': outfn})
selected_layer = iface.addVectorLayer(outfn, '', 'ogr')

# =================EXTEND LINES==========================================
# extend rotated lines 
#infn = r'C:\Users\g.husband\sanef_pygis\rotated.shp'
infn = os.path.join(dir, "sides", f"{layer.name()}_rotated.shp")
outfn = os.path.join(dir, "sides", f"{layer.name()}_extended.shp")
#outfn = r'C:\Users\g.husband\sanef_pygis\extended.shp'
processing.run("native:extendlines", {'INPUT': infn,
'ANGLE': 90,
'START_DISTANCE': 500,
'END_DISTANCE': 500, 
'OUTPUT': outfn})
selected_layer = iface.addVectorLayer(outfn, '', 'ogr')

#=================LINE INTERSECTIONS=======================================

# intersection d
over = os.path.join(dir, "sides", f"{layer.name()}_extended.shp")
infn = os.path.join(dir, "sides", f"{layer.name()}_dissD.shp")
outfn = os.path.join(dir, "sides", f"{layer.name()}_intersectD.shp")
processing.run("native:lineintersections", {'INPUT': over,
'INTERSECT': infn,
'OUTPUT': outfn})
selected_layer = iface.addVectorLayer(outfn, '', 'ogr')


over = os.path.join(dir, "sides", f"{layer.name()}_extended.shp")
infn = os.path.join(dir, "sides", f"{layer.name()}_dissG.shp")
outfn = os.path.join(dir, "sides", f"{layer.name()}_intersectG.shp")
processing.run("native:lineintersections", {'INPUT': over,
'INTERSECT': infn,
'OUTPUT': outfn})
selected_layer = iface.addVectorLayer(outfn, '', 'ogr')
# make sure they have the same feature count

# ======================Adding index field================================
infn = os.path.join(dir, "sides", f"{layer.name()}_intersectD.shp")    # intersect D
outfn = os.path.join(dir, "sides", f"{layer.name()}_incr_intersectD.shp")   # incr_intersectD
processing.run("native:addautoincrementalfield", {'INPUT': infn,
'FIELD_NAME': "AUTO", 
'OUTPUT': outfn})
selected_layer = iface.addVectorLayer(outfn, '', 'ogr')
# add index to points 2
infn = os.path.join(dir, "sides", f"{layer.name()}_intersectG.shp")
outfn = os.path.join(dir, "sides", f"{layer.name()}_incr_intersectG.shp")

processing.run("native:addautoincrementalfield", {'INPUT': infn,
'FIELD_NAME': "AUTO", 
'OUTPUT': outfn})
selected_layer = iface.addVectorLayer(outfn, '', 'ogr')


#========================Adding xy fields========================================

infn = os.path.join(dir, "sides", f"{layer.name()}_incr_intersectD.shp")
outfn = os.path.join(dir, "sides", f"{layer.name()}_incr_xy_intersectD.shp")
processing.run("native:addxyfields", {'INPUT': infn,
'CRS': 'ProjectCrs', 
'OUTPUT': outfn})
selected_layer = iface.addVectorLayer(outfn, '', 'ogr')

# add x y field to points g
infn = os.path.join(dir, "sides", f"{layer.name()}_incr_intersectG.shp")
outfn = os.path.join(dir, "sides", f"{layer.name()}_incr_xy_intersectG.shp")    # defining output destination 
processing.run("native:addxyfields", {'INPUT': infn,
'CRS': 'ProjectCrs', 
'OUTPUT': outfn})
selected_layer = iface.addVectorLayer(outfn, '', 'ogr')

#=============================[JOIN]====================================
print(layer.name()) # it works up to here 
# join incr_xy_intersect_g with incr_xy_intersect_d on index

ing = os.path.join(dir, "sides", f"{layer.name()}_incr_xy_intersectG.shp") # first geometry to join 
ind = os.path.join(dir, "sides", f"{layer.name()}_incr_xy_intersectD.shp")  # second geometry to join 
outfn = os.path.join(dir, "sides", f"{layer.name()}_join.shp") # result of the join 
#-----------------------------------------------Joining attribute tables------------------------------------------------------

processing.run("native:joinattributestable", {'INPUT': ing, # ing goes here
'FIELD': 'AUTO',    # merger on auto increment field 
'INPUT_2':ind,  # ind goes here
'FIELD_2':'AUTO',   # merger on autoincrement field 
'CRS': 'ProjectCrs',    # uses projet coordinate system 
'OUTPUT': outfn})   # output set as outfn 
print("merging of the layers done ")

layer = iface.addVectorLayer(outfn, '', 'ogr')# creating a vector layer with a joined output field 
# calculate fields
pv = layer.dataProvider()   # not sure just add it 
##=====================Adding missing fields)========================================
pv.addAttributes([
QgsField('len_test_m', QVariant.Double), 
QgsField('mx1', QVariant.Double), # 
QgsField('mx2', QVariant.Double), 
QgsField('my1', QVariant.Double), 
QgsField('my2', QVariant.Double) # 
])

layer.updateFields() # update the attribute table 
expression1 = QgsExpression('abs(sqrt(("x"-"x_2")^2+("y"-"y_2")^2))')   # expression to calculate distance 
mx1 = QgsExpression('if ("len_test_m"<50, ("x_2"+"x")/2, "x")')
mx2 = QgsExpression('if ("len_test_m"<50, ("x_2"+"x")/2, "x_2")')

my1 = QgsExpression('if ("len_test_m"<50, ("y_2"+"y")/2, "y")')
my2 = QgsExpression('if ("len_test_m"<50, ("y_2"+"y")/2, "y_2")')
#if("len_test_m"<50, ("x"+"x_2")/2, "x"
# adding context 
context = QgsExpressionContext()
context.appendScopes(QgsExpressionContextUtils.globalProjectLayerScopes(layer))
# applying expressions 
# 1) calculate distance between both sides 
with edit(layer):
    for f in layer.getFeatures():
        context.setFeature(f)
        f['len_test_m'] = expression1.evaluate(context)
        layer.updateFeature(f)
# 2) calculate mx1
with edit(layer):
    for f in layer.getFeatures():
        context.setFeature(f)
        f['mx1'] = mx1.evaluate(context)
        f['mx2'] = mx2.evaluate(context)
        f['my1'] = my1.evaluate(context)
        f['my2'] = my2.evaluate(context)
        layer.updateFeature(f)
# save shapefile to csv 
#outfn = r'C:\Users\g.husband\sanef_pygis\join.csv'
outfn = os.path.join(dir, "sides", f"{layer.name()}join.csv")
QgsVectorFileWriter.writeAsVectorFormat(layer,
outfn,
"utf-8",driverName = "CSV" , layerOptions = ['GEOMETRY=AS_XYZ'])



#=======================Calculate fields===============================

print (os.path.join(dir, "sides", f"{layer.name()}join.csv"))
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!Upgrade uri path to be relative!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
layer_name = layer.name()
uri =  f"file:///C:/Users/g.husband/Desktop/pygis/sides/{layer_name}join.csv?encoding=%s&delimiter=%s&xField=%s&yField=%s&crs=%s" % ("UTF-8",",", "mx1", "my1","epsg:2154")
#Make a vector layer
eq_layer=QgsVectorLayer(uri,"delete_me_1","delimitedtext")
#Check if layer is valid
if not eq_layer.isValid():
    print ("Layer not loaded")
#Add CSV data
layer = QgsProject.instance().addMapLayer(eq_layer)
#outfn = r'C:\Users\g.husband\sanef_pygis\right.shp'
outfn = os.path.join(dir, "sides", f"{layer_name}_right.shp")
layer.selectAll()
processing.run("native:saveselectedfeatures", {'INPUT':layer,'OUTPUT':outfn})

# do the same for the other side 
uri =  f"file:///C:/Users/g.husband/Desktop/pygis/sides/{layer_name}join.csv?encoding=%s&delimiter=%s&xField=%s&yField=%s&crs=%s" % ("UTF-8",",", "mx2", "my2","epsg:2154")
#Make a vector layer
eq_layer=QgsVectorLayer(uri,"delete_me_2","delimitedtext")
#Check if layer is valid
if not eq_layer.isValid():
    print ("Layer not loaded")
#Add CSV data
layer = QgsProject.instance().addMapLayer(eq_layer)
layer.selectAll()
outfn = os.path.join(dir, "sides", f"{layer_name}_left.shp")
processing.run("native:saveselectedfeatures", {'INPUT':layer,'OUTPUT':outfn})
selected_layer = iface.addVectorLayer(outfn, '', 'ogr')


outfn = os.path.join(dir, "sides", f"{layer_name}_left.shp")
# points rp path side 1
#infn = r'C:\Users\g.husband\sanef_pygis\right.shp'
#outfn = r'C:\Users\g.husband\sanef_pygis\path_right.shp'
infn = os.path.join(dir, "sides", f"{layer_name}_right.shp")
outfn = os.path.join(dir, "sides", f"{layer_name}_path_right.shp")
processing.run("qgis:pointstopath", {'INPUT': infn,
'ORDER_FIELD': 'AUTO',
'OUTPUT': outfn })
selected_layer = iface.addVectorLayer(outfn, '', 'ogr')
# points to path side 2
infn = os.path.join(dir, "sides", f"{layer_name}_left.shp")
outfn = os.path.join(dir, "sides", f"{layer_name}_path_left.shp")
processing.run("qgis:pointstopath", {'INPUT': infn,
'ORDER_FIELD': 'AUTO',
'OUTPUT': outfn })
selected_layer = iface.addVectorLayer(outfn, '', 'ogr')


# ================================== Merge ==================================

# merge layers 
in1 = r'C:\Users\g.husband\sanef_pygis\path_left.shp'
in2 = r'C:\Users\g.husband\sanef_pygis\path_right.shp'
# the name of the file can be chose here
outfn = r'C:\Users\g.husband\sanef_pygis\final_result.shp'
processing.run("native:mergevectorlayers", {'LAYERS': [in1,
in2],
'OUTPUT': outfn })
selected_layer = iface.addVectorLayer(outfn, '', 'ogr')






# join incr_xy_intersect_g with incr_xy_intersect_d on index
ing = r'C:\Users\g.husband\Desktop\pygis\sides\A40_incr_xy_intersectG.shp'
ind = r'C:\Users\g.husband\Desktop\pygis\sides\A40_incr_xy_intersectD.shp'
outfn = r'C:\Users\g.husband\Desktop\pygis\sides\join.shp'
processing.run("native:joinattributestable", {'INPUT': ing,
'FIELD': 'AUTO',
'INPUT_2':ind,
'FIELD_2':'AUTO',
'CRS': 'ProjectCrs', 
'OUTPUT': outfn})
layer = iface.addVectorLayer(outfn, '', 'ogr')
# calculate fields
pv = layer.dataProvider()
pv.addAttributes([QgsField('len_test_m', QVariant.Double), QgsField('mx1', QVariant.Double),
QgsField('mx2', QVariant.Double), QgsField('my1', QVariant.Double), QgsField('my2', QVariant.Double)
])
layer.updateFields()
expression1 = QgsExpression('abs(sqrt(("x"-"x_2")^2+("y"-"y_2")^2))')
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
outfn = r'C:\Users\g.husband\sanef_pygis\join.csv'
QgsVectorFileWriter.writeAsVectorFormat(layer,
outfn,
"utf-8",driverName = "CSV" , layerOptions = ['GEOMETRY=AS_XYZ'])





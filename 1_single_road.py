import processing 

layer = iface.activeLayer()
print(layer.name())
# split layer by attribute 
layer.selectByExpression('"portee"= \'G\'')
# save selection 
fn = r'C:\Users\g.husband\sanef_pygis\cote_g.shp'
writer = QgsVectorFileWriter.writeAsVectorFormat(layer, fn, 'utf-8', driverName='ESRI Shapefile', onlySelected=True)
del(writer)

fn = r'C:\Users\g.husband\sanef_pygis\cote_d.shp'
layer.selectByExpression('"portee"= \'D\'')
writer = QgsVectorFileWriter.writeAsVectorFormat(layer, fn, 'utf-8', driverName='ESRI Shapefile', onlySelected=True)
del(writer)

# dissolve cote_d and cote_g
infn = r'C:\Users\g.husband\sanef_pygis\cote_g.shp'
outfn = r'C:\Users\g.husband\sanef_pygis\diss_g.shp'
processing.run("native:dissolve", {'INPUT':infn, 'OUTPUT':outfn})
# add modified vector to layer
selected_layer = iface.addVectorLayer(outfn, '', 'ogr')
infn = r'C:\Users\g.husband\sanef_pygis\cote_d.shp'
outfn = r'C:\Users\g.husband\sanef_pygis\diss_d.shp'
processing.run("native:dissolve", {'INPUT':infn, 'OUTPUT':outfn})
# add modified shapefiles to canvas
selected_layer = iface.addVectorLayer(outfn, '', 'ogr')# select wanted layer










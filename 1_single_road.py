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










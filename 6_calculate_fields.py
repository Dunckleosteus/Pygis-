uri = "file:///C:/Users/g.husband/sanef_pygis/join.csv?encoding=%s&delimiter=%s&xField=%s&yField=%s&crs=%s" % ("UTF-8",",", "mx1", "my1","epsg:2154")
#Make a vector layer
eq_layer=QgsVectorLayer(uri,"delete_me_1","delimitedtext")
#Check if layer is valid
if not eq_layer.isValid():
    print ("Layer not loaded")
#Add CSV data
layer = QgsProject.instance().addMapLayer(eq_layer)
outfn = r'C:\Users\g.husband\sanef_pygis\right.shp'
layer.selectAll()
processing.run("native:saveselectedfeatures", {'INPUT':layer,'OUTPUT':outfn})

# do the same for the other side 
uri = "file:///C:/Users/g.husband/sanef_pygis/join.csv?encoding=%s&delimiter=%s&xField=%s&yField=%s&crs=%s" % ("UTF-8",",", "mx2", "my2","epsg:2154")
#Make a vector layer
eq_layer=QgsVectorLayer(uri,"delete_me_2","delimitedtext")
#Check if layer is valid
if not eq_layer.isValid():
    print ("Layer not loaded")
#Add CSV data
layer = QgsProject.instance().addMapLayer(eq_layer)
outfn = r'C:\Users\g.husband\sanef_pygis\left.shp'
layer.selectAll()
processing.run("native:saveselectedfeatures", {'INPUT':layer,'OUTPUT':outfn})
#selected_layer = iface.addVectorLayer(outfn, '', 'ogr')

# points rp path side 1
infn = r'C:\Users\g.husband\sanef_pygis\right.shp'
outfn = r'C:\Users\g.husband\sanef_pygis\path_right.shp'
processing.run("qgis:pointstopath", {'INPUT': infn,
'ORDER_FIELD': 'AUTO',
'OUTPUT': outfn })
#selected_layer = iface.addVectorLayer(outfn, '', 'ogr')
# points to path side 2
infn = r'C:\Users\g.husband\sanef_pygis\left.shp'
outfn = r'C:\Users\g.husband\sanef_pygis\path_left.shp'
processing.run("qgis:pointstopath", {'INPUT': infn,
'ORDER_FIELD': 'AUTO',
'OUTPUT': outfn })
#selected_layer = iface.addVectorLayer(outfn, '', 'ogr')



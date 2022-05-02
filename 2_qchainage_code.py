# selects diss_d 
# creating points from path 
# explode lines 
# rotate exploded

# select diss_d and press run on the script
infn = r'C:\Users\g.husband\sanef_pygis\diss_d.shp'
outfn = r'C:\Users\g.husband\sanef_pygis\dots.shp'
layer = iface.activeLayer()
processing.run("native:pointsalonglines", {'INPUT': infn,
'DISTANCE': 40,
'OUTPUT': outfn })

# creating points from path 
infn = r'C:\Users\g.husband\sanef_pygis\dots.shp'
outfn = r'C:\Users\g.husband\sanef_pygis\path.shp'
processing.run("qgis:pointstopath", {'INPUT': infn,
'ORDER_FIELD': 'distance',
'OUTPUT': outfn })

# explode lines 
infn = r'C:\Users\g.husband\sanef_pygis\path.shp'
outfn = r'C:\Users\g.husband\sanef_pygis\exploded.shp'
processing.run("native:explodelines", {'INPUT': infn,
'OUTPUT': outfn})  
#selected_layer = iface.addVectorLayer(outfn, '', 'ogr')

# rotate exploded
infn = r'C:\Users\g.husband\sanef_pygis\exploded.shp'
outfn = r'C:\Users\g.husband\sanef_pygis\rotated.shp'
processing.run("native:rotatefeatures", {'INPUT': infn,
'ANGLE': 90,
'OUTPUT': outfn})
selected_layer = iface.addVectorLayer(outfn, '', 'ogr')












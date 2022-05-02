# extend rotated lines 
infn = r'C:\Users\g.husband\sanef_pygis\rotated.shp'
outfn = r'C:\Users\g.husband\sanef_pygis\extended.shp'
processing.run("native:extendlines", {'INPUT': infn,
'ANGLE': 90,
'START_DISTANCE': 500,
'END_DISTANCE': 500, 
'OUTPUT': outfn})
selected_layer = iface.addVectorLayer(outfn, '', 'ogr')

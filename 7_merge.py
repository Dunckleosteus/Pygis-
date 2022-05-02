# merge layers 
in1 = r'C:\Users\g.husband\sanef_pygis\path_left.shp'
in2 = r'C:\Users\g.husband\sanef_pygis\path_right.shp'
# the name of the file can be chose here
outfn = r'C:\Users\g.husband\sanef_pygis\final_result.shp'
processing.run("native:mergevectorlayers", {'LAYERS': [in1,
in2],
'OUTPUT': outfn })
selected_layer = iface.addVectorLayer(outfn, '', 'ogr')
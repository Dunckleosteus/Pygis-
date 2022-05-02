# intersection d
over = r'C:\Users\g.husband\sanef_pygis\extended.shp'
infn = r'C:\Users\g.husband\sanef_pygis\diss_d.shp'
outfn = r'C:\Users\g.husband\sanef_pygis\intersect_d.shp'
processing.run("native:lineintersections", {'INPUT': over,
'INTERSECT': infn,
'OUTPUT': outfn})
#selected_layer = iface.addVectorLayer(outfn, '', 'ogr')
# intersection 
over = r'C:\Users\g.husband\sanef_pygis\extended.shp'
infn = r'C:\Users\g.husband\sanef_pygis\diss_g.shp'
outfn = r'C:\Users\g.husband\sanef_pygis\intersect_g.shp'
processing.run("native:lineintersections", {'INPUT': over,
'INTERSECT': infn,
'OUTPUT': outfn})
#selected_layer = iface.addVectorLayer(outfn, '', 'ogr')
# make sure they have the same feature count

# add index to layer to points 1
infn = r'C:\Users\g.husband\sanef_pygis\intersect_d.shp'
outfn = r'C:\Users\g.husband\sanef_pygis\incr_intersect_d.shp'
processing.run("native:addautoincrementalfield", {'INPUT': infn,
'OUTPUT': outfn})
#selected_layer = iface.addVectorLayer(outfn, '', 'ogr')
# add index to points 2
infn = r'C:\Users\g.husband\sanef_pygis\intersect_g.shp'
outfn = r'C:\Users\g.husband\sanef_pygis\incr_intersect_g.shp'
processing.run("native:addautoincrementalfield", {'INPUT': infn,
'OUTPUT': outfn})
#selected_layer = iface.addVectorLayer(outfn, '', 'ogr')
# add x y field to points d
infn = r'C:\Users\g.husband\sanef_pygis\incr_intersect_d.shp'
outfn = r'C:\Users\g.husband\sanef_pygis\incr_xy_intersect_d.shp'
processing.run("native:addxyfields", {'INPUT': infn,
'CRS': 'ProjectCrs', 
'OUTPUT': outfn})
selected_layer = iface.addVectorLayer(outfn, '', 'ogr')
# add x y field to points g
infn = r'C:\Users\g.husband\sanef_pygis\incr_intersect_g.shp'
outfn = r'C:\Users\g.husband\sanef_pygis\incr_xy_intersect_g.shp'
processing.run("native:addxyfields", {'INPUT': infn,
'CRS': 'ProjectCrs', 
'OUTPUT': outfn})
selected_layer = iface.addVectorLayer(outfn, '', 'ogr')



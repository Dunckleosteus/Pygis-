import processing 
import os 
from qchainage import chainagetool



# paste location of working directory here: 
dir = r"C:\Users\g.husband\Desktop\pygis"

# how many lines are there in excel ? 


infn = os.path.join(dir, "sides", f"{layer.name()}_coteD.shp")
outfn = os.path.join(dir, "sides", f"{layer.name()}_splitter.shp")

# select layer to use function on 
layer = iface.activeLayer()
chainagetool.points_along_line(layerout=outfn,
              startpoint=0,
              endpoint=0,
              distance=0,
              label="dc",
              layer=layer,
              selected_only=False,
              force=False,
              fo_fila=False,
              divide=500,
              decimal=2)

selected_layer = iface.addVectorLayer(outfn, '', 'ogr')
print(selected_layer.featureCount())

## creating points from path 
#infn = os.path.join(dir, "sides", f"{layer.name()}_dotsD.shp")
##infn = r'C:\Users\g.husband\sanef_pygis\dots.shp'
#outfn = os.path.join(dir, "sides", f"{layer.name()}_pathD.shp")
##outfn = r'C:\Users\g.husband\sanef_pygis\path.shp'
#processing.run("qgis:pointstopath", {'INPUT': infn,
#'ORDER_FIELD': 'distance',
#'OUTPUT': outfn })
#
## explode lines 
##infn = r'C:\Users\g.husband\sanef_pygis\path.shp'
#infn = os.path.join(dir, "sides", f"{layer.name()}_pathD.shp")
#outfn = os.path.join(dir, "sides", f"{layer.name()}_exploded.shp")
##outfn = r'C:\Users\g.husband\sanef_pygis\exploded.shp'
#processing.run("native:explodelines", {'INPUT': infn,
#'OUTPUT': outfn})  
##selected_layer = iface.addVectorLayer(outfn, '', 'ogr')
#
## rotate exploded
##infn = r'C:\Users\g.husband\sanef_pygis\exploded.shp'
#infn = os.path.join(dir, "sides", f"{layer.name()}_exploded.shp")
#outfn = os.path.join(dir, "sides", f"{layer.name()}_rotated.shp")
##outfn = r'C:\Users\g.husband\sanef_pygis\rotated.shp'
#processing.run("native:rotatefeatures", {'INPUT': infn,
#'ANGLE': 90,
#'OUTPUT': outfn})
#selected_layer = iface.addVectorLayer(outfn, '', 'ogr')
#
## =================EXTEND LINES==========================================
## extend rotated lines 
##infn = r'C:\Users\g.husband\sanef_pygis\rotated.shp'
#infn = os.path.join(dir, "sides", f"{layer.name()}_rotated.shp")
#outfn = os.path.join(dir, "sides", f"{layer.name()}_extended.shp")
##outfn = r'C:\Users\g.husband\sanef_pygis\extended.shp'
#processing.run("native:extendlines", {'INPUT': infn,
#'ANGLE': 90,
#'START_DISTANCE': 500,
#'END_DISTANCE': 500, 
#'OUTPUT': outfn})
#selected_layer = iface.addVectorLayer(outfn, '', 'ogr')
#
#
#layer = iface.activeLayer()
#processing.run("native:pointsalonglines", {'INPUT': infn,
#'DISTANCE': 40,
#'OUTPUT': outfn })
#
## creating points from path 
#infn = os.path.join(dir, "sides", f"{layer.name()}_dotsD.shp")
##infn = r'C:\Users\g.husband\sanef_pygis\dots.shp'
#outfn = os.path.join(dir, "sides", f"{layer.name()}_pathD.shp")
##outfn = r'C:\Users\g.husband\sanef_pygis\path.shp'
#processing.run("qgis:pointstopath", {'INPUT': infn,
#'ORDER_FIELD': 'distance',
#'OUTPUT': outfn })
#
## explode lines 
##infn = r'C:\Users\g.husband\sanef_pygis\path.shp'
#infn = os.path.join(dir, "sides", f"{layer.name()}_pathD.shp")
#outfn = os.path.join(dir, "sides", f"{layer.name()}_exploded.shp")
##outfn = r'C:\Users\g.husband\sanef_pygis\exploded.shp'
#processing.run("native:explodelines", {'INPUT': infn,
#'OUTPUT': outfn})  
##selected_layer = iface.addVectorLayer(outfn, '', 'ogr')
#
## rotate exploded
##infn = r'C:\Users\g.husband\sanef_pygis\exploded.shp'
#infn = os.path.join(dir, "sides", f"{layer.name()}_exploded.shp")
#outfn = os.path.join(dir, "sides", f"{layer.name()}_rotated.shp")
##outfn = r'C:\Users\g.husband\sanef_pygis\rotated.shp'
#processing.run("native:rotatefeatures", {'INPUT': infn,
#'ANGLE': 90,
#'OUTPUT': outfn})
#selected_layer = iface.addVectorLayer(outfn, '', 'ogr')
#
## =================EXTEND LINES==========================================
## extend rotated lines 
##infn = r'C:\Users\g.husband\sanef_pygis\rotated.shp'
#infn = os.path.join(dir, "sides", f"{layer.name()}_rotated.shp")
#outfn = os.path.join(dir, "sides", f"{layer.name()}_extended.shp")
##outfn = r'C:\Users\g.husband\sanef_pygis\extended.shp'
#processing.run("native:extendlines", {'INPUT': infn,
#'ANGLE': 90,
#'START_DISTANCE': 500,
#'END_DISTANCE': 500, 
#'OUTPUT': outfn})
#selected_layer = iface.addVectorLayer(outfn, '', 'ogr')

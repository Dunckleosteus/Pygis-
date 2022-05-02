import processing 
outfn=r'T:\Auscultation routiere\09 - STAGIAIRE APPRENTI\2021-08-30 au 24-08-30 - HUSBAND Georges - Uni LaSalle\3 - SANEF 2021\Qgis\pygis\converter\buffer.shp'

layer = iface.activeLayer()#select the layer with mouse 
raw_a= r'{}'.format(str(layer.name()))
print (raw_a)

# BUFFER 
processing.run("native:buffer", {'INPUT':layer,
'DISTANCE':30,
'END_CAP_STYLE':1,
'OUTPUT':outfn
})

# clip vector by mask 
outfn2 = r'C:\Users\g.husband\sanef_pygis\projector\files\CONV_{}.shp'.format(str(raw_a))
print (outfn2)
processing.run("gdal:clipvectorbypolygon",{'INPUT':'A13',
'MASK':outfn,
'OUTPUT':outfn2
}
)
selected_layer = iface.addVectorLayer(outfn2, '', 'ogr')
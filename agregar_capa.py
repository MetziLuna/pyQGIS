from qgis.core import QgsGeometry
layer = iface.addVectorLayer("/home/metzi/Datos/DATOS_SIG/munA_WGS_1984/munA_WGS_1984.shp","municipio","ogr")

#Para cada municipio se muesta en la consola su código y las coordenadas de su centroide

for feature in layer.getFeatures():
    geometry = feature.geometry()
    centroid = geometry.centroid().asPoint()    
    cod = feature.attribute("COD_MUN4")
    print (cod,centroid.x(),centroid.y())    

# -*- coding: cp1252 -*-
#"C:\Python27\ArcGISx6410.7\python.exe" "E:\\scripts-arcgis\\Puntos_Calientes\\puntos_calientes.py"
# IMPORTACION DE FUNCIONES

# Importacion del modulo webbrowser
# import webbrowser

import requests
# Importacion del modulo OS
import os
# Impotacion del modulo zipfile
import zipfile
# Importacion del modulo de ArcGIS
import arcpy
# Importacion del modulo time
import time

from string import Template


GDB_PATH = "E:\\scripts-arcgis\\sde\\puntos_calientes_197.sde"
#GDB_PATH = "E:\\scripts-arcgis\\sde\\puntos_calientes_214.sde"
puntos_calientes_sde_puntos_calientes_dia = GDB_PATH + "\\puntos_calientes.sde.puntos_calientes_dia"
puntos_calientes_sde_puntos_calientes_a_la_fecha = GDB_PATH + "\\puntos_calientes.sde.puntos_calientes_a_la_fecha"

CARPETA_BASE = "E:\\scripts-arcgis\\Puntos_Calientes\\Piloto_IF"

CARPETA_DESCARGAS = os.path.join(CARPETA_BASE, "Datos Descargados")
CARPETA_PC = os.path.join(CARPETA_BASE, 'Puntos_Calientes')
CARPETA_DPA = os.path.join(CARPETA_BASE, 'DPA')
CARPETA_PROCESO = os.path.join(CARPETA_BASE, 'Proceso')
CARPETA_RESULTADO = os.path.join(CARPETA_BASE, "Resultado")

zip_viirs = os.path.join(CARPETA_DESCARGAS, 'J1_VIIRS_C2_South_America_24h.zip')

Recorte_shp = os.path.join(CARPETA_PROCESO, "Recorte.shp")
Buffer_shp = os.path.join(CARPETA_PROCESO, "Buffer.shp")
Intersecar_shp = os.path.join(CARPETA_PROCESO, "Intersecar.shp")
Disolver_shp = os.path.join(CARPETA_PROCESO, "Disolver.shp")

IF_Chile_shp = os.path.join(CARPETA_RESULTADO, "IF_Chile.shp")

Recorte_Disolve_dia_shp = os.path.join(CARPETA_PC, "Recorte_Disolve_dia.shp")
Buffer_dia_shp = os.path.join(CARPETA_PROCESO, "Buffer_dia.shp")
Disolver_dia_shp = os.path.join(CARPETA_PROCESO, "Disolver_dia.shp")
Intersecar_dia_shp = os.path.join(CARPETA_PROCESO, "Intersecar_dia.shp")

J1_VIIRS_C2_South_America_24h_shp = os.path.join(CARPETA_DESCARGAS, "J1_VIIRS_C2_South_America_24h.shp")

dpa_shp = os.path.join(CARPETA_DPA, "dpa.shp")

PC_Proyec_shp = os.path.join(CARPETA_PC, "PC_Proyec.shp")
PC_Chile_shp = os.path.join(CARPETA_PC, "PC_Chile.shp")
PC_Proyec = os.path.join(CARPETA_PC, "PC_Proyec")
PuntosC_Chile_shp = os.path.join(CARPETA_PC, "PuntosC_Chile.shp")

IF_Chile_Acum_shp = os.path.join(CARPETA_RESULTADO, "IF_Chile_Acum.shp")

#--------------------------------------------------------------------------------------------------------------------------

# ELIMINACION DE DATOS

# 1.) Eliminacion de Shapefile descargado
# Process: Eliminar
arcpy.Delete_management(J1_VIIRS_C2_South_America_24h_shp, "ShapeFile")
print "Eliminacion de shapefile de puntos calientes realizada"


# 2.) Eliminacion de puntos calientes proyectados
# Process: Eliminar
arcpy.Delete_management(PC_Proyec_shp, "ShapeFile")
print "Eliminacion de puntos calientes proyectados realizada"

# 3.) Eliminacion del shp de recorte
# Process: Eliminar
arcpy.Delete_management(Recorte_shp, "ShapeFile")
print "Eliminacion del shp de recorte realizada"

# 4.) Eliminacion de Buffer
# Process: Eliminar
arcpy.Delete_management(Buffer_shp, "ShapeFile")
print "Eliminacion del shp de buffer realizada"

# 5.) Eliminacion de Interseca
# Process: Eliminar
arcpy.Delete_management(Intersecar_shp, "ShapeFile")
print "Eliminacion del shp de intersecar realizada"

# 6.) Eliminacion de disolver
# Process: Eliminar
arcpy.Delete_management(Disolver_shp, "ShapeFile")
print "Eliminacion del shp de disolver realizada"

# 7.) Eliminacion de IF_Chile
# Process: Eliminar
arcpy.Delete_management(IF_Chile_shp, "ShapeFile")
print "Eliminacion del shp de IF_Chile realizada"


# 8.) Elimina puntos calientes disueltos
# Process: Eliminar
arcpy.Delete_management(PuntosC_Chile_shp, "ShapeFile")
Delete_succeeded = "false"

# Process: Delete
arcpy.Delete_management(Recorte_Disolve_dia_shp, "ShapeFile")
Delete_succeeded = "false"

# Process: Delete
arcpy.Delete_management(Buffer_dia_shp, "ShapeFile")
Delete_succeeded = "false"

# Process: Delete
arcpy.Delete_management(Disolver_dia_shp, "ShapeFile")
Delete_succeeded = "false"

# Process: Delete
arcpy.Delete_management(Intersecar_dia_shp, "ShapeFile")


#--------------------------------------------------------------------------------------------------------------------------

# ENTRADA

# MANEJO DE INFORMACION DESCARGADA
# DEFINICION DE VARIABLES LOCALES


# DEFINICION DE FUNCIONES
# Funcion que descara archivo zip de puntos calientes de las ultimas 24hrs (VIIRS 375m)



url = 'https://firms.modaps.eosdis.nasa.gov/data/active_fire/noaa-20-viirs-c2/shapes/zips/J1_VIIRS_C2_South_America_24h.zip'
viirs_content = requests.get(url, verify=False)
open(zip_viirs, 'wb').write(viirs_content.content)
print ("Descarga de datos VIIRS realizada")
time.sleep(20)

#########################
## Antiguo metodo:
### zipdescargado = 'C:\Users\Administrador\Downloads\J1_VIIRS_C2_South_America_24h.zip'
### datosdescomprimidos = 'C:\Users\Administrador\Documents\Piloto_IF\Datos Descargados'
### descarga = webbrowser.open("https://firms.modaps.eosdis.nasa.gov/data/active_fire/viirs/shapes/zips/J1_VIIRS_C2_South_America_24h.zip", new=2, autoraise=True)
### print "Descarga de datos realizada"
### Funcion que pausa el proceso por 15 segundos
### time.sleep(20)
### Funcion que cierra el navegador web
### os.system("taskkill /im chrome.exe /f")
##########################

# Funcion que descomprime todos los archivos de la descarga
zf = zipfile.ZipFile(zip_viirs)
zf.extractall(CARPETA_DESCARGAS)

zf.close()
print "Archivos descomprimidos"

# Funcion que elimina el archivo de descarga
Eliminar = os.remove(zip_viirs)
print "Eliminacion del Archivo Zip descargado realizada"

#------------------------------------------------------------------------------
# BLOQUE PRINCIPAL / GEOPROCESOS
#------------------------------------------------------------------------------

# PROCESAMIENTO

# 1.) Proyeccion de datos descargados


# Process: Proyectar
arcpy.Project_management(J1_VIIRS_C2_South_America_24h_shp, PC_Proyec, "GEOGCS['GCS_WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]]", "", "GEOGCS['WGS 84',DATUM['WGS_1984',SPHEROID['WGS 84',6378137.0,298.257223563]],PRIMEM['Greenwich',0.0],UNIT['degree',0.0174532925199433]]", "NO_PRESERVE_SHAPE", "")
print "Proyeccion realizada"

# 2.) Recorte de puntos calientes con la DPA de Chile

# Process: Recortar
arcpy.Clip_analysis(PC_Proyec_shp, dpa_shp, Recorte_shp, "")
print "Recorte Realizado"

# 3.) Incorporar puntos calientes

# Process: Incorporar

field_mapping_text = Template(
    "LATITUDE \"LATITUDE\" true false false 19 Double 10 18 ,First,#,$path_recorte,LATITUDE,-1,-1;LONGITUDE \"LONGITUDE\" true false false 19 Double 10 18 ,First,#,$path_recorte,LONGITUDE,-1,-1;BRIGHT_TI4 \"BRIGHT_TI4\" true false false 19 Double 10 18 ,First,#,$path_recorte,BRIGHT_TI4,-1,-1;SCAN \"SCAN\" true false false 19 Double 10 18 ,First,#,$path_recorte,SCAN,-1,-1;TRACK \"TRACK\" true false false 19 Double 10 18 ,First,#,$path_recorte,TRACK,-1,-1;ACQ_DATE \"ACQ_DATE\" true true false 8 Date 0 0 ,First,#,$path_recorte,ACQ_DATE,-1,-1;ACQ_TIME \"ACQ_TIME\" true false false 4 Text 0 0 ,First,#,$path_recorte,ACQ_TIME,-1,-1;SATELLITE \"SATELLITE\" true false false 1 Text 0 0 ,First,#,$path_recorte,SATELLITE,-1,-1;CONFIDENCE \"CONFIDENCE\" true false false 7 Text 0 0 ,First,#,$path_recorte,CONFIDENCE,-1,-1;VERSION \"VERSION\" true false false 6 Text 0 0 ,First,#,$path_recorte,VERSION,-1,-1;BRIGHT_TI5 \"BRIGHT_TI5\" true false false 19 Double 10 18 ,First,#,$path_recorte,BRIGHT_TI5,-1,-1;FRP \"FRP\" true false false 19 Double 10 18 ,First,#,$path_recorte,FRP,-1,-1;DAYNIGHT \"DAYNIGHT\" true false false 1 Text 0 0 ,First,#,$path_recorte,DAYNIGHT,-1,-1"
).substitute(path_recorte=Recorte_shp)

arcpy.Append_management(
    Recorte_shp,
    PC_Chile_shp,
    "NO_TEST",
    field_mapping_text,
    ""
)
print "Incorporacion de puntos calientes Realizada"

# 3.1) Disolver puntos calientes segun coordenadas y fecha de descarga

# Process: Disolver
arcpy.Dissolve_management(PC_Chile_shp, PuntosC_Chile_shp, "LATITUDE;LONGITUDE;ACQ_DATE", "", "MULTI_PART", "DISSOLVE_LINES")


# 4.) Buffer
# Process: Zona de influencia
arcpy.Buffer_analysis(PuntosC_Chile_shp, Buffer_shp, "187 Meters", "FULL", "ROUND", "ALL", "", "PLANAR")
print "Buffer Realizado"

# 5.) Intersecar
# Process: Intersect

input_features = "{} #;{} #".format(
    dpa_shp,
    Buffer_shp
)
arcpy.Intersect_analysis(input_features, Intersecar_shp, "ALL", "", "INPUT")
print "Proceso de Intersecar Realizado"

# 6.) Disolver
# Process: Disolver
arcpy.Dissolve_management(Intersecar_shp, Disolver_shp, "comuna;provincia;region", "", "MULTI_PART", "DISSOLVE_LINES")
print "Proceso de Disolver Realizado"

# 7.) Calcular area

# Process: Agregar atributos de geometroa
arcpy.AddGeometryAttributes_management(Disolver_shp, "AREA_GEODESIC", "", "HECTARES", "PROJCS['WGS_1984_UTM_Zone_19S',GEOGCS['GCS_WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Transverse_Mercator'],PARAMETER['False_Easting',500000.0],PARAMETER['False_Northing',10000000.0],PARAMETER['Central_Meridian',-69.0],PARAMETER['Scale_Factor',0.9996],PARAMETER['Latitude_Of_Origin',0.0],UNIT['Meter',1.0]]")
print "Calculo del area en hectareas realizado"

# 8.) Agrega y calcula fecha
# Process: Agregar campo
arcpy.AddField_management(Disolver_shp, "Fecha", "DATE", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")

# Process: Calcular campo
arcpy.CalculateField_management(Disolver_shp, "Fecha", "time.strftime('%d/%m/%Y')", "PYTHON_9.3", "")
print "Calculo de la fecha realizado"

# 11.) Copia resultado
# Process: Copiar entidades
arcpy.CopyFeatures_management(Disolver_shp, IF_Chile_shp, "", "0", "0", "0")

# 10.) Incorpora resultado acum
# Process: Append

field_mapping_text = Template(
    "comuna \"comuna\" true false false 30 Text 0 0 ,First,#,$if_chile_path,comuna,-1,-1;provincia \"provincia\" true false false 30 Text 0 0 ,First,#,$if_chile_path,provincia,-1,-1;region \"region\" true false false 50 Text 0 0 ,First,#,$if_chile_path,region,-1,-1;AREA_GEO \"AREA_GEO\" true false false 19 Double 0 0 ,First,#,$if_chile_path,AREA_GEO,-1,-1;FECHA \"FECHA\" true true false 8 Date 0 0 ,First,#,$if_chile_path,Fecha,-1,-1"
).substitute(if_chile_path=IF_Chile_shp)

arcpy.Append_management(
    IF_Chile_shp,
    IF_Chile_Acum_shp,
    "NO_TEST",
    field_mapping_text,
    ""
)


# Nuevo...............................................................................................................................


# Process: Dissolve
arcpy.Dissolve_management(Recorte_shp, Recorte_Disolve_dia_shp, "LATITUDE;LONGITUDE;ACQ_DATE", "", "MULTI_PART", "DISSOLVE_LINES")
print "Proceso de Disolver dia Realizado"

# Process: Buffer
arcpy.Buffer_analysis(Recorte_Disolve_dia_shp, Buffer_dia_shp, "187 Meters", "FULL", "ROUND", "ALL", "", "PLANAR")
print "Buffer dia Realizado"

# Process: Intersect

input_features = "{} #;{} #".format(
    Buffer_dia_shp,
    dpa_shp
)
arcpy.Intersect_analysis(input_features, Intersecar_dia_shp, "ALL", "", "INPUT")
print "Proceso de Intersecar dia Realizado"

# Process: Dissolve
arcpy.Dissolve_management(Intersecar_dia_shp, Disolver_dia_shp, "comuna;provincia;region", "", "MULTI_PART", "DISSOLVE_LINES")
print "Proceso de Disolver dia Realizado"

isolver_dia_shp__3_ = Disolver_dia_shp

# Process: Add Geometry Attributes
arcpy.AddGeometryAttributes_management(Disolver_dia_shp, "AREA_GEODESIC", "", "HECTARES", "GEOGCS['GCS_WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]]")
print "Colculo del area en hectareas dia realizado"

# Process: Add Field
arcpy.AddField_management(Disolver_dia_shp, "Fecha", "DATE", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")

# Process: Calculate Field
arcpy.CalculateField_management(Disolver_dia_shp, "Fecha", "time.strftime('%d/%m/%Y')", "PYTHON_9.3", "")
print "Colculo de la fecha dia realizado"

# Process: Delete Rows
arcpy.DeleteRows_management(puntos_calientes_sde_puntos_calientes_dia)
print "Elimina registros dia de la sde"

# Process: Append

field_mapping_text = Template(
        "comuna \"comuna\" true true false 30 Text 0 0 ,First,#,$path_disolver_dia,comuna,-1,-1;provincia \"provincia\" true true false 30 Text 0 0 ,First,#,$path_disolver_dia,provincia,-1,-1;region \"region\" true true false 50 Text 0 0 ,First,#,$path_disolver_dia,region,-1,-1;area_geo \"area_geo\" true true false 8 Double 8 38 ,First,#,$path_disolver_dia,AREA_GEO,-1,-1;fecha \"fecha\" true true false 36 Date 0 0 ,First,#,$path_disolver_dia,Fecha,-1,-1;GlobalID \"GlobalID\" false false false 38 GlobalID 0 0 ,First,#;st_area(shape) \"st_area(shape)\" false false true 0 Double 0 0 ,First,#;st_length(shape) \"st_length(shape)\" false false true 0 Double 0 0 ,First,#"
).substitute(path_disolver_dia=Disolver_dia_shp)

arcpy.Append_management(
    Disolver_dia_shp,
    puntos_calientes_sde_puntos_calientes_dia,
    "NO_TEST", 
    field_mapping_text,
    ""
)
print "Incorporacion de puntos calientes dia Realizada"


# Termino nuevo.................................................................

# ---------------------------------------------------------------------------------------------------------------------------------

# SALIDA

# 2.) Elimina filas de la base de datos (a la fecha) sde
# Process: Delete Rows
arcpy.DeleteRows_management(puntos_calientes_sde_puntos_calientes_a_la_fecha)
print "Elimina registros a la fecha de la sde"

# 3.) Incorpora filas de la base de datos (a la fecha) sde
# Process: Append
field_mapping_text = Template(
    "comuna \"comuna\" true true false 30 Text 0 0 ,First,#,$path_if,comuna,-1,-1;provincia \"provincia\" true true false 30 Text 0 0 ,First,#,$path_if,provincia,-1,-1;region \"region\" true true false 50 Text 0 0 ,First,#,$path_if,region,-1,-1;area_geo \"area_geo\" true true false 8 Double 8 38 ,First,#,$path_if,AREA_GEO,-1,-1;fecha \"fecha\" true true false 36 Date 0 0 ,First,#,$path_if,Fecha,-1,-1;GlobalID \"GlobalID\" false false false 38 GlobalID 0 0 ,First,#;st_area(shape) \"st_area(shape)\" false false true 0 Double 0 0 ,First,#;st_length(shape) \"st_length(shape)\" false false true 0 Double 0 0 ,First,#"
).substitute(path_if=IF_Chile_shp)

arcpy.Append_management(
    IF_Chile_shp,
    puntos_calientes_sde_puntos_calientes_a_la_fecha,
    "NO_TEST", 
    field_mapping_text,
    ""
)
print "Incorpora nuevos registros a la fecha de la sde"


#---------------------------------------------------------------------------------

print "Proceso realizado exitosamente"

# FIN DEL PROGRAMA

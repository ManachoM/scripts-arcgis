# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# Publicacion_shakemap_gdb.py
# Created on: 2019-02-27 11:23:44.00000
#   (generated by ArcGIS/ModelBuilder)
# Description:
# ---------------------------------------------------------------------------
#ejecutar desde cmd
# "C:\Python27\ArcGIS10.3\python.exe" "C:\\Users\\Administrador\\Documents\\SHAKEMAP_2019\Python\Proceso_Publicación_ShakeMap_SE.py"

# Import arcpy module
import arcpy
import os
from string import Template

# Definicion de variables:
FILE_GDB_PATH = "E:\\scripts-arcgis\\Shakemap\\SHAKEMAP_2019\\Importa_shake.gdb"
GDB_PATH = "E:\\scripts-arcgis\\sde\\Shakemap_197.sde"

shakemap = FILE_GDB_PATH + "\\shakemap"
shakemap_entero = FILE_GDB_PATH + "\\shakemap_entero"
shakemap_sde_shakemap = GDB_PATH + "\\shakemap.sde.shakemap"

CARPETA_SHAKE_ENTRADA = "E:\\scripts-arcgis\\Shakemap\\SHAKEMAP_ENTRADA\\"
CARPETA_SHAKE_POLIGONO = "E:\\scripts-arcgis\\Shakemap\\SHAKEMAP_2019\\Shake_Poligono\\"
CARPETA_SHAKE_DISUELTO = "E:\\scripts-arcgis\\Shakemap\\SHAKEMAP_2019\\Shake_Disuelto\\"
CARPETA_SHAKE_CORTADO = "E:\\scripts-arcgis\\Shakemap\\SHAKEMAP_2019\\Shake_Cortado\\"
CARPETA_SHAKE_JOIN = "E:\\scripts-arcgis\\Shakemap\\SHAKEMAP_2019\\Join\\"
CARPETA_SHAKE_CLIP = "E:\\scripts-arcgis\\Shakemap\\SHAKEMAP_2019\\Clip\\"

shakemap_poligono_shp = os.path.join(CARPETA_SHAKE_POLIGONO, "shakemap_poligono.shp")
poligono_disuelto_shp = os.path.join(CARPETA_SHAKE_DISUELTO, "poligono_disuelto.shp")
shakemap_cortado_shp = os.path.join(CARPETA_SHAKE_CORTADO, "shakemap_cortado.shp")
shakemap_cortado_disuelto_shp = os.path.join(CARPETA_SHAKE_CORTADO, "shakemap_cortado_disuelto.shp")
shakemap_grd = os.path.join(CARPETA_SHAKE_ENTRADA, "shakemap.grd")
Intensidad_dbf = os.path.join(CARPETA_SHAKE_JOIN, "Intensidad.dbf")
DPA_shp = os.path.join(CARPETA_SHAKE_CLIP, "DPA.shp")

print "Borra correctamente shakemap de la gdb"
# Local variables:
La_eliminacion_se_realizo_correctamente__2_ = "true"

# Process: Eliminar (2)
arcpy.Delete_management(shakemap, "RasterDataset")

print "Borra correctamente shakemap_entero de la gdb"
# Local variables:
La_eliminacion_se_realizo_correctamente__2_ = "true"

# Process: Eliminar (2)
arcpy.Delete_management(shakemap_entero, "RasterDataset")

print "Borra correctamente el shakemap_poligono.shp"
# Local variables:
La_eliminacion_se_realizo_correctamente__2_ = "true"

# Process: Eliminar (2)
arcpy.Delete_management(shakemap_poligono_shp, "ShapeFile")

print "Borra correctamente el poligono_disuelto.shp"
# Local variables:
La_eliminacion_se_realizo_correctamente__2_ = "true"

# Process: Eliminar (2)
arcpy.Delete_management(poligono_disuelto_shp, "ShapeFile")

print "Borra correctamente el shakemap_cortado.shp"
# Local variables:
La_eliminacion_se_realizo_correctamente__2_ = "true"

# Process: Eliminar (2)
arcpy.Delete_management(shakemap_cortado_shp, "ShapeFile")

print "Borra correctamente el shakemap_cortado_disuelto.shp"
# Local variables:
La_eliminacion_se_realizo_correctamente = "false"

# Process: Eliminar
arcpy.Delete_management(shakemap_cortado_disuelto_shp, "ShapeFile")

print "Importa correctamente el shakemap a la BD.gdb"

# Process: De ráster a geodatabase
arcpy.RasterToGeodatabase_conversion(shakemap_grd, FILE_GDB_PATH, "")

print "Transforma correctamente shakemap de ráster a poligono"
# Process: De ráster a polígono
arcpy.RasterToPolygon_conversion(shakemap, shakemap_poligono_shp, "NO_SIMPLIFY", "Value")

# Local variables:
print "Define correctamente la proyección del shakemap poligono"
# Process: Definir proyección
arcpy.DefineProjection_management(shakemap_poligono_shp, "GEOGCS['GCS_WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]]")

# Local variables:

print "disuelve correctamente el shakemap poligono"
# Process: Disolver
arcpy.Dissolve_management(shakemap_poligono_shp, poligono_disuelto_shp, "GRIDCODE", "", "MULTI_PART", "DISSOLVE_LINES")

# Local variables:
print "Asocia correctamente la simbología"
# Process: Campo de unión
arcpy.JoinField_management(poligono_disuelto_shp, "GRIDCODE", Intensidad_dbf, "GRIDCODE", "GRIDCODE;INTENS_INS")

# Local variables:

print "Recorta correctamente el océano del shakemap poligono"
# Process: Recortar
arcpy.Clip_analysis(poligono_disuelto_shp, DPA_shp, shakemap_cortado_shp, "")

# Local variables:

print "disuelve correctamente la simbología"
# Process: Disolver
arcpy.Dissolve_management(shakemap_cortado_shp, shakemap_cortado_disuelto_shp, "INTENS_INS", "", "MULTI_PART", "DISSOLVE_LINES")

# Local variables:

# Process: Delete Rows
arcpy.DeleteRows_management(shakemap_sde_shakemap)
print "Elimina correctamente los registros de la BD .SDE"


# Local variables

field_mapping_text = Template (
    "intens_ins \"intens_ins\" true true false 254 Text 0 0 ,First,#,$path_cd,INTENS_INS,-1,-1;st_area(shape) \"st_area(shape)\" false false true 0 Double 0 0 ,First,#;st_length(shape) \"st_length(shape)\" false false true 0 Double 0 0 ,First,#"
).substitute(path_cd=shakemap_cortado_disuelto_shp)

# Process: Append
arcpy.Append_management(
    shakemap_cortado_disuelto_shp,
    shakemap_sde_shakemap,
    "NO_TEST",
    field_mapping_text,
    ""
)
print "incorpora correctamente los nuevos registros a la BD .SDE"

print "elimina shakemap.grd de la carpeta entrada"

# Local variables:
Delete_succeeded = "false"

# Process: Delete
arcpy.Delete_management(shakemap_grd, "RasterDataset")

print "shakemap.grd eliminado"

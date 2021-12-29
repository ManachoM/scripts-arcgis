# -*- coding: cp1252 -*-
#ejecutar desde cmd
# "C:\Python27\ArcGISx6410.7\python.exe" "E:\scripts-arcgis\wfs_MOP\Descarga_WMS.py"


import arcpy
from datetime import datetime, date, time, timedelta
import calendar
import os
from string import Template

ahora = datetime.now()
print ('Hora:',ahora.hour,ahora.minute,ahora.second)

# Definición de variables:

GDB_PATH = "E:\\scripts-arcgis\\wfs_MOP\\WFS_MOP\\MOP_WMS.gdb"
WFS_MOP_SDE = "E:\\scripts-arcgis\\sde\\wfs_mop_214.sde\\"
#WFS_MOP_SDE = "E:\\scripts-arcgis\\sde\\wfs_mop_197.sde\\"

CARPETA_MOP_PROJ = "E:\\scripts-arcgis\\wfs_MOP\\WFS_MOP\\MOP_WMS_Proj\\"
CARPETA_INTERSECT = "E:\\scripts-arcgis\\wfs_MOP\\WFS_MOP\\MOP_WMS_Intersect\\"
CARPETA_DPA = "E:\\scripts-arcgis\\wfs_MOP\\WFS_MOP\\DPA\\"

MOP_WMS_gdb = GDB_PATH

# Datos de GDB:
Aeropuertos_nacionales = MOP_WMS_gdb + "\\Aeropuertos_nacionales"
Ubicaciones_de_APR = MOP_WMS_gdb + "\\Ubicaciones_de_APR"
Obras_Portuarias = MOP_WMS_gdb + "\\Obras_Portuarias"
Tuneles = MOP_WMS_gdb + "\\Tuneles"
Catastro_de_Embalses = MOP_WMS_gdb + "\\Catastro_de_Embalses"
Puentes = MOP_WMS_gdb + "\\Puentes"
#Red_Vial_Nacional = MOP_WMS_gdb + "\\Red_Vial_Nacional"

# Datos proyectados:
Aeropuertos_nacionales_point_shp = os.path.join(CARPETA_MOP_PROJ, "Aeropuertos_nacionales_point.shp")
Catastro_de_Embalses_point_shp = os.path.join(CARPETA_MOP_PROJ, "Catastro_de_Embalses_point.shp")
Obras_Portuarias_point_shp = os.path.join(CARPETA_MOP_PROJ, "Obras_Portuarias_point.shp")
Puentes_shp = os.path.join(CARPETA_MOP_PROJ, "Puentes.shp")
#Red_Vial_Nacional_line_shp = os.path.join(CARPETA_MOP_PROJ, "Red_Vial_Nacional_line.shp")
Tuneles_shp = os.path.join(CARPETA_MOP_PROJ, "Tuneles.shp")
Ubicaciones_de_APR_point_shp = os.path.join(CARPETA_MOP_PROJ, "Ubicaciones_de_APR_point.shp")

# Datos intersectados:
Comunas_shp = os.path.join(CARPETA_DPA, "Comunas.shp")
Aeropuertos_nacionales_point_shp_intersect = os.path.join(CARPETA_INTERSECT, "Aeropuertos_nacionales_point.shp")
Catastro_de_Embalses_point_shp_intersect = os.path.join(CARPETA_INTERSECT, "Catastro_de_Embalses_point.shp")
Obras_Portuarias_point_shp_intersect = os.path.join(CARPETA_INTERSECT, "Obras_Portuarias_point.shp")
Puentes_shp_intersect = os.path.join(CARPETA_INTERSECT, "Puentes.shp")
#Red_Vial_Nacional_line_shp_intersect = os.path.join(CARPETA_INTERSECT, "Red_Vial_Nacional_line.shp")
Ubicaciones_de_APR_point_shp_intersect = os.path.join(CARPETA_INTERSECT, "Ubicaciones_de_APR_point.shp")
Tuneles_shp_intersect = os.path.join(CARPETA_INTERSECT, "Tuneles_line.shp")


Puentes__2_ = os.path.join(CARPETA_MOP_PROJ, "Puentes")
#Red_Vial_Nacional_line = Red_Vial_Nacional_line_shp
Tuneles__2_ = os.path.join(CARPETA_MOP_PROJ, "Tuneles")
Ubicaciones_de_APR_point = os.path.join(CARPETA_MOP_PROJ, "Ubicaciones_de_APR_point")

Aeropuertos_nacionales_point_shp__2_ = os.path.join(CARPETA_INTERSECT, "Aeropuertos_nacionales_point.shp")
Ubicaciones_de_APR_point_shp__2_ = os.path.join(CARPETA_INTERSECT, "Ubicaciones_de_APR_point.shp")
Catastro_de_Embalses_point_shp__2_ = os.path.join(CARPETA_INTERSECT, "Catastro_de_Embalses_point.shp")
Obras_Portuarias_point_shp__3_ = os.path.join(CARPETA_INTERSECT, "Obras_Portuarias_point.shp")
Puentes_shp__2_ = os.path.join(CARPETA_INTERSECT, "Puentes.shp")
#Red_Vial_Nacional_line_shp__2_ = os.path.join(CARPETA_INTERSECT, "Red_Vial_Nacional_line.shp")
Tuneles_shp__2_ = os.path.join(CARPETA_INTERSECT, "Tuneles.shp")

wfs_mop_sde_Aeropuertos_nacionales_point = WFS_MOP_SDE + "wfs_mop.sde.Aeropuertos_nacionales_point"
wfs_mop_sde_Catastro_de_Embalses_point = WFS_MOP_SDE + "wfs_mop.sde.Catastro_de_Embalses_point"
wfs_mop_sde_Obras_Portuarias_point = WFS_MOP_SDE + "wfs_mop.sde.Obras_Portuarias_point"
wfs_mop_sde_Puentes_point = WFS_MOP_SDE + "wfs_mop.sde.Puentes_point"
#wfs_mop_sde_Red_Vial_Nacional_line = WFS_MOP_SDE + "wfs_mop.sde.Red_Vial_Nacional_line"
wfs_mop_sde_Tuneles_line = WFS_MOP_SDE + "wfs_mop.sde.Tuneles_line"
wfs_mop_sde_Ubicaciones_de_APR_point = WFS_MOP_SDE + "wfs_mop.sde.Ubicaciones_de_APR_point"

wfs_mop_sde_Catastro_de_Embalses_point__2_ = WFS_MOP_SDE + "wfs_mop.sde.Catastro_de_Embalses_point"




arcpy.Delete_management(Catastro_de_Embalses, "FeatureClass")
arcpy.Delete_management(Aeropuertos_nacionales, "FeatureClass")
arcpy.Delete_management(Ubicaciones_de_APR, "FeatureClass")
arcpy.Delete_management(Obras_Portuarias, "FeatureClass")
arcpy.Delete_management(Tuneles, "FeatureClass")
arcpy.Delete_management(Puentes, "FeatureClass")
#arcpy.Delete_management(Red_Vial_Nacional, "FeatureClass")
print 'Eliminacion exitosa de los datos de la BD'


print 'Eliminacion de Datos proyectados'
arcpy.Delete_management(Aeropuertos_nacionales_point_shp, "ShapeFile")
arcpy.Delete_management(Catastro_de_Embalses_point_shp, "ShapeFile")
arcpy.Delete_management(Obras_Portuarias_point_shp, "ShapeFile")
arcpy.Delete_management(Puentes_shp, "ShapeFile")
#arcpy.Delete_management(Red_Vial_Nacional_line_shp, "ShapeFile")
arcpy.Delete_management(Tuneles_shp, "ShapeFile")
arcpy.Delete_management(Ubicaciones_de_APR_point_shp, "ShapeFile")
print 'Eliminacion Exitosa de Datos proyectados'


print 'Eliminacion de Datos Intersectados'
arcpy.Delete_management(Aeropuertos_nacionales_point_shp_intersect, "ShapeFile")
arcpy.Delete_management(Catastro_de_Embalses_point_shp_intersect, "ShapeFile")
arcpy.Delete_management(Obras_Portuarias_point_shp_intersect, "ShapeFile")
arcpy.Delete_management(Puentes_shp_intersect, "ShapeFile")
#arcpy.Delete_management(Red_Vial_Nacional_line_shp_intersect, "ShapeFile")
arcpy.Delete_management(Tuneles_shp_intersect, "ShapeFile")
arcpy.Delete_management(Ubicaciones_de_APR_point_shp_intersect, "ShapeFile")
print 'Eliminacion Exitosa de Datos Intersectados'

print 'Inicio Descarga WFS'
arcpy.WFSToFeatureClass_conversion("https://rest-sit.mop.gov.cl/arcgis/services/IDE_MOP/INFRA_MOP_ONEMI/MapServer/WFSServer?request=GetCapabilities&service=WFS", "Catastro_de_Embalses", MOP_WMS_gdb, "Catastro_de_Embalses")
arcpy.WFSToFeatureClass_conversion("https://rest-sit.mop.gov.cl/arcgis/services/IDE_MOP/INFRA_MOP_ONEMI/MapServer/WFSServer?request=GetCapabilities&service=WFS", "Aeropuertos_nacionales", MOP_WMS_gdb, "Aeropuertos_nacionales")
arcpy.WFSToFeatureClass_conversion("https://rest-sit.mop.gov.cl/arcgis/services/IDE_MOP/INFRA_MOP_ONEMI/MapServer/WFSServer?request=GetCapabilities&service=WFS", "Ubicaciones_de_APR", MOP_WMS_gdb, "Ubicaciones_de_APR")
arcpy.WFSToFeatureClass_conversion("https://rest-sit.mop.gov.cl/arcgis/services/IDE_MOP/INFRA_MOP_ONEMI/MapServer/WFSServer?request=GetCapabilities&service=WFS", "Obras_Portuarias", MOP_WMS_gdb, "Obras_Portuarias")
arcpy.WFSToFeatureClass_conversion("https://rest-sit.mop.gov.cl/arcgis/services/IDE_MOP/INFRA_MOP_ONEMI/MapServer/WFSServer?request=GetCapabilities&service=WFS", "Tuneles", MOP_WMS_gdb, "Tuneles")
arcpy.WFSToFeatureClass_conversion("https://rest-sit.mop.gov.cl/arcgis/services/IDE_MOP/INFRA_MOP_ONEMI/MapServer/WFSServer?request=GetCapabilities&service=WFS", "Puentes", MOP_WMS_gdb, "Puentes")
#arcpy.WFSToFeatureClass_conversion("https://rest-sit.mop.gov.cl/arcgis/services/IDE_MOP/INFRA_MOP_ONEMI/MapServer/WFSServer?request=GetCapabilities&service=WFS", "Red_Vial_Nacional", MOP_WMS_gdb, "Red_Vial_Nacional")
print 'Descarga WFS exitosa'

print 'Eliminar campos'
arcpy.DeleteField_management(Ubicaciones_de_APR, "Comuna")
arcpy.DeleteField_management(Tuneles, "Regi�n")
#arcpy.DeleteField_management(Red_Vial_Nacional, "Provincia;Regi�n")
arcpy.DeleteField_management(Puentes, "Regi�n")
arcpy.DeleteField_management(Obras_Portuarias, "Comuna")
arcpy.DeleteField_management(Catastro_de_Embalses, "Comuna;Regi�n")
print 'Eliminacion exitosa de campos'


print 'Inicio Proyeccion'
# Process: Proyectar
arcpy.Project_management(Aeropuertos_nacionales, Aeropuertos_nacionales_point_shp, "GEOGCS['GCS_WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]]", "SIRGAS_2000_To_WGS_1984_1", "GEOGCS['GCS_SIRGAS_2000',DATUM['D_SIRGAS_2000',SPHEROID['GRS_1980',6378137.0,298.257222101]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]]", "NO_PRESERVE_SHAPE", "")
arcpy.Project_management(Catastro_de_Embalses, Catastro_de_Embalses_point_shp, "GEOGCS['GCS_WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]]", "SIRGAS_2000_To_WGS_1984_1", "GEOGCS['GCS_SIRGAS_2000',DATUM['D_SIRGAS_2000',SPHEROID['GRS_1980',6378137.0,298.257222101]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]]", "NO_PRESERVE_SHAPE", "")
arcpy.Project_management(Obras_Portuarias, Obras_Portuarias_point_shp, "GEOGCS['GCS_WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]]", "SIRGAS_2000_To_WGS_1984_1", "GEOGCS['GCS_SIRGAS_2000',DATUM['D_SIRGAS_2000',SPHEROID['GRS_1980',6378137.0,298.257222101]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]]", "NO_PRESERVE_SHAPE", "")
arcpy.Project_management(Puentes, Puentes_shp, "GEOGCS['GCS_WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]]", "SIRGAS_2000_To_WGS_1984_1", "GEOGCS['GCS_SIRGAS_2000',DATUM['D_SIRGAS_2000',SPHEROID['GRS_1980',6378137.0,298.257222101]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]]", "NO_PRESERVE_SHAPE", "")
#arcpy.Project_management(Red_Vial_Nacional, Red_Vial_Nacional_line_shp, "GEOGCS['GCS_WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]]", "SIRGAS_2000_To_WGS_1984_1", "GEOGCS['GCS_SIRGAS_2000',DATUM['D_SIRGAS_2000',SPHEROID['GRS_1980',6378137.0,298.257222101]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]]", "NO_PRESERVE_SHAPE", "")
arcpy.Project_management(Tuneles, Tuneles_shp, "GEOGCS['GCS_WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]]", "SIRGAS_2000_To_WGS_1984_1", "GEOGCS['GCS_SIRGAS_2000',DATUM['D_SIRGAS_2000',SPHEROID['GRS_1980',6378137.0,298.257222101]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]]", "NO_PRESERVE_SHAPE", "")
arcpy.Project_management(Ubicaciones_de_APR, Ubicaciones_de_APR_point_shp, "GEOGCS['GCS_WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]]", "SIRGAS_2000_To_WGS_1984_1", "GEOGCS['GCS_SIRGAS_2000',DATUM['D_SIRGAS_2000',SPHEROID['GRS_1980',6378137.0,298.257222101]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]]", "NO_PRESERVE_SHAPE", "")
print 'Proyeccion correcta'

print 'Interseccion con DPA'
arcpy.Intersect_analysis("{} #;{} #".format(Comunas_shp, Aeropuertos_nacionales_point_shp), Aeropuertos_nacionales_point_shp_intersect, "ALL", "", "INPUT")
arcpy.Intersect_analysis("{} #;{} #".format(Comunas_shp, Ubicaciones_de_APR_point_shp), Ubicaciones_de_APR_point_shp_intersect, "ALL", "", "INPUT")
arcpy.Intersect_analysis("{} #;{} #".format(Comunas_shp, Catastro_de_Embalses_point_shp), Catastro_de_Embalses_point_shp_intersect, "ALL", "", "INPUT")
arcpy.Intersect_analysis("{} #;{} #".format(Obras_Portuarias_point_shp, Comunas_shp), Obras_Portuarias_point_shp_intersect, "ALL", "", "INPUT")
arcpy.Intersect_analysis("{} #;{} #".format(Comunas_shp, Puentes_shp), Puentes_shp_intersect, "ALL", "", "INPUT")
#arcpy.Intersect_analysis("{} #;{} #".format(Comunas_shp, Red_Vial_Nacional_line_shp), Red_Vial_Nacional_line_shp_intersect, "ALL", "", "INPUT")
arcpy.Intersect_analysis("{} #;{} #".format(Comunas_shp, Tuneles_shp), Tuneles_shp_intersect, "ALL", "", "INPUT")
print 'Interseccion exitosa'

print 'Eliminar registros de la BD'
arcpy.DeleteRows_management(wfs_mop_sde_Aeropuertos_nacionales_point)
arcpy.DeleteRows_management(wfs_mop_sde_Catastro_de_Embalses_point)
arcpy.DeleteRows_management(wfs_mop_sde_Obras_Portuarias_point)
arcpy.DeleteRows_management(wfs_mop_sde_Puentes_point)
#arcpy.DeleteRows_management(wfs_mop_sde_Red_Vial_Nacional_line)
arcpy.DeleteRows_management(wfs_mop_sde_Tuneles_line)
arcpy.DeleteRows_management(wfs_mop_sde_Ubicaciones_de_APR_point)
print 'Eliminacion exitosa'

print 'Incorporar nuevos Datos a la BD'

# Process: Incorporar (6)
arcpy.Append_management(
    Aeropuertos_nacionales_point_shp_intersect,
    wfs_mop_sde_Aeropuertos_nacionales_point,
    "NO_TEST",
    Template(
        "fid_comuna \"fid_comuna\" true true false 4 Long 0 10 ,First,#,$path_shp,FID_Comuna,-1,-1;region \"region\" true true false 60 Text 0 0 ,First,#,$path_shp,region,-1,-1;comuna \"comuna\" true true false 60 Text 0 0 ,First,#,$path_shp,comuna,-1,-1;provincia \"provincia\" true true false 60 Text 0 0 ,First,#,$path_shp,provincia,-1,-1;fid_aeropu \"fid_aeropu\" true true false 4 Long 0 10 ,First,#,$path_shp,FID_Aeropu,-1,-1;objectid \"objectid\" true true false 4 Long 0 10 ,First,#,$path_shp,OBJECTID,-1,-1;nombre \"nombre\" true true false 150 Text 0 0 ,First,#,$path_shp,Nombre,-1,-1;ubicacion \"ubicacion\" true true false 250 Text 0 0 ,First,#,$path_shp,Ubicacion,-1,-1;propiedad \"propiedad\" true true false 50 Text 0 0 ,First,#,$path_shp,Propiedad,-1,-1;tipo \"tipo\" true true false 50 Text 0 0 ,First,#,$path_shp,Tipo,-1,-1;red_del_ae \"red_del_ae\" true true false 50 Text 0 0 ,First,#,$path_shp,Red_del_Ae,-1,-1"
    ).substitute(path_shp=Aeropuertos_nacionales_point_shp_intersect),
    ""
)

# Process: Incorporar (6)
arcpy.Append_management(
    Catastro_de_Embalses_point_shp_intersect,
    wfs_mop_sde_Catastro_de_Embalses_point,
    "NO_TEST",
    Template(
        "fid_comuna \"fid_comuna\" true true false 4 Long 0 10 ,First,#,$path_shp,FID_Comuna,-1,-1;region \"region\" true true false 60 Text 0 0 ,First,#,$path_shp,region,-1,-1;comuna \"comuna\" true true false 60 Text 0 0 ,First,#,$path_shp,comuna,-1,-1;provincia \"provincia\" true true false 60 Text 0 0 ,First,#,$path_shp,provincia,-1,-1;fid_catast \"fid_catast\" true true false 4 Long 0 10 ,First,#,$path_shp,FID_Catast,-1,-1;objectid \"objectid\" true true false 4 Long 0 10 ,First,#,$path_shp,OBJECTID,-1,-1;nombre \"nombre\" true true false 50 Text 0 0 ,First,#,$path_shp,Nombre,-1,-1;altura_mur \"altura_mur\" true true false 4 Long 0 10 ,First,#,$path_shp,Altura_Mur,-1,-1;uso_embals \"uso_embals\" true true false 100 Text 0 0 ,First,#,$path_shp,Uso_Embals,-1,-1"
    ).substitute(path_shp=Catastro_de_Embalses_point_shp_intersect),
    ""
)

# Process: Incorporar (6)
arcpy.Append_management(
    Obras_Portuarias_point_shp_intersect,
    wfs_mop_sde_Obras_Portuarias_point,
    "NO_TEST",
    Template (
        "fid_obras_ \"fid_obras_\" true true false 4 Long 0 10 ,First,#,$path_shp,FID_Obras_,-1,-1;objectid \"objectid\" true true false 4 Long 0 10 ,First,#,$path_shp,OBJECTID,-1,-1;tipo_de_ob \"tipo_de_ob\" true true false 50 Text 0 0 ,First,#,$path_shp,Tipo_de_Ob,-1,-1;nombre_de_ \"nombre_de_\" true true false 250 Text 0 0 ,First,#,$path_shp,Nombre_de_,-1,-1;globalid \"globalid\" true true false 38 Text 0 0 ,First,#,$path_shp,GlobalID,-1,-1;fid_comuna \"fid_comuna\" true true false 4 Long 0 10 ,First,#,$path_shp,FID_Comuna,-1,-1;region \"region\" true true false 60 Text 0 0 ,First,#,$path_shp,region,-1,-1;comuna \"comuna\" true true false 60 Text 0 0 ,First,#,$path_shp,comuna,-1,-1;provincia \"provincia\" true true false 60 Text 0 0 ,First,#,$path_shp,provincia,-1,-1"
    ).substitute(path_shp=Obras_Portuarias_point_shp_intersect),
    ""
)

# Process: Incorporar (6)
arcpy.Append_management(
    Puentes_shp_intersect,
    wfs_mop_sde_Puentes_point,
    "NO_TEST",
    Template(
        "fid_comuna \"fid_comuna\" true true false 4 Long 0 10 ,First,#,$path_shp,FID_Comuna,-1,-1;region \"region\" true true false 60 Text 0 0 ,First,#,$path_shp,region,-1,-1;comuna \"comuna\" true true false 60 Text 0 0 ,First,#,$path_shp,comuna,-1,-1;provincia \"provincia\" true true false 60 Text 0 0 ,First,#,$path_shp,provincia,-1,-1;fid_puente \"fid_puente\" true true false 4 Long 0 10 ,First,#,$path_shp,FID_Puente,-1,-1;objectid \"objectid\" true true false 4 Long 0 10 ,First,#,$path_shp,OBJECTID,-1,-1;rol_v�a \"rol_v�a\" true true false 40 Text 0 0 ,First,#,$path_shp,Rol_V�a,-1,-1;nombre \"nombre\" true true false 75 Text 0 0 ,First,#,$path_shp,Nombre,-1,-1;largo \"largo\" true true false 8 Double 8 38 ,First,#,$path_shp,Largo,-1,-1"
    ).substitute(path_shp=Puentes_shp_intersect),
    ""
)

# Process: Incorporar (6)
#arcpy.Append_management(
    #Red_Vial_Nacional_line_shp_intersect,
    #wfs_mop_sde_Red_Vial_Nacional_line,
    #"NO_TEST",
    #Template(
        #"fid_comuna \"fid_comuna\" true true false 4 Long 0 10 ,First,#,$path_shp,FID_Comuna,-1,-1;region \"region\" true true false 60 Text 0 0 ,First,#,$path_shp,region,-1,-1;comuna \"comuna\" true true false 60 Text 0 0 ,First,#,$path_shp,comuna,-1,-1;provincia \"provincia\" true true false 60 Text 0 0 ,First,#,$path_shp,provincia,-1,-1;fid_red_vi \"fid_red_vi\" true true false 4 Long 0 10 ,First,#,$path_shp,FID_Red_Vi,-1,-1;objectid \"objectid\" true true false 4 Long 0 10 ,First,#,$path_shp,OBJECTID,-1,-1;rol_v�a \"rol_v�a\" true true false 20 Text 0 0 ,First,#,$path_shp,Rol_V�a,-1,-1;nombre \"nombre\" true true false 254 Text 0 0 ,First,#,$path_shp,Nombre,-1,-1;km_total \"km_total\" true true false 4 Long 0 10 ,First,#,$path_shp,Km_Total,-1,-1;clasificac \"clasificac\" true true false 70 Text 0 0 ,First,#,$path_shp,Clasificac,-1,-1;km_inicio \"km_inicio\" true true false 4 Long 0 10 ,First,#,$path_shp,Km_Inicio,-1,-1;km_fin \"km_fin\" true true false 4 Long 0 10 ,First,#,$path_shp,Km_Fin,-1,-1;shape_stle \"shape_stle\" true true false 8 Double 8 38 ,First,#,$path_shp,SHAPE_STLe,-1,-1;shape_leng \"shape_leng\" true true false 8 Double 8 38 ,First,#,$path_shp,SHAPE_Leng,-1,-1;st_length(shape) \"st_length(shape)\" false false true 0 Double 0 0 ,First,#"
    #).substitute(path_shp=Red_Vial_Nacional_line_shp_intersect),
    #""
#)#

# Process: Incorporar (6)
arcpy.Append_management(
    Tuneles_shp_intersect,
    wfs_mop_sde_Tuneles_line,
    "NO_TEST",
    Template(
        "fid_comuna \"fid_comuna\" true true false 4 Long 0 10 ,First,#,$path_shp,FID_Comuna,-1,-1;region \"region\" true true false 60 Text 0 0 ,First,#,$path_shp,region,-1,-1;comuna \"comuna\" true true false 60 Text 0 0 ,First,#,$path_shp,comuna,-1,-1;provincia \"provincia\" true true false 60 Text 0 0 ,First,#,$path_shp,provincia,-1,-1;fid_tunele \"fid_tunele\" true true false 4 Long 0 10 ,First,#,$path_shp,FID_Tunele,-1,-1;objectid \"objectid\" true true false 4 Long 0 10 ,First,#,$path_shp,OBJECTID,-1,-1;objectid_1 \"objectid_1\" true true false 4 Long 0 10 ,First,#,$path_shp,OBJECTID_1,-1,-1;rol_v�a \"rol_v�a\" true true false 15 Text 0 0 ,First,#,$path_shp,Rol_V�a,-1,-1;nombre \"nombre\" true true false 40 Text 0 0 ,First,#,$path_shp,Nombre,-1,-1;largo \"largo\" true true false 8 Double 8 38 ,First,#,$path_shp,Largo,-1,-1;shape_stle \"shape_stle\" true true false 8 Double 8 38 ,First,#,$path_shp,SHAPE_STLe,-1,-1;shape_leng \"shape_leng\" true true false 8 Double 8 38 ,First,#,$path_shp,SHAPE_Leng,-1,-1;st_length(shape) \"st_length(shape)\" false false true 0 Double 0 0 ,First,#"
    ).substitute(path_shp=Tuneles_shp_intersect),
    ""
)

# Process: Incorporar (6)
arcpy.Append_management(
    Ubicaciones_de_APR_point_shp_intersect,
    wfs_mop_sde_Ubicaciones_de_APR_point,
    "NO_TEST",
    Template(
        "fid_comuna \"fid_comuna\" true true false 4 Long 0 10 ,First,#,$path_shp,FID_Comuna,-1,-1;region \"region\" true true false 60 Text 0 0 ,First,#,$path_shp,region,-1,-1;comuna \"comuna\" true true false 60 Text 0 0 ,First,#,$path_shp,comuna,-1,-1;provincia \"provincia\" true true false 60 Text 0 0 ,First,#,$path_shp,provincia,-1,-1;fid_ubicac \"fid_ubicac\" true true false 4 Long 0 10 ,First,#,$path_shp,FID_Ubicac,-1,-1;objectid \"objectid\" true true false 4 Long 0 10 ,First,#,$path_shp,OBJECTID,-1,-1;nombre \"nombre\" true true false 100 Text 0 0 ,First,#,$path_shp,Nombre,-1,-1"
    ).substitute(path_shp=Ubicaciones_de_APR_point_shp_intersect),
    ""
)
print 'Incorporacion de Datos exitosa'

ahora = datetime.now()
print ('Hora:',ahora.hour,ahora.minute,ahora.second)

print 'proceso terminado'

#-*- coding: utf-8 -*-

import arcpy
from string import Template

print 'Eliminando Registros Antiguos'

GDB_PATH = "E:\\scripts-arcgis\\sde\\PP_Estivales_G_Sectorial_214.sde"
#GDB_PATH = "E:\\scripts-arcgis\\sde\\PP_Estivales_G_Sectorial_197.sde"
FC_OBRAS = GDB_PATH + "\\pp_estivales_gsectorial.sde.Obras_MINVU_MOP"

arcpy.DeleteRows_management(FC_OBRAS)

print 'Registros Antiguos Eliminados'

print 'Incorpora Registros Nuevos'

input_tables = Template(
    "'$database_path\\pp_estivales_gsectorial.sde.Gestion_Sectorial_MINVU';'$database_path\\pp_estivales_gsectorial.sde.Gestion_sectorial_MOP'"
).substitute(database_path=GDB_PATH)

field_mapping_text = Template(
    "objectid_1 \"objectid_1\" true false false 4 Long 0 10 ,First,#,$database_path\\pp_estivales_gsectorial.sde.Gestion_Sectorial_MINVU,objectid_1,-1,-1,$database_path\\pp_estivales_gsectorial.sde.Gestion_sectorial_MOP,objectid_1,-1,-1;region \"region\" true false false 70 Text 0 0 ,First,#,$database_path\\pp_estivales_gsectorial.sde.Gestion_Sectorial_MINVU,region,-1,-1,$database_path\\PP_Estivales_G_Sectorial.sde\\pp_estivales_gsectorial.sde.Gestion_sectorial_MOP,region,-1,-1;provincia \"provincia\" true false false 70 Text 0 0 ,First,#,$database_path\\pp_estivales_gsectorial.sde.Gestion_Sectorial_MINVU,provincia,-1,-1,$database_path\\PP_Estivales_G_Sectorial.sde\\pp_estivales_gsectorial.sde.Gestion_sectorial_MOP,provincia,-1,-1;comuna \"comuna\" true false false 70 Text 0 0 ,First,#,$database_path\\pp_estivales_gsectorial.sde.Gestion_Sectorial_MINVU,comuna,-1,-1,$database_path\\PP_Estivales_G_Sectorial.sde\\pp_estivales_gsectorial.sde.Gestion_sectorial_MOP,comuna,-1,-1;sector \"sector\" true false false 500 Text 0 0 ,First,#,$database_path\\pp_estivales_gsectorial.sde.Gestion_Sectorial_MINVU,sector,-1,-1,$database_path\\PP_Estivales_G_Sectorial.sde\\pp_estivales_gsectorial.sde.Gestion_sectorial_MOP,sector,-1,-1;referencia \"referencia\" true true false 1000 Text 0 0 ,First,#,$database_path\\pp_estivales_gsectorial.sde.Gestion_Sectorial_MINVU,referencia,-1,-1,$database_path\\PP_Estivales_G_Sectorial.sde\\pp_estivales_gsectorial.sde.Gestion_sectorial_MOP,referencia,-1,-1;estado \"estado\" true true false 50 Text 0 0 ,First,#,$database_path\\pp_estivales_gsectorial.sde.Gestion_Sectorial_MINVU,estado,-1,-1,$database_path\\PP_Estivales_G_Sectorial.sde\\pp_estivales_gsectorial.sde.Gestion_sectorial_MOP,estado,-1,-1;estado_2020 \"estado_2020\" true true false 50 Text 0 0 ,First,#,$database_path\\pp_estivales_gsectorial.sde.Gestion_Sectorial_MINVU,estado_2020,-1,-1,$database_path\\PP_Estivales_G_Sectorial.sde\\pp_estivales_gsectorial.sde.Gestion_sectorial_MOP,estado_2020,-1,-1;plazo_ejecucion \"plazo_ejecucion\" true true false 50 Text 0 0 ,First,#,$database_path\\pp_estivales_gsectorial.sde.Gestion_Sectorial_MINVU,plazo_ejecucion,-1,-1,$database_path\\PP_Estivales_G_Sectorial.sde\\pp_estivales_gsectorial.sde.Gestion_sectorial_MOP,plazo_ejecucion,-1,-1;costo_estimado \"costo_estimado\" true true false 50 Text 0 0 ,First,#,$database_path\\pp_estivales_gsectorial.sde.Gestion_Sectorial_MINVU,costo_estimado,-1,-1,$database_path\\PP_Estivales_G_Sectorial.sde\\pp_estivales_gsectorial.sde.Gestion_sectorial_MOP,costo_estimado,-1,-1;responsable_obra \"responsable_obra\" true true false 100 Text 0 0 ,First,#,$database_path\\pp_estivales_gsectorial.sde.Gestion_Sectorial_MINVU,responsable_obra,-1,-1,$database_path\\PP_Estivales_G_Sectorial.sde\\pp_estivales_gsectorial.sde.Gestion_sectorial_MOP,responsable_obra,-1,-1;otra_inst_responsable \"otra_inst_responsable\" true true false 100 Text 0 0 ,First,#,$database_path\\pp_estivales_gsectorial.sde.Gestion_Sectorial_MINVU,otra_inst_responsable,-1,-1,$database_path\\PP_Estivales_G_Sectorial.sde\\pp_estivales_gsectorial.sde.Gestion_sectorial_MOP,otra_inst_responsable,-1,-1;nom_respo_info \"responsable_info\" true true false 100 Text 0 0 ,First,#,$database_path\\pp_estivales_gsectorial.sde.Gestion_Sectorial_MINVU,nom_respo_info,-1,-1,$database_path\\PP_Estivales_G_Sectorial.sde\\pp_estivales_gsectorial.sde.Gestion_sectorial_MOP,nom_respo_info,-1,-1;dependencia \"dependencia\" true true false 100 Text 0 0 ,First,#,$database_path\\pp_estivales_gsectorial.sde.Gestion_Sectorial_MINVU,dependencia,-1,-1,$database_path\\PP_Estivales_G_Sectorial.sde\\pp_estivales_gsectorial.sde.Gestion_sectorial_MOP,dependencia,-1,-1;correo \"correo\" true true false 100 Text 0 0 ,First,#,$database_path\\pp_estivales_gsectorial.sde.Gestion_Sectorial_MINVU,correo,-1,-1,$database_path\\PP_Estivales_G_Sectorial.sde\\pp_estivales_gsectorial.sde.Gestion_sectorial_MOP,correo,-1,-1;telefono \"telefono\" true true false 50 Text 0 0 ,First,#,$database_path\\pp_estivales_gsectorial.sde.Gestion_Sectorial_MINVU,telefono,-1,-1,$database_path\\PP_Estivales_G_Sectorial.sde\\pp_estivales_gsectorial.sde.Gestion_sectorial_MOP,telefono,-1,-1;latitud \"latitud\" true true false 50 Text 0 0 ,First,#,$database_path\\pp_estivales_gsectorial.sde.Gestion_Sectorial_MINVU,latitud,-1,-1,$database_path\\PP_Estivales_G_Sectorial.sde\\pp_estivales_gsectorial.sde.Gestion_sectorial_MOP,latitud,-1,-1;longitud \"longitud\" true true false 50 Text 0 0 ,First,#,$database_path\\pp_estivales_gsectorial.sde.Gestion_Sectorial_MINVU,longitud,-1,-1,$database_path\\PP_Estivales_G_Sectorial.sde\\pp_estivales_gsectorial.sde.Gestion_sectorial_MOP,longitud,-1,-1;tipo_obra \"tipo_obra\" true true false 50 Text 0 0 ,First,#,$database_path\\pp_estivales_gsectorial.sde.Gestion_Sectorial_MINVU,tipo_obra,-1,-1,$database_path\\PP_Estivales_G_Sectorial.sde\\pp_estivales_gsectorial.sde.Gestion_sectorial_MOP,tipo_obra,-1,-1;otro_tip_obra \"otro_tip_obra\" true true false 254 Text 0 0 ,First,#,$database_path\\pp_estivales_gsectorial.sde.Gestion_Sectorial_MINVU,otro_tip_obra,-1,-1,$database_path\\PP_Estivales_G_Sectorial.sde\\pp_estivales_gsectorial.sde.Gestion_sectorial_MOP,otro_tip_obra,-1,-1;globalid \"globalid\" false false false 38 GlobalID 0 0 ,First,#,$database_path\\pp_estivales_gsectorial.sde.Gestion_Sectorial_MINVU,globalid,-1,-1,$database_path\\pp_estivales_gsectorial.sde.Gestion_sectorial_MOP,globalid,-1,-1"
).substitute(database_path = GDB_PATH)

arcpy.Append_management(
    input_tables,
    target = FC_OBRAS,
    schema_type = "NO_TEST",
    field_mapping = field_mapping_text,
    subtype = ""
)

print 'Registros Nuevos Incorporados'
print 'Procesamiento Terminado'

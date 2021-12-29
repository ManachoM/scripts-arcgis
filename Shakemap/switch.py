# -*- coding: cp1252 -*-
import commands
import os
#import msvcrt

txt_file_path = 'E:\\scripts-arcgis\\Shakemap\\ejecutar.txt'
python_path = 'C:\\Python27\\ArcGISx6410.7\\python.exe'
shakemap_script_path = 'E:\\scripts-arcgis\\Shakemap\\Proceso_Publicacion_ShakeMap_SE.py'

archivo=open(txt_file_path)
leer=archivo.readline()
while leer == "1":
    os.system(
        '{} {}'.format(
            python_path,
            shakemap_script_path
        )
    )
    print 'ejecutado con exito'
    break
archivo=open(txt_file_path,'w')
escribir=archivo.write("0")
archivo.close()

#msvcrt.getch()

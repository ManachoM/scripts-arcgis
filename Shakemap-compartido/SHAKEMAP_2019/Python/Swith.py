# -*- coding: cp1252 -*-
import commands
import os
#import msvcrt

archivo=open('C:\sismologia\SHAKEMAP_ENTRADA\ejecutar.txt')
leer=archivo.readline()
while leer == "1":
    os.system('C:\Python27\ArcGIS10.3\python.exe C:\\Users\\Administrador\\Documents\\SHAKEMAP_2019\Python\Proceso_Publicación_ShakeMap_SE.py')
    print 'ejecutado con exito'
    break
archivo=open('C:\sismologia\SHAKEMAP_ENTRADA\ejecutar.txt','w')
escribir=archivo.write("0")	
archivo.close()

#msvcrt.getch()
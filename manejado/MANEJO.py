import json
import cv2
import os
import datetime
import pandas as pd
import csv
import numpy as np
def lectura(archivo):
    with open(archivo) as archivo_json:
        datos=json.load(archivo_json)
    with open('manejado/dec1.csv',newline='') as f:
        data=csv.reader(f,delimiter=',')
        temperaturas=list(data)
    return datos,temperaturas
def Carpeta_original(archivos):
    print(archivos,end='\n\n')
    for elm in archivos:
        if not '.' in elm:   
            ruta_imagenes=directorio+'\\'+elm
            return os.listdir(ruta_imagenes),ruta_imagenes
def rutas_carpetas_imagenes(carpetas):
    combo=[]
    for carpeta in carpetas:
        if '.' in carpeta:
            continue
        ruta_elementos_carpetas=ruta_madre+'\\'+carpeta
        imagenes_carpeta=nombre_elementos(ruta_elementos_carpetas)
        combo.append(imagenes_carpeta)
    return combo

def nombre_elementos(rutas):
    rutas_imagen=[]
    imagenes=os.listdir(rutas)
    for imagen in imagenes:
        rutas_imagenes=rutas+'\\'+imagen
        rutas_imagen.append(rutas_imagenes)
    return rutas_imagen
def agregado(base,imagenes,temperatura):
    inicializado='1/1/2023'
    cont=-1
    for mediciones in imagenes:
        cont+=1
        fecha_inicial=datetime.datetime.strptime(inicializado,'%d/%m/%Y')
        dia=datetime.timedelta(days=cont)
        fecha_actual=fecha_inicial+dia
        formato=datetime.datetime.strftime(fecha_actual,'%d/%m/%Y')
        if all(float(i)==0 for i in temperatura[cont+1][1:len(temperatura)-1]):
            base['Maquina_1']['fechas'][formato]={'Nombre':temperatura[cont+1][0],'Rango de Temperatura': 0, 'Directorio':mediciones}
        else:
            temperatura_mas_alta=temperatura[cont+1][1:].index(max(temperatura[cont+1][1:]))
            base['Maquina_1']['fechas'][formato]={'Nombre':temperatura[cont+1][0],'Rango de Temperatura': temperatura[0][temperatura_mas_alta+1], 'Directorio':mediciones,}
    return base
def cargado(archivo):
    with open ('manejado/base_de_datos.json','w') as dicc:
        json.dump(base,dicc,indent=4)
        print("Exportado")     
def apertura_dataframe(base):
    data=pd.DataFrame.from_dict(base['Maquina_1']['fechas'],orient='index')
    print(data.head(45))
    return data
def movimiento_en_general(directorio_general,imagenes):
    ruta_interfaz=directorio_general+'\\Grafica2\\static\\'
    rutas_llegada=[]
    for carpeta in imagenes:
        for ruta in carpeta:
            lista_ruta=ruta.split('\\')
            ruta_de_llegada=ruta_interfaz+lista_ruta[-1]
            rutas_llegada.append(ruta_de_llegada)
            imagen=cv2.imread(ruta)
            cv2.imwrite(ruta_de_llegada,imagen)
    print('Movimiento Exitoso')
    return rutas_llegada
def criterio_de_recorte():
    pass
base,temperatura=lectura('manejado/base_de_datos.json')
directorio_general=os.getcwd()
directorio=directorio_general+'\\'+'manejado'
carpetas,ruta_madre=Carpeta_original(os.listdir(directorio))
imagenes=rutas_carpetas_imagenes(carpetas)
rutas_estaticas=movimiento_en_general(directorio_general,imagenes)
archivito=agregado(base,rutas_estaticas,temperatura)
cargado(archivito)
dataframe=apertura_dataframe(base).dropna()
print(dataframe)
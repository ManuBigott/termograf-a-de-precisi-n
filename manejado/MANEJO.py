import json
import cv2
import os

def lectura(archivo):
    with open(archivo) as archivo_json:
        datos=json.load(archivo_json)
        return datos
        print(datos['Maquina_1']['fechas']['10-11-2024']['imagen'])
def Carpeta_original(archivos):
    carpetas_imagenes=archivos[-1]
    ruta=os.path.abspath(carpetas_imagenes)
    return os.listdir(carpetas_imagenes),ruta
def rutas_carpetas_imagenes(carpetas):
    imgagenes=[]
    for carpeta in carpetas:
        if '.' in carpeta:
            continue
        ruta_elementos_carpetas=ruta_madre+'/'+carpeta
        imagenes_carpeta=nombre_elementos(ruta_elementos_carpetas)
        imgagenes.append(imagenes_carpeta)
        print(imgagenes,end='\n\n')
    return imgagenes
def nombre_elementos(rutas):
    imagenes=os.listdir(rutas)
    for imagen in imagenes:
        rutas_imagenes=rutas+'/'+imagen
    return rutas_imagenes
def muestreo(imagenes):
    for entrada in imagenes:
        for file in entrada:
            imagen=cv2.imread(file)
            cv2.imshow(imagen,mat=10)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        break    
lectura('base_de_datos')
carpetas,ruta_madre=Carpeta_original(os.listdir())
imagenes=rutas_carpetas_imagenes(carpetas)
muestreo(imagenes)

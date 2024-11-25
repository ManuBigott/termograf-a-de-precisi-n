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
    combo=[]
    for carpeta in carpetas:
        if '.' in carpeta:
            continue
        ruta_elementos_carpetas=ruta_madre+'/'+carpeta
        imagenes_carpeta=nombre_elementos(ruta_elementos_carpetas)
        combo.append(imagenes_carpeta)
        print(combo,end='\n\n') 
    return combo
def nombre_elementos(rutas):
    rutas_imagen=[]
    imagenes=os.listdir(rutas)
    for imagen in imagenes:
        rutas_imagenes=rutas+'/'+imagen
        rutas_imagen.append(rutas_imagenes)
    return rutas_imagen
def muestreo(imagenes):
    print(imagenes,end='\n\n') 
    for entrada in imagenes:
        for visual in entrada:
            imagen=cv2.imread(visual)
            cv2.imshow("Imagen",imagen)
            cv2.waitKey(0)
        cv2.destroyAllWindows()
lectura('base_de_datos')
carpetas,ruta_madre=Carpeta_original(os.listdir())
print(carpetas)
imagenes=rutas_carpetas_imagenes(carpetas)
#muestreo(imagenes)

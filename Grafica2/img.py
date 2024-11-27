from flask import Flask, render_template, request, jsonify, redirect, url_for
import json
import matplotlib.pyplot as plt
import base64
import io
from datetime import datetime
import cv2
import numpy as np
app = Flask(__name__)
#hola carlota
#probando git
def cargar_base_de_datos():
    """Cargar la base de datos inicial"""
    try:
        with open('base_de_datos.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}
data = cargar_base_de_datos()
@app.route('/ver_imagen', methods=['GET'])
def ver_imagen():
    maquina = request.args.get('maquina')
    fecha = request.args.get('fecha')

    if not all([maquina, fecha]):
        return jsonify({'message': 'Máquina y fecha son requeridas'}), 400

    maquina_data = data.get(maquina, {})
    imagen_data = maquina_data.get('fechas', {}).get(fecha, {})
    especificaciones = maquina_data.get('Especificaciones', {})

    if not imagen_data:
        return jsonify({'message': 'Imagen no encontrada'}), 404

    ruta_imagen = imagen_data.get('imagen')

    return render_template('ver_imagen.html', ruta_imagen=ruta_imagen, imagen_data=imagen_data, maquina=maquina, fecha=fecha, especificaciones=especificaciones)
@app.route('/seleccionar_imagen', methods=['GET'])
def seleccionar_imagen():
    """Renderiza la página para seleccionar la imagen a procesar"""
    return render_template('seleccionar_imagen.html', data=data)

def escalador(ruta):
    Azul_oscuroL, Azul_oscuroH = np.array([120, 50, 50], np.uint8), np.array([130, 255, 255], np.uint8)
    AzulL, AzulH = np.array([180, 50, 50], np.uint8), np.array([190, 255, 255], np.uint8)
    CianL, CianH = np.array([75, 50, 50], np.uint8), np.array([85, 255, 255], np.uint8)
    VerdeL, VerdeH = np.array([60, 50, 50], np.uint8), np.array([70, 255, 255], np.uint8)
    AmarilloL, AmarilloH = np.array([30, 50, 50], np.uint8), np.array([40, 255, 255], np.uint8)
    NaranjaL, NaranjaH = np.array([15, 50, 50], np.uint8), np.array([25, 255, 255], np.uint8)
    RojoL, RojoH = np.array([0, 50, 50], np.uint8), np.array([10, 255, 255], np.uint8)
    Rojo_intensoL, Rojo_intensoH = np.array([120, 50, 50], np.uint8), np.array([130, 255, 255], np.uint8)

    img = cv2.imread(ruta, -1)
    if img is None:
        print('No se pudo leer la imagen desde la ruta:', ruta)
        return {'error': 'No se pudo leer la imagen'}
    print('Imagen leída correctamente')

    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    print('Conversión a HSV realizada')

    mask = cv2.inRange(hsv, RojoL, RojoH)
    mask1 = cv2.inRange(hsv, AmarilloL, AmarilloH)
    mask2 = cv2.inRange(hsv, CianL, CianH)
    T = mask.shape
    print(f'Tamaño de la máscara: {T}')
    lista = []
    lista1 = []
    lista2 = []

    for i in mask:
        lista += list(i)
    for i in mask1:
        lista1 += list(i)
    for i in mask2:
        lista2 += list(i)

    a1 = 0
    b1 = 0
    c1 = 0
    for i in lista:
        if int(i) == 0:
            a1 += 1

    for i in lista1:
        if int(i) == 0:
            b1 += 1

    for i in lista2:
        if int(i) == 0:
            c1 += 1

    a = T[0] * T[1] - a1
    b = T[0] * T[1] - b1
    c = T[0] * T[1] - c1

    analizado = ((a + b + c) / (T[0] * T[1])) * 100
    print(f'Valor de analizado: {analizado}')
    if analizado == 0:
        print('Error en el cálculo del valor analizado')

    return {
        "40_50": (a / (a + b + c)) * 100,
        "20_30": (b / (a + b + c)) * 100,
        "0_10": (c / (a + b + c)) * 100,
        "analizado": analizado
    }

    
# Nueva ruta para procesar una imagen y obtener los resultados del análisis
@app.route('/procesar_imagen', methods=['GET'])
def procesar_imagen():
    maquina = request.args.get('maquina')
    fecha = request.args.get('fecha')
    print(f'Recibidos: maquina={maquina}, fecha={fecha}')  # Depuración

    if not all([maquina, fecha]):
        print('Error: Máquina y fecha son requeridas')  # Depuración
        return jsonify({'message': 'Máquina y fecha son requeridas'}), 400

    maquina_data = data.get(maquina, {})
    imagen_data = maquina_data.get('fechas', {}).get(fecha, {})
    print(f'Datos obtenidos: maquina_data={maquina_data}, imagen_data={imagen_data}')  # Depuración

    if not imagen_data:
        print('Error: Imagen no encontrada')  # Depuración
        return jsonify({'message': 'Imagen no encontrada'}), 404

    ruta_imagen = imagen_data.get('imagen')
    print(f'Ruta de la imagen: {ruta_imagen}')  # Depuración

    resultados = escalador(ruta_imagen)
    print(f'Resultados del escalador: {resultados}')  # Depuración

    if 'analizado' not in resultados:
        print('Error: Clave "analizado" no encontrada en los resultados')  # Depuración
        return jsonify({'message': 'Error en el procesamiento de la imagen. Verifica la ruta proporcionada.'}), 500

    if resultados["analizado"] == 0:
        print('Error: Valor de "analizado" es 0')  # Depuración
        return jsonify({'message': 'Error en el procesamiento de la imagen. Verifica la ruta proporcionada.'}), 500

    return render_template('procesar_imagen.html', resultados=resultados)

@app.errorhandler(404)
def page_not_found(e):
    """Manejar errores 404"""
    return render_template('error.html', mensaje="Página no encontrada"), 404
@app.errorhandler(500)
def internal_error(e):
    """Manejar errores 500"""
    return render_template('error.html', mensaje="Error interno del servidor"), 500
@app.route('/')
def menu():
    """Renderiza el menú principal"""
    return render_template('menu.html')
@app.route('/ver_maquinas', methods=['GET'])
def ver_maquinas():
    """Renderiza la página con los datos de las máquinas"""
    return render_template('index.html', data=data)

@app.route('/agregar_imagen', methods=['POST', 'GET'])
def agregar_imagen():
    if request.method == 'GET':
        return render_template('agregar_imagen.html')
    
    maquina = request.form.get('maquina')
    fecha = request.form.get('fecha')  # Fecha en formato día/mes/año
    ruta_imagen = request.files.get('ruta_imagen')
    temperatura_maquina = request.form.get('temperatura_maquina')
    temperatura_ambiente = request.form.get('temperatura_ambiente')
    especificaciones = request.form.get('especificaciones')

    if not all([maquina, fecha, ruta_imagen, temperatura_maquina, temperatura_ambiente]):
        return jsonify({'message': 'Todos los campos son requeridos'}), 400

    # Verificar la existencia de la carpeta 'static'
    import os
    if not os.path.exists('static'):
        os.makedirs('static')

    # Guardar la imagen en la carpeta 'static'
    try:
        ruta_imagen.save(f'static/{ruta_imagen.filename}')
    except Exception as e:
        print(f'Error guardando la imagen: {e}')
        return jsonify({'message': f'Error guardando la imagen: {e}'}), 500

    # Actualizar la ruta de la imagen para que apunte a la carpeta 'static'
    ruta_imagen_path = f'static/{ruta_imagen.filename}'
    print(f'Imagen guardada en: {ruta_imagen_path}')  # Depuración

    # Convertir la fecha a un objeto datetime para garantizar el formato correcto
    try:
        fecha_obj = datetime.strptime(fecha, '%d/%m/%Y')
        fecha_str = fecha_obj.strftime('%d/%m/%Y')
    except ValueError:
        return jsonify({'message': 'Formato de fecha inválido. Use día/mes/año.'}), 400

    # Obtener o crear la entrada de la máquina
    maquina_data = data.setdefault(maquina, {'Especificaciones': {}, 'fechas': {}})
    
    # Actualizar las especificaciones si se proporcionaron
    if especificaciones:
        maquina_data['Especificaciones'] = especificaciones

    # Agregar los datos de la imagen y las temperaturas
    maquina_data['fechas'][fecha_str] = {
        'imagen': ruta_imagen_path,
        'temperatura_maquina': int(temperatura_maquina),
        'temperatura_ambiente': int(temperatura_ambiente)
    }

    # Guardar la base de datos actualizada
    with open('base_de_datos.json', 'w') as f:
        json.dump(data, f, indent=4)

    return jsonify({'message': 'Datos agregados exitosamente'})

@app.route('/editar_maquina/<maquina>', methods=['GET', 'POST'])
def editar_maquina(maquina):
    """Maneja la edición de datos de una máquina específica"""
    if request.method == 'GET':
        maquina_data = data.get(maquina, {})
        especificaciones = maquina_data.get('Especificaciones', {})
        return render_template('editar_maquina.html', maquina=maquina, data=maquina_data, especificaciones=especificaciones)
    
    fecha = request.form.get('fecha')  # Fecha en formato día/mes/año
    nueva_imagen = request.form.get('ruta_imagen')
    nueva_temperatura_maquina = request.form.get('temperatura_maquina')
    nueva_temperatura_ambiente = request.form.get('temperatura_ambiente')
    nuevas_especificaciones = request.form.get('especificaciones')

    if not all([fecha, nueva_imagen, nueva_temperatura_maquina, nueva_temperatura_ambiente, nuevas_especificaciones]):
        return jsonify({'message': 'Todos los campos son requeridos'}), 400

    # Convertir la fecha a un objeto datetime para garantizar el formato correcto
    try:
        fecha_obj = datetime.strptime(fecha, '%d/%m/%Y')
        fecha_str = fecha_obj.strftime('%d/%m/%Y')
    except ValueError:
        return jsonify({'message': 'Formato de fecha inválido. Use día/mes/año.'}), 400

    # Obtener o crear la entrada de la máquina
    maquina_data = data.setdefault(maquina, {'Especificaciones': {}, 'fechas': {}})
    fechas = maquina_data['fechas']

    if fecha_str not in fechas:
        return jsonify({'message': 'Fecha no encontrada'}), 404

    # Actualizar los datos de la imagen y las temperaturas
    fechas[fecha_str] = {
        'imagen': nueva_imagen,
        'temperatura_maquina': int(nueva_temperatura_maquina),
        'temperatura_ambiente': int(nueva_temperatura_ambiente)
    }

    # Actualizar las especificaciones si se proporcionaron
    if nuevas_especificaciones:
        maquina_data['Especificaciones'] = nuevas_especificaciones

    # Guardar la base de datos actualizada
    with open('base_de_datos.json', 'w') as f:
        json.dump(data, f, indent=4)

    return jsonify({'message': 'Datos de la máquina actualizados exitosamente'})

@app.route('/graficar_temperaturas', methods=['GET'])
def graficar_temperaturas():
    """Genera y muestra una gráfica de temperaturas"""
    maquina = request.args.get('maquina')
    if not maquina:
        return jsonify({'message': 'Máquina es requerida'}), 400

    maquina_data = data.get(maquina, {})
    fechas = maquina_data.get('fechas', {})

    if not fechas:
        return jsonify({'message': 'No hay datos de fechas disponibles para la máquina'}), 404

    fechas_ordenadas = sorted(fechas.keys(), key=lambda x: datetime.strptime(x, '%d/%m/%Y'))
    
    try:
        temperaturas_maquina = [fechas[fecha]['temperatura_maquina'] for fecha in fechas_ordenadas]
        temperaturas_ambiente = [fechas[fecha]['temperatura_ambiente'] for fecha in fechas_ordenadas]
    except KeyError as e:
        return jsonify({'message': f'Error en los datos: {e}'}), 500

    plt.figure()
    plt.plot(fechas_ordenadas, temperaturas_maquina, label='Temperatura Máquina')
    plt.plot(fechas_ordenadas, temperaturas_ambiente, label='Temperatura Ambiente')
    plt.xlabel('Fecha')
    plt.ylabel('Temperatura')
    plt.title(f'Temperaturas de la {maquina}')
    plt.legend()

    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    graph_url = base64.b64encode(img.getvalue()).decode()

    plt.close()

    return render_template('grafica.html', graph_url=graph_url)
@app.route('/seleccionar_maquina_editar', methods=['GET'])
def seleccionar_maquina_editar():
    """Renderiza la página para seleccionar la máquina a editar"""
    return render_template('seleccionar_maquina_editar.html', data=data)
if __name__ == '__main__':
    app.run(debug=True)


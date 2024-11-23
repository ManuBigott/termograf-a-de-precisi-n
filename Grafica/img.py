from flask import Flask, render_template, request, jsonify
import json


app = Flask(__name__)


def cargar_base_de_datos():
    try:
       with open('base_de_datos.json', 'r') as f:
           return json.load(f)
    except FileNotFoundError:
        return {}

data = cargar_base_de_datos()

@app.route('/')
def index():
    return render_template('index.html', data=data)

@app.route('/agregar_imagen', methods=['POST'])
def agregar_imagen():
    maquina = request.form.get('maquina')
    fecha = request.form.get('fecha')
    ruta_imagen = request.form.get('ruta_imagen')
    temperatura_maquina = request.form.get('temperatura_maquina')
    temperatura_ambiente = request.form.get('temperatura_ambiente')

    if not maquina or not fecha or not ruta_imagen or not temperatura_maquina or not temperatura_ambiente:
        return jsonify({'message': 'Todos los campos son requeridos'}), 400

    
    maquina_data = data.get(maquina, {})
    fechas = maquina_data.setdefault('fechas', {})
    fechas[fecha] = {
        'imagen': ruta_imagen,
        'temperatura_maquina': int(temperatura_maquina),
        'temperatura_ambiente': int(temperatura_ambiente)
    }

    data[maquina] = maquina_data

    
    with open('base_de_datos.json', 'w') as f:
        json.dump(data, f, indent=4)

    return jsonify({'message': 'Imagen agregada exitosamente'})

@app.route('/ver_imagen', methods=['POST'])
def ver_imagen():
    maquina = request.form.get('maquina')
    fecha = request.form.get('fecha')

    if not maquina or not fecha:
        return jsonify({'message': 'Máquina y fecha son requeridas'}), 400

  
    maquina_data = data.get(maquina, {})
    imagen_data = maquina_data.get('fechas', {}).get(fecha, {})

    if not imagen_data:
        return jsonify({'message': 'Imagen no encontrada'}), 404

    ruta_imagen = imagen_data.get('imagen')

    
    return render_template('imagen.html', ruta_imagen=ruta_imagen, imagen_data=imagen_data, maquina=maquina, fecha=fecha)

if __name__ == '__main__':
    app.run(debug=True)

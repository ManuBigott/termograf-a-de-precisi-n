 # Termografía de Precisión 
![termonota-2-enero-24](https://github.com/user-attachments/assets/71dca2aa-c448-471c-8147-6c414b24f11f)

### Descripción del Proyecto

El proyecto tiene como objetivo automatizar un sistema que se realiza manualmente por parte de un termógrafo, para hacer que la recopilación de datos mediante imágenes tomadas en distintos periodos de tiempo sea realizada de manera más eficiente a la hora de guardar y analizar dichos datos e imágenes para luego clasificarlos y saber el funcionamiento optimo con las imágenes relacionadas a la maquinaria utilizada.

### Funcionalidades del Proyecto
- Recopilación de datos e imágenes termográficas sobre motores eléctricos, especificaciones y la temperatura optima a la que funcionan. Principalmente recopilación de imágenes es lo que permite tener una base de datos concisa. 

- Preprocesamiento de datos, Limpieza y organización de los datos, manejar valores sobre la temperatura mediante una escala de colores.

- Luego la imagen y los datos recopilados son guardados en la base de datos.

- Reporta un mensaje sobre cómo debería funcionar de manera óptima y una alerta si pasa los valores permitidos. Junto con posibles reportes sobre el fenómeno que se esta dando.

- Grafica sobre la temperatura que varía a lo largo del tempo con las imágenes del motor tomadas en distintos periodos de tiempo.


### Avance General

Se ha desarrollado toda la rama de procesamiento de imágenes obteniendo así funciones importatntes que otorgan información crucial de la imagen. Las herramientas de trabajo como la interfaz gráfica se ha desarrollado de manera eficiente y con la simplicidad necesaria adaptándolas a las necesidades del procesamiento y muestreo de imagenes termográficas.
La base de datos se ha organizado y estructurado de manera eficiente y se ha logrado un b uen orden en términos generales.

### Objetivos alcanzados

- Procesamiento y obtención de información a partir de imágenes termográficas exitosa
- Procesamiento rápido a partir de algoritmo algoritmos de búsqueda secuencial
- Recorte imágenes para mejor resolución
- A partir del algoritmo de búsqueda secuencial se generan también base de datos o estructuras de datos necesario para el preprocesado
- Ordenamiento y depuración de base de datos exitos

### Recursos Utilizados
Se utilizaron las siguientes librerías:
- Datetime: La librería datetime en Python es un módulo que proporciona clases para manipular fechas y horas. Incluye los tipos de datos date, time y datetime, que pueden usarse para representar y operar con fechas y horas. Permite realizar operaciones aritméticas con estos tipos, facilitando el manejo de la información temporal en Python.
- Json: Es un formato de texto ligero y de fácil lectura que se utiliza comúnmente para transmitir datos entre sistemas y aplicaciones.
- Matplotlib: Sirve para crear visualizaciones de datos en dos dimensiones. Con ella, se puede generar una gran variedad de gráficos.
- Numpy: Esta especialmente diseñada para realizar cálculos numéricos y trabajar con grandes conjuntos de datos.
- OpenCV: Ofrece una amplia gama de funciones y algoritmos para procesar imágenes y videos.
- OS Module: Esta librería  proporciona una manera de interactuar con el sistema operativo en el que se está trabajando.
- Pandas: :  Esta diseñada específicamente para la manipulación y análisis de datos.
- CSV: Es una herramienta esencial para trabajar con datos tabulares en formato CSV.
- IO Module: Este proporciona herramientas fundamentales para trabajar con diferentes tipos de entrada y salida (I/O), es decir, para manejar la lectura y escritura de datos.
- Base 64: Este formato es especialmente útil cuando se necesita transmitir o almacenar datos binarios (como imágenes, archivos, etc.) en medios que solo admiten texto.
- Flask: Es un microframework web para Python que te permite crear aplicaciones web de forma rápida y sencilla.

También se ha utilizado base de datos de imágenes para el entrenamiento y aplicación de dichas funciones
### Problemas encontrados
- Escasez a niveles de imágenes para el preprocesado.
- A falta de la herramienta para captar imágenes termográfica faltarían algunos datos de suma importancia para el análisis.
- Entre estos datos serían la temperatura ambiente y temperaturas específicas, de igual manera no afectaría tanto pero a futuro para mejorar la precisión serían imprescindibles.

##### Miembros Desarrolladores del proyecto:
- Alexander Alvarado
- Harold Angarita
- Nicanor Hermoso
- Manuel Morales
- Giovanni Omogrosso
- Gabriel Torrealba

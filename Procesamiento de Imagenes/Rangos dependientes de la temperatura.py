import numpy as np

def rangos_color_temperatura(temperatura):
    """
    Define rangos de color HSV aproximados según la temperatura.

    Args:
        temperatura: Temperatura en grados Celsius.

    Returns:
        Tupla con los valores bajo y alto de HSV para el rango de color.
    """

    if temperatura <= 0:
        # Colores fríos (azules, violetas)
        bajo = np.array([240, 100, 50], np.uint8)
        alto = np.array([300, 255, 255], np.uint8)
    elif temperatura <= 20:
        # Colores fríos (azules, verdes)
        bajo = np.array([180, 100, 50], np.uint8)
        alto = np.array([240, 255, 255], np.uint8)
    elif temperatura <= 40:
        # Colores cálidos (amarillos, verdes)
        bajo = np.array([60, 100, 50], np.uint8)
        alto = np.array([180, 255, 255], np.uint8)
    else:
        # Colores muy cálidos (rojos, naranjas)
        bajo = np.array([0, 100, 50], np.uint8)
        alto = np.array([60, 255, 255], np.uint8)

    return bajo, alto

# Ejemplo de uso:
temperatura = 30
bajo, alto = rangos_color_temperatura(temperatura)
print("Rango de color para", temperatura, "°C:")
print("Bajo:", bajo)
print("Alto:", alto)

Azul_oscuroL,Azul_oscuroH = np.array([120,50,50],np.uint8) , np.array([130,255,255],np.uint8)
AzulL,AzulH = np.array([180,50,50],np.uint8),np.array([190,255,255],np.uint8)
CianL,CianH = np.array([75,50,50],np.uint8),np.array([85,255,255],np.uint8)
VerdeL,VerdeH = np.array([60,50,50],np.uint8),np.array([70,255,255],np.uint8)
AmarilloL,AmarilloH = np.array([30,50,50],np.uint8),np.array([40,255,255],np.uint8)
NaranjaL,NaranjaH = np.array([15,50,50],np.uint8),np.array([25,255,255],np.uint8)
RojoL,RojoH = np.array([0,50,50],np.uint8),np.array([10,255,255],np.uint8)
Rojo_intensoL,Rojo_intensoH = np.array([120,50,50],np.uint8),np.array([130,255,255],np.uint8)


import numpy as np

# Definimos la función de Himmelblau
def himmelblau(x, y):
    return (x**2 + y - 11)**2 + (x + y**2 - 7)**2

# Rango de búsqueda para x e y
x_vals = np.linspace(-5, 5, 1000) #Se usa linspace para generar 1000 puntos equidistantes entre -5 y 5
y_vals = np.linspace(-5, 5, 1000) #Crea un arreglo de 1000 numeros, comenzando en -5 y terminando en 5

# Inicializamos el valor mínimo y las coordenadas correspondientes
min_value = float('inf')
min_coords = (None, None)

# Realizamos una búsqueda por grilla
for x in x_vals:
    for y in y_vals:
        value = himmelblau(x, y)
        if value < min_value:
            min_value = value
            min_coords = (x, y)

# Mostramos los resultados
print(f"Valores mínimos de (x, y): {min_coords}")
print(f"Valor mínimo de la función: {min_value}")

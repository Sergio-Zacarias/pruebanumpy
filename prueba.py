import numpy as np

# print("¡NumPy funciona perfectamente!")
# print("Versión instalada:", np.__version__)

# 1. Crear un arreglo de 1D
# mi_array = np.array([10, 20, 30, 40, 50])
# print("--- Arreglo Básico ---")
# print("Array original:", mi_array)
# print("Forma (shape):", mi_array.shape)

# # 2. Operaciones matemáticas directas (Vectorización)
# print("\n--- Operaciones Matemáticas ---")
# print("Sumar 5 a cada elemento:", mi_array + 5)
# print("Multiplicar por 2:", mi_array * 2)

# 3. Crear un arreglo desde listas o tulplas
# Crear Arreglo desde Lista     
# lista = [1,2,3,4,5]
# arrglo1 = np.array(lista)
# print("Arreglo desde lista:", arrglo1)

# Crear Arreglo desde Tupla
# tupla = (7,8,9,10)
# arreglo2 = np.array(tupla)
# print("Arreglo desde una tupla: ", arreglo2)

# Crear Array 2D (matriz)
# lista_delista = [[1,2,3], [7,8,5]]
# matriz = np.array(lista_delista)
# print(f"Matriz 2D: \n {matriz}")

# Funciones para crear arreglos
# np.arange(start, stop, step) el step se puede omitir y por defecto es 1
# y el stop no se incluye en el arreglo 
# arr = np.arange(0,10,2)
# print("np.arange", arr)

# np.linspace(start, stop, num)
# Genera un array con una cantidad fija de elementos, distribuidos
# de forma equidistante entre un  valor inicial y uno final.
# arr = np.linspace(0, 1, 5) # en este caso si se imprime el valor final(stop)
# print("np.linspace:", arr)

#  np.zeros(shape)
# Crea un array lleno de ceros.
# arr = np.zeros((2, 3))  # 2 filas, 3 columnas

# np.ones(shape)
# Crea un array lleno de unos.
# arr = np.ones((3, 3))
# print("np.ones:\n", arr)

# np.eye(n)
# Genera una matriz identidad de tamaño n × n, con unos en la diagonal
#  principal y ceros en el resto.
# arr = np.eye(4)
# print("np.eye:\n", arr)
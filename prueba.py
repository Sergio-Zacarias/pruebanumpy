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

# Dimensiones (ndim) Indica cuántas dimensiones tiene el array:
# a = np.array([1,2,3])
# print("Una dimension",a.ndim)
# b = np.array([[1,2,3], [4,5,6]])
# print("Dos dimensiones", b.ndim)
# c = np.array([[[1],[2]],[[4],[5]]])
# print("Tres dimensiones", c.ndim)

# Forma (shape) Devuelve una tupla con la cantidad de elementos por dimensión.
# a = np.array([1,2,3])
# print("Forma de a:", a.shape)  # (3,) significa que es un vector plano de 3 elementos en linea recta
# b = np.array([[1,2,3], [4,5,6]])
# print("Forma de b:", b.shape)  # (2, 3) 2 filas y 3 columnas
# c = np.array([[[1],[2]],[[4],[5]]])
# print("Forma de c:", c.shape)  # (2, 2, 1) 2 bloques, 2 filas y 1 columna

# Tamaño (size) Indica la cantidad total de elementos del array
# a = np.array([1,2,3])
# print("Tamaño de a:", a.size)  # 3 elementos          

# Tipo de datos (dtype) Los arrays son homogéneos: todos los elementos comparten el mismo tipo.
# arr = np.array([1, 2, 3])
# print("Tipo de datos:", arr.dtype)  # int64 
# Si mezclás tipos, NumPy intenta unificarlos automáticamente:
# arr = np.array([1, 2, 3.5])
# print("Tipo de datos:", arr.dtype)  # float64

# Conversión de tipos (astype)
# Podemos forzar el tipo de un array usando .astype().
# arr = np.array([1, 2, 3, 4])
# print("Original:", arr, arr.dtype)
#  Convertir a float
# arr_float = arr.astype(float)
# print("Convertido a float:", arr_float, arr_float.dtype)
# # Convertir a string
# arr_str = arr.astype(str)
# print("Convertido a string:", arr_str, arr_str.dtype)

# Indexación y slicing
# NumPy permite acceder a porciones de un array de forma similar a las listas de Python, pero con 
# mayor poder expresivo.
# Indexación en 1D
# arr = np.array([10, 20, 30, 40, 50])
# print(arr[0])    # Primer elemento -> 10
# print(arr[-1])   # Último elemento -> 50

# #Slicing en 1D
# print(arr[1:4])   # Elementos de índice 1 a 3 -> [20 30 40]
# print(arr[:3])    # Primeros 3 -> [10 20 30]
# print(arr[::2])   # Cada 2 elementos -> [10 30 50]

# # Indexación en 2D
# # En arrays de dos dimensiones se usa la notación [fila, columna].
# mat = np.array([[1, 2, 3],
#                 [4, 5, 6],
#                 [7, 8, 9],
#                 [10, 11, 12]])
# print(mat[0, 0])   # Esquina superior izquierda -> 1
# print(mat[1, 2])   # Fila 1, columna 2 -> 6
# print(mat[-1, -1]) # Último elemento -> 9

#Slicing en 2D
# mat = np.array([[1, 2, 3],
#                 [4, 5, 6],
#                 [7, 8, 9],
#                 [10, 11, 12]])
# print(mat[2:4, 1:3])

# Indexación y slicing en ND
# En arrays con más dimensiones se agregan más índices separados por comas.
# arr3d = np.array([[[1, 2], [3, 4]],
#                   [[5, 6], [7, 8]]])
# # print(arr3d[0, 1, 1]) # Primer bloque, segunda fila, segunda columna -> 4
# print(arr3d[1, 1:2, 0:2]) # [7 8]
# print(arr3d[1, :, :]) # Segundo bloque completo -> [[5 6] [7 8]]
import numpy as np
# Operaciones básicas con Arrays
# arr1 = np.array([1,2,3])
# arr2 = np.array([7,15,13])
# print("Suma de arrays: ", arr1 + arr2)
# print("Resta de arrays: ", arr1 - arr2)
# print("Multiplicación de arrays: ", arr1 * arr2)
# print("División de arrays: ", arr1 / arr2)

# Broadcasting en NumPy
# El broadcasting permite operar entre arrays de diferentes tamaños o formas, siempre que se
# cumplan reglas específicas
#sumar un escalar a un array
# arr = np.array([1, 2, 3, 4])
# print(arr + 5) 
# operaciones entre un array 2D y uno 1D
# mat = np.array([[1, 2, 3],
#                 [4, 5, 6]])
# vec = np.array([10, 20, 30]) # NumPy expande el array más pequeño para que coincida en dimensiones con el mayor
# print(mat + vec)

# Funciones matemáticas comunes
# NumPy incluye funciones que operan elemento a elemento (ufuncs, universal functions).
# Raíz cuadrada ( np.sqrt )
# arr = np.array([1, 4, 9, 16])
# print("Raíz cuadrada:", np.sqrt(arr)) 

# Exponencial ( np.exp )
# arr = np.array([0, 1, 2])
# print("Exponencial:", np.exp(arr)) 

# Logaritmo natural ( np.log )
# arr = np.array([1, np.e, np.e**2])
# print("Logaritmo natural:", np.log(arr)) 

# Funciones trigonométricas ( np.sin , np.cos )
# arr = np.array([0, np.pi/2, np.pi])
# print("Seno:", np.sin(arr)) 
# print("Coseno:", np.cos(arr)) 

# reshape : cambiar la forma de un array
# arr = np.arange(12) # Array de 0 a 11
# print("Array original:\n", arr)
# mat = arr.reshape(3, 4) # 3 filas, 4 columnas
# print("Array con reshape (3x4):\n", mat)
# Podemos usar -1 para que NumPy calcule automáticamente una dimensión
# mat = arr.reshape(-1, 6) # NumPy ajusta la cantidad de filas
# print(mat)

# Concatenación de arrays
# a = np.array([1, 2, 3])
# b = np.array([4, 5, 6])
# c = np.concatenate([a, b])
# print("Concatenación:", c)

# Apilamiento horizontal ( np.hstack )
# a = np.array([[1, 2], [3, 4]])
# b = np.array([[5, 6], [7, 8]])
# c = np.hstack((a, b))
# print("Apilamiento horizontal:\n", c)

# Apilamiento vertical ( np.vstack )
# c = np.vstack((a, b))
# print("Apilamiento vertical:\n", c)

# División de arrays ( split )
# Podemos dividir un array en sub-arrays con np.split y funciones relacionadas
# División en 1D
# arr = np.arange(10)
# dividido = np.split(arr, 2)
# print("División en 2 partes:", dividido)

# División en 2D
# mat = np.arange(16).reshape(4, 4)
# print("Matriz original:\n", mat)
# # Dividir en 2 bloques horizontales
# print("División vertical:\n", np.vsplit(mat, 2))
# # Dividir en 2 bloques verticales
# print("División horizontal:\n", np.hsplit(mat, 2))

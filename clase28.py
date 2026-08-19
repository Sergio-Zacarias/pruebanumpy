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

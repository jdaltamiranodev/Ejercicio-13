#Enunciado del ejercicio:

#En este segundo ejercicio, tenéis que crear una aplicación que obtendrá
# los elementos impares de una lista pasada por parámetro con filter y
# realizará una suma de todos estos elementos obtenidos mediante reduce.

from functools import reduce

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def impares(x):
    if x % 2 != 0:
        return True
    return False

def suma(a, b):
    return a + b

filtrada = list(filter(impares, numeros))
print(filtrada)

sumatoria = reduce(suma, filtrada)
print(sumatoria)
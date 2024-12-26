"""Escribí un programa que le solicite al usuario un número entero y 
muestre todos los números correlativos entre el 1 y el número ingresado 
por el usuario."""

num = int(input("Ingrese un número entero: "))
for i in range(1, num + 1):
    print(i)
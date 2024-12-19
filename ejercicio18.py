"""Escribí un programa que solicite al usuario el ingreso de dos números 
diferentes y muestre en pantalla al mayor de los dos."""

num1 = int(input("Ingrese un número: "))
num2 = int(input("Ingrese otro número: "))

if num1 > num2:
    print(f"{num1} es mayor que {num2}")
else:
    print(f"{num1} es menor que {num2}")

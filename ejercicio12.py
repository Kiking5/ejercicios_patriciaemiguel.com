"""Escribí un programa para solicitar al usuario el ingreso de un número 
entero y que luego imprima un valor de verdad dependiendo de si el número 
es par o no. Recordar que un número es par si el resto, al dividirlo por 2, 
es 0."""

num = int(input("Ingrese un número entero: "))

print(num % 2 == 0)

"""Escribí un programa que, dado un número por el usuario, muestre todos 
sus divisores positivos. Recordá que un divisor es aquel que divide al 
número de forma exacta (con resto 0)."""

num = int(input("Ingrese un número: "))

for i in range(1, num + 1):
    if num % i == 0:
        print(i)    
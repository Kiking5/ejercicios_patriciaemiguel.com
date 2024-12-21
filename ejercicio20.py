"""Escribí un programa para solicitar al usuario tres números y mostrar 
en pantalla al menor de los tres."""

num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
num3 = int(input("Ingrese el tercer número: "))

if num1 < num2 and num1 < num3:
    print(f"El menor de los tres números es {num1}")
elif num2 < num1 and num2 < num3:
    print(f"El menor de los tres números es {num2}")
else:
    print(f"El menor de los tres números es {num3}")

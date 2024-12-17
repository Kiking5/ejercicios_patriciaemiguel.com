"""Escribí un programa que solicite al usuario un número y le reste el 15%, 
almacenando todo en una única variable. A continuación, mostrar el resultado 
final en pantalla."""

num = float(input("Ingrese un número: "))
descuento = (num/100)*85 
print(f"{num} menos el 15% es: {descuento}")
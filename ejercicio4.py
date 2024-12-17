"""Escribí un programa que solicite al usuario ingresar la cantidad de 
kilómetros recorridos por una motocicleta y la cantidad de litros de 
combustible que consumió durante ese recorrido. Mostrar el consumo de 
combustible por kilómetro."""

kilometros = float(input("Ingrese la cantidad de kilometros recorridos: "))
litros_consumidos = float(input("Ingrese los litros que consumio en el recorrido: "))
print(f"El consumo de gasolina fue de {kilometros/litros_consumidos} litros.")

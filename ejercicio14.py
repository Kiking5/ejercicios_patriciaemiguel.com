"""Escribí un programa que, dada una cadena de texto por el usuario, imprima 
True si la cantidad de caracteres en la cadena es un número par, o False si 
no lo es."""

texto = input("Ingrese un texto: ")
print((len(texto)) % 2 == 0)
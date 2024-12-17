"""Escribí un programa que solicite al usuario el ingreso de dos palabras, 
las cuales se guardarán en dos variables distintas. A continuación, almacená 
en una variable la concatenación de la primera palabra, más un espacio, más 
la segunda palabra. Mostrá este resultado en pantalla."""

palabra1 = input("Ingrese una palabra: ")
palabra2 = input("Ingrese otra palabra: ")
frase = (f"{palabra1} {palabra2}")
print(frase)
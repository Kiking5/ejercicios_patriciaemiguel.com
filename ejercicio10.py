"""Escribí un programa que solicite al usuario que ingrese cuántos shows 
musicales ha visto en el último año y almacene ese número en una variable. 
A continuación mostrar en pantalla un valor de verdad (True o False) que 
indique si el usuario ha visto más de 3 shows."""

cantidad_de_shows = int(input("Ingrese cuantos shows musicales ha visto en el año: "))
if cantidad_de_shows > 3:
    print(True)
else: 
    print(False)
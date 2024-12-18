"""Escribí un programa que le solicite al usuario su edad y la guarde en 
una variable. Que luego solicite la cantidad de artículos comprados en una 
tienda y la guarde en otra variable. Finalmente, mostrar en pantalla un 
valor de verdad (True o False) que indique si el usuario es mayor de 18 años
 de edad y además compró más de 1 artículo."""

edad = int(input("Ingrese su edad: "))
articulos = int(input("Ingrese la cantidad de artículos comprados: "))

print((edad >= 18) and (articulos > 1))

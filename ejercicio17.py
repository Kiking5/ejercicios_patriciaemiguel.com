"""Escribí un programa que, dado un número entero, muestre su valor absoluto. 
Recordá que, para los números positivos su valor absoluto es igual al número 
(el valor absoluto de 52 es 52), mientras que, para los negativos, su valor 
absoluto es el número multiplicado por -1 (el valor absoluto de -52 es 52)."""

num = int(input("Ingrese un numero entero cualquiera: "))
absoluto =  abs(num)
print(f"El valor absoluto de {num} es {absoluto}")

##############################

if num < 0:
    num = num * -1
print(f"El valor absoluto es {num}")
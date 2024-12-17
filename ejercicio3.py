"""Escribí un programa que solicite al usuario dos números y los almacene en 
dos variables. En otra variable, almacená el resultado de la suma de esos dos 
números y luego mostrá ese resultado en pantalla. A continuación, el programa 
debe solicitar al usuario que ingrese un tercer número, el cual se debe 
almacenar en una nueva variable. Por último, mostrá en pantalla el resultado 
de la multiplicación de este nuevo número por el resultado de la suma anterior."""

num1 = int(input("Ingrese un número: "))
num2 = int(input("Ingrese un segundo número: "))
sum = num1 + num2
print(f"El resultado de la suma de {num1} y {num2} es {sum}")
num3 = int(input(f"Ingrese un tercer numero para multiplicar con {sum}: "))
mult = sum * num3
print(f"El resultado de mutiplicar {sum} y {num3} es: {mult}")
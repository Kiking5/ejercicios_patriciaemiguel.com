"""Escribí un programa que permita saber si un año es bisiesto. Para que 
un año sea bisiesto debe ser divisible por 4 y no debe ser divisible por 
100, excepto que también sea divisible por 400."""
biciesto = int(input("Ingrese un año: "))

if biciesto % 400 == 0:
    print(f"{biciesto} es biciesto")
elif biciesto % 4 == 0 and biciesto % 100 != 0:
    print(f"{biciesto} es biciesto")
else:
    print(f"{biciesto} no es biciesto")
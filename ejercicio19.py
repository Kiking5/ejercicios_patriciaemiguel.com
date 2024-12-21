"""Escribí un programa que solicite al usuario una letra y, si es una vocal, 
muestre el mensaje “Es vocal”. Verificar si el usuario ingresó un string de 
más de un carácter y, en ese caso, informarle que no se puede procesar el dato."""

vocales = "aeiouAEIOU"
letra = input("Ingrese una letra: ") 
for vocal in vocales:
    if letra == vocal:
        print(f"La letra {letra} es una vocal.")
        break
else:
    print(f"La letra {letra} no es una vocal.")
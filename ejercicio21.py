"""Escribí un programa que solicite ingresar un nombre de usuario y una 
contraseña. Si el nombre es “Gwenevere” y la contraseña es “excalibur”, 
mostrar en pantalla “Usuario y contraseña correctos. Puede ingresar a 
Camelot”. Si el nombre o la contraseña no coinciden, mostrar “Acceso 
denegado”."""

usuario = str(input("Ingrese su usuario: "))
contraseña = str(input("Ingrese su contraseña: "))

if usuario == "Gwenevere" and contraseña == "excalibur":
    print("suario y contraseña correctos. Puede ingresar a Camelot.")
else:
    print("Acceso denegado.")
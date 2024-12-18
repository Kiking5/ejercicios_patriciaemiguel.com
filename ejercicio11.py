"""Escribí un programa que le solicite al usuario ingresar una fecha formada 
por 8 números, donde los primeros dos representan el día, los siguientes dos 
el mes y los últimos cuatro el año (DDMMAAAA). Este dato debe guardarse en una 
variable con tipo int (número entero). Finalmente, mostrar al usuario la fecha 
con el formato DD / MM / AAAA."""

fecha = int(input("Ingresa una fecha en formato (DDMMAAAA), ejemplo 24122019: "))
fecha_str = str(fecha)
dia = fecha_str[:2]
mes = fecha_str[2:4]
year = fecha_str[4:]

print(f"La fecha es: {dia} / {mes} / {year}")
#ejercicio 1
print("dime el peso de tu paquete en kilogramos (puede tener decimales)")
peso_decimales = float(input("escribe aqui el peso de tu paquete: "))
print("Seleccione la zona a la que quiere que su envio llegue (1, 2 o 3):")
print("Zonas disponibles:")
print("1. Zona 1 (america): $5.0 por kilo")
print("2. Zona 2 (europa): $7.5 por kilo")
print("3. Zona 3 (resto del mundo): $10.0 por kilo")
zona = int(input("escribe aqui el numero de la zona: "))

if zona == 1:
    costo_envio = precio_envio = peso_decimales * 5.0
    print("El costo de envio es: $", costo_envio)
elif zona == 2:
    costo_envio = precio_envio = peso_decimales * 7.5
    print("El costo de envio es: $", costo_envio)   
elif zona == 3:
    costo_envio = precio_envio = peso_decimales * 10.0
    print("El costo de envio es: $", costo_envio)
else:
    print("Zona no válida. Por favor, seleccione una zona válida (1, 2 o 3).")
    costo_envio = None 
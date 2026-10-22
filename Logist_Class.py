#Tarifas:
tarifa_1 = 5.00
tarifa_2 = 7.50
tarifa_3 = 10.00

#Zonas del mundo:
Zona_1 = "America"
Zona_2 = "Europa"
Zona_3 = "Resto del mundo"

Lugar_destino = int(input("Ingrese un numero de acuerdo a su lugar de destino \n 1. America \n 2. Europa \n 3. Resto del mundo: \n"))

if Lugar_destino == 1:
    print("Su destino sera: ", Zona_1)
    print("La tarifa de su envio es: ", tarifa_1)

elif Lugar_destino == 2:
    print("Su destino sera: ", Zona_2)
    print("La tarifa de su envio es: ", tarifa_2)

elif Lugar_destino == 3:
    print("Su destino sera: ", Zona_3)
    print("La tarifa de su envio es: ", tarifa_3)

else:
    print("Ha ocurrido un error, ingrese un numero nuevamente")
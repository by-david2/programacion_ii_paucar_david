#condicional if
#simple

combustible = 5
if combustible >= 10:
    print("La nave puede despegar")

# condicionales in - else
creditos = int(input("Ingrese la cantidad de creditos: "))
precio_respuesta= int(input("Ingrese el precio de la respuesta: "))
if creditos >= precio_respuesta:
    print("La nave puede despegar")
else:
    print("La nave no puede despegar")

# if anidado 
if creditos >= precio_respuesta:
    print("La nave puede despegar")
    if creditos > precio_respuesta:
        print("Le sobran creditos")
    else:
        print("Le faltan creditos")
else:
    print("La nave no puede despegar")      

# condicionales elif
if creditos >= precio_respuesta:
    print("La nave puede despegar")
elif creditos == precio_respuesta:
    print("La nave puede despegar, pero no le sobran creditos")
else:
    print("La nave no puede despegar")  

tipo_repuesto = input("Ingrese el tipo de repuesto (motor, ala o escudo): ")
if tipo_repuesto == "motor" and creditos >= precio_respuesta and tipo_repuesto == "motor":
    print("puede comprar el repuesto")
elif tipo_repuesto == "ala" and creditos >= precio_respuesta and tipo_repuesto == "ala":
    print("puede comprar el repuesto")
elif tipo_repuesto == "escudo" and creditos >= precio_respuesta and tipo_repuesto == "escudo":
    print("puede comprar el repuesto")
else:
    print("no puede comprar el repuesto")  

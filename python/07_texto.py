#string cadena de caracteres
nave = "caza estelar nº1"
aprendiz= "obi-wan kenobi"
droide = "R2-D2"
planeta = "naboo"
codigo="1234-5678-9012"
print("Nave:", type(nave))
print("Aprendiz:", type(aprendiz))
print("Droide:", type(droide))
print("Planeta:", type(planeta))
print("Codigo:", type(codigo))
print("Aprendiz:", aprendiz)
print("Droide:", droide)
print("Planeta:", planeta)
print("Codigo es :" + codigo)
print("Codigo:", type(codigo))

longitud_nave = len(nave)
print("La longitud de la cadena nave es:" + str(longitud_nave))
longitud_aprendiz = len(aprendiz)
print("La longitud de la cadena aprendiz es:" + str(longitud_aprendiz))

mensaje ="La federacion de comercio ha bloqueado el planeta"
print("Mensaje:" + mensaje)
mensaje_mayusculas = mensaje.upper()
print("Mensaje en mayusculas:" + mensaje_mayusculas)
mensaje_minuscula = mensaje.lower()
print("Mensaje en minusculas:" + mensaje_minuscula)

comunicado = "La federacion de comercio ha bloqueado el planeta"
print("Mensaje:" + comunicado)
nuevo_comunicado = comunicado.replace("bloqueado", "invadido")
print("Mensaje modificado:" + nuevo_comunicado)

planeta = "Tatooine, adooo, venuz, naboo"
planetas = planeta.split(", ")
print(planetas)
print("Planetas:" + str(planetas))
print("Primer planeta:" + planetas[0])

droide = "R2-D2"
print("Primer caracter del droide:" + droide[0])
print("Último caracter del droide:" + droide[-1])
print("el tercer caracter del droide es:" + droide[2])
print("el cuarto caracter del droide es:" + droide[3])
print("el quinto caracter del droide es:" + droide[4])

planeta = "     naboo       "
print("Planeta original:" + planeta)
print("Planeta sin espacios en blanco:" + planeta.strip())

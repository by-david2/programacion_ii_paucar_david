# ciclo for

naves=[
    " caza n-1",
    " nave real de naboo",
    " trasporte",
]
for nave in naves:
    print ("inspeccionando", nave)
print("inspeccion realizada")

rondas= range (1,6)

print("tipo de rondas:", type(rondas))
for ronda in rondas:
    print(f"ronda de vigilancia: {ronda}")
    print(f"tipo de dato ronda {type(ronda)}")


droides= range (1,17,2)

print("tipo de droide:", type(droides))
for droide in droides:
    print(f"ronda de vigilancia: {droide}")
    print(f"tipo de dato ronda {type(droide)}")

planetas=[
    "Naboo",
    "tatooine",
    "coruscant"
]
recorrido = enumerate(planetas,start=1)
for posicion, planeta in recorrido:
    print(f"destino: {posicion}: {planeta}")
    print(f"tipo de dato ronda {type(posicion)}: {type(planetas)}")

paises = [
    "Ecuador",
    "Colombia",
    "Venezuela",
    "Chile",
    "Brasil",
]
for pais in paises:
    if pais == "Chile":
        continue
    if pais == "Brasil":
        break
    print(f"pais visitado {pais}")

#creacion de diccionarios
jedi={}
jedi_activo= {
    "nombre": "obiwam",
    "fuerza": "120",
    "estilo_pelea":"samurai",
    "mision":["guerra aldeana", "secretos palpatine", "escolta de leia"],
    "descripcion":{
        "estatura": 1.80,
        "especie":"humana"
    }
}
print(jedi_activo)
nave = dict(nombre="AZ-1", capacidad=8, tubo_laser=2)
print(nave)

#otra forma de crear un diccionario
jedi["nombre"]= "luck"
jedi["fuerza"]= 150
print(jedi)

for clave, valor in jedi_activo.items():
    print(f"clave: {clave} - {valor}")

#uso del while
combustible = 100
vueta = 1

while combustible >= 20:
    print(f"vueta {vueta}")
    print(f"combustible inicial:{combustible}")
    combustible -= 20
    print(f"combustible final:{combustible}")
    vueta += 1
print("carrera finalizada")
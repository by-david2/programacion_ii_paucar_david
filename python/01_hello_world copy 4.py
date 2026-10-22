naves=[
    "Caza_1",
    "Caza_2",
    "Caza_3"
]
for nave in naves:
    print( "Inspeccionando", nave)
print("Inspeccion realizada")

droides = range(1,17, 6) 
print("tipo de rondas: ", type(droides))
for droide in droides:
    print(f"Ronda de vigilancia: {droide}")
    print(f"Tipo de dato ronda: {type(droide)}")

planetas= [
    "Naboo",
    "Tatooine",
    "Coruscant"
]

recorrido = enumerate(planetas, start= 1)

for posicion, planeta in recorrido:
    print(f"Destino {posicion}: {planeta}")
    print(f"Tipos de dato {type(posicion)}: {type(planeta)}")
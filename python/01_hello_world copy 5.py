#control de flota

naves = [
    {"nombre": "caza_1",
    "combustible": 100,
    "droides": ["rd2 - rd3"],
    },
    
    {"nombre": "transportador",
     "combustible": 35,
     "droides": ["r2 - r3"]
     },

     {"nombre": "real_caza",
      "combustible": 65,
      "droides": ["rd2 - rd3", "r2 - r3"] 
     }

]
naves_lista = 0
naves_recarga = 0
total_droides = 0
total_ciclos = 0

for numero, nave in enumerate(naves, start = 1):
    print(f"--Nave : {numero}-{nave}")
    if nave["combustible"] >=50 :
        print("Estado inicial: Lista")
        naves_listas += 1
    else:
        print("Estado inicial: Reacargar")
        naves_recarga += 1
        ciclo = 0 
        while nave["combustible"] <=50:
            ciclo +=1
            nave["combustible"] +=10
        total_ciclos += ciclo
        print("Recarga Completada")
        print("Estado Final: Lista")
    total_droides = len(nave["droides"])
    for droide in nave["droides"]:
        print(f"droide: {droide}")

print("-------------------------")
print("RESUMEN")
print("-------------------------")
print("-------------------------")
print(f"total naves: {len(naves)}")
print(f"Naves listas incialmente: {naves_listas}")
print(f"Naves recargadas: {naves_recarga}")
print(f"total droides: {total_droides}")
print(f"total ciclos: {total_ciclos}")
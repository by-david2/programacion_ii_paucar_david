"""
control de flota de naboo
"""
naves = [
    {
        "nombre": "caza n-1",
        "combustible": 10,
        "droide": ["r2-d2"]
   },
   {
        "nombre": "trasportador",
        "combustible": 10,
        "droide": ["r2-n3"]
   },
      {
        "nombre": "real caza",
        "combustible": 5,
        "droide": ["r2-d2", "r2-n3"]
   }
]
naves_listas=0
naves_recarga=0
total_droides=0
total_ciclos=0
for numero,nave in enumerate(naves,start=1):
    print(f"---nave : {numero}-{nave}")
    if nave ["combustible"] >= 50:
        print(f"estado inicial:LISTA")
        naves_listas += 1
    else:
        print(f"estado inicial: RECARGAR")
        naves_recarga += 1
        ciclo=0
        while nave["combustible"] <= 50:
            ciclo +=1
            nave["combustible"] += 10
        total_ciclos += ciclo
        print("recarga completa")
        print("estado final: LISTA")
    total_droides+=len(nave["droide"])
    for droide in nave ["droide"]:
        print(f"droide: {droide}") 
print("====================================")           
print("resumen")
print("====================================")
print(f"total naves: {len(naves)}")
print(f"naves listas inicialmente: {naves_listas}")
print(f"naves recargadas: {naves_recarga}")
print(f"total droides: {total_droides}")
print(f"total ciclos: {total_ciclos}")
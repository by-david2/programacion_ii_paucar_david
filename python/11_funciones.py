#funciones
def activar_sistema():
    print("==sistema de naboo==")
    print("sistema de control activado")

activar_sistema()

#funciones de parametros

def saludar_jedi(nombre):
    print(f"que la fuerza te acopmañe: {nombre}")

saludar_jedi("qui-go jim")
saludar_jedi("obi-wan kenobi")

def mostrar_nave(nombre,combustible):
    print(f"nave: {nombre}")
    print(f"cantidad combustible: {combustible}")

mostrar_nave("Caza n-1", 80)

#funciones que devulven datos o informacion
#return

def calcular_combustible(inicial,consumo):
    restante =inicial - consumo
    return restante
resultado = calcular_combustible(100,25)
print(f"combustible: {resultado}")
class Guerrero:
    nombre: str
    poder: int
    def __init__(self,nombre:str, poder:int):
        self.nombre = nombre
        self.poder=poder

    def saludar(self):
        print("hola, soy:", self.nombre)
        print("mi poder es de:", self.poder)

    def entrenar(self):
        aumento=200
        self.poder += aumento

    def atacar(self,cantidad):
        danio =self.poder*cantidad
        print("guerrero", self.nombre)
        print("daño causado", danio)


goku=Guerrero("goku",9000)
goku.saludar()

print("nombre del personaje:", goku.nombre)
print("el poder es de", goku.poder)
goku.entrenar()
print("poder actual del personaje", goku.poder)
goku.atacar(2)
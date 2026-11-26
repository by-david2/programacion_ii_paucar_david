class RadarDragon:
    region1: int
    region2: int
def __init__(self,region1,region2):
        self.region1=region1
        self.region2=region2

def buscar_esferas(self):
    esferasRegion1 = 7 - self.region1
    esferasRegion2 = 7 - self.region2
    print(f"las esferas encontradas en la region 1 son: {self.region1}")
    print(f"las esferas encontradas en la region 2 son: {self.region2}")
bulma=RadarDragon(3,2)
bulma.buscar_esferas()

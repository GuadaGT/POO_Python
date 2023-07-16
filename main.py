class Vehículo:
    def __init__(self, color, ruedas, puertas):
        self.color = color
        self.ruedas = ruedas
        self.puertas = puertas

class Coche(Vehículo):
    def __init__(self, color, ruedas, puertas, velocidad, cilindrada):
        super().__init__(color, ruedas, puertas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

coche = Coche("Verde", 4, 5, 200, 5100)
print("Color:", coche.color)
print("Ruedas:", coche.ruedas)
print("Puertas:", coche.puertas)
print("Velocidad:", coche.velocidad)
print("Cilindrada:", coche.cilindrada)
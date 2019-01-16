# Classe Quadrado: Crie uma classe que modele um quadrado:

# Atributos: Tamanho do lado
# Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área;

class Quadrado:

    def __init__(self, lado):
        self.lado = lado

    def mostrar_lado(self):
        print(self.mostrar_lado)

    def trocar_lado(self,outro_lado):
        self.lado = outro_lado

    def calcular_area(self):
        print(self.lado**2)

quadrado = Quadrado(10)

print(quadrado.lado)


quadrado.trocar_lado(7)
print(quadrado.lado)

quadrado.calcular_area()

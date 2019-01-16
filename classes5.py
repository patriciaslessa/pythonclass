# Classe Bola: Crie uma classe que modele uma bola:
#
# Atributos: Cor, circunferência, material
# Métodos: trocaCor e mostraCor

class Bola:

    def __init__(self, cor, raio):
        self.cor = cor
        self.raio = raio

    def mostrar_cor(self):
        print(self.cor)

    def mostrar_raio(self):
        print(self.raio)

    def trocar_cor(self,outra_cor):
        self.cor = outra_cor

bola = Bola('verde', 10)
# print(bola.cor)
# print(bola.raio)

tenis = Bola('azul',3)
# print(tenis.cor)
# print(tenis.raio)


bola.mostrar_cor()
tenis.mostrar_cor()
bola.mostrar_raio()
tenis.mostrar_raio()

tenis.material='polimero'
print(tenis.material)
#print(bola.material)


class BolaGolf(Bola):
    material = 'palha'

golf = BolaGolf('branco',1)
print(golf.material)
golf.mostrar_cor()
golf.mostrar_raio()


class BolaSquash(Bola):
    def __init__ (self,cor,raio,material):
        Bola.__init__(self,cor,raio)
        self.material = material

    def exibir_material(self):
        print(self.material)

squash = BolaSquash('verde',17,'lona')
squash.exibir_material()
squash.mostrar_cor()




bol = Bola('verde',10)
print(bol.cor)
bol.trocar_cor('vermelho')
print(bol.cor)

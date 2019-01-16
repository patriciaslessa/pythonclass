# Crie uma classe que modele um retangulo:
# Atributos: LadoA, LadoB (ou Comprimento e Largura, ou Base e Altura, a escolher)
# Métodos: Mudar valor dos lados, Retornar valor dos lados, calcular Área e calcular Perímetro;
# Crie um programa que utilize esta classe. Ele deve pedir ao usuário que informe as medida des de um local.
# Depois, deve criar um objeto com as medidas e calcular a quantidade de pisos e de rodapés necessárias para o local.

class Retangulo:

    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def mostrar_lado(self):
        return (self.mostrar_base,self.mostrar_altura )

    def trocar_lado(self,outra_base, outra_altura):
        self.base = outra_base
        self.altura = outra_altura

    def calcular_area(self):
        return (self.base*self.altura)

    def calcular_perimetro(self):
        return (2*(self.base+self.altura))

retangulo = Retangulo(10,5)

print (retangulo.base, retangulo.altura)

retangulo.trocar_lado(7,3)
print (retangulo.base, retangulo.altura)

print (retangulo.calcular_area())
print (retangulo.calcular_perimetro())

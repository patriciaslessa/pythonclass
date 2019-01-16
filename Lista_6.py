##Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
##o produto do dobro do primeiro com metade do segundo .
##a soma do triplo do primeiro com o terceiro.
##o terceiro elevado ao cubo.

a= int(input("digite inteiro: "))
b= int(input("digite inteiro: "))
c= float(input("digite real: "))
x= (2*a)*(c/2)
y= 3*a + c
z= c**3
#print("x: %i,y: %i,z: %5.2f" %(x,y,z))  
print(f"x: {x}, y: {y}, z: {z:0.2f}")
      

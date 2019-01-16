#Classe Pessoa: Crie uma classe que modele uma pessoa:
#CPF, Nome, Cidade

import pandas as pd

pessoas=[]

for _ in range(2):
    pessoa= {
        'CPF':input('digite o CPF: '),
        'Nome':input('digite o nome: '),
        'idade': int(input('digite a idade: '))
        }
    pessoas.append(pessoa)


data = pd.DataFrame(pessoas)
#M = data['idade'].mean()

print( data['idade'].mean())
print(data)

data['idade'].plot()

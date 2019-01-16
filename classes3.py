#Classe Pessoa: Crie uma classe que modele uma pessoa:
#CPF, Nome, Cidade

import pandas as pd

pessoa_1 = { 'CPF': 12345678912,
        'Nome':'Joao',
        'Cidade':'Recife',
         'idade': 33
}
pessoa_2 = { 'CPF':64345673412,
        'Nome':'Pepe',
        'Cidade':'JG',
        'idade': 20
}


data = pd.DataFrame([pessoa_1,pessoa_2])
M = data['idade'].mean()

print(M)

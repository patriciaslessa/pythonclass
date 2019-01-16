#Classe Pessoa: Crie uma classe que modele uma pessoa:
#CPF, Nome, Cidade

import pandas as pd

pessoa_1 = { 'CPF': 12345678912,
        'Nome':'Joao',
        'Cidade':'Recife'
}
pessoa_2 = { 'CPF':64345673412,
        'Nome':'Pepe',
        'Cidade':'JG'
}


print(pd.DataFrame([pessoa_1,pessoa_2]))

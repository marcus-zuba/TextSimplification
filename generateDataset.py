import os
import pandas as pd
from sklearn.model_selection import train_test_split

data = []
tipos = set()

# Open a file: file
for filename in sorted(os.listdir('processado')):

    file = open(f'processado/{filename}',mode='r')

    rule = filename.split("_")[1].replace(".txt", "")
    
    # read all lines at once
    all_of_it = file.read()

    all_of_it = all_of_it.split('\n')

    for i, par in enumerate(all_of_it):
        
        l = par.split("//")
        if(i<1250):
            tipos.add(f"frase-{rule}")
            l.append(f"frase-{rule}")
            data.append(l)
        elif(i<2500):
            tipos.add(f"parágrafo-{rule}")
            l.append(f"parágrafo-{rule}")
            data.append(l)

df = pd.DataFrame(data, columns=['Complexa', 'Simples', 'Tipo'])

df = df.replace('old character','new character', regex=True)
  
df.to_csv("dataset/dataset.csv", sep='\t')

treino, teste = train_test_split(df, test_size=20000, stratify=df["Tipo"], random_state=1)

teste, validacao = train_test_split(teste, test_size=10000, stratify=teste["Tipo"], random_state=1)

for tipo in tipos:
    print(tipo)
    print(f"\tQuantidade de {tipo} no treino: {len(treino[treino['Tipo'] == tipo])}")
    print(f"\tQuantidade de {tipo} no teste: {len(teste[teste['Tipo'] == tipo])}")
    print(f"\tQuantidade de {tipo} na validação: {len(validacao[validacao['Tipo'] == tipo])}")

treino.to_csv("dataset/train.complex", columns=["Complexa"], header=False, index=False)
treino.to_csv("dataset/train.simple", columns=["Simples"], header=False, index=False)

teste.to_csv("dataset/test.complex", columns=["Complexa"], header=False, index=False)
teste.to_csv("dataset/test.simple", columns=["Simples"], header=False, index=False)

validacao.to_csv("dataset/valid.complex", columns=["Complexa"], header=False, index=False)
validacao.to_csv("dataset/valid.simple", columns=["Simples"], header=False, index=False)

for filename in sorted(os.listdir('dataset')):
    
    file = open(f'dataset/{filename}',mode='r')
    
    # read all lines at once
    all_of_it = file.read()

    file.close()

    all_of_it = all_of_it.split('\n')

    file = open(f'dataset/{filename}',mode='w')

    for s in all_of_it:
        file.writelines(s.removeprefix('"').removesuffix('"')+"\n")
    
    file.close()
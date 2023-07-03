import os
from wordfreq import tokenize

n_pares_frases = 0
n_pares_paragrafos = 0

numeroDeFrases = 0
numeroDeParagrafos = 0

numeroDePalavrasFrases = 0
numeroDePalavrasParagrafos = 0

# Open a file: file
for filename in sorted(os.listdir('processado')):

    file = open(f'processado/{filename}',mode='r')

    print(filename)
    
    # read all lines at once
    all_of_it = file.read()

    all_of_it = all_of_it.split('\n')

    for i, par in enumerate(all_of_it):
        
        if(i<1250):
            numeroDeFrases+=1
            numeroDePalavrasFrases+=(len(tokenize(par, 'pt')))
        elif(i<2500):
            numeroDeParagrafos+=1
            numeroDePalavrasParagrafos+=(len(tokenize(par, 'pt')))

    print(f'\tn frases: {numeroDeFrases}')
    print(f'\tn parágrafos: {numeroDeParagrafos}')

    print(f'\tn palavras nas frases: {numeroDePalavrasFrases}')
    print(f'\tn palavras nos parágrafos: {numeroDePalavrasParagrafos}')

    # close the file
    file.close()

print(f'média de palavras nas frases: {numeroDePalavrasFrases/numeroDeFrases}')
print(f'média de palavras nos parágrafos: {numeroDePalavrasParagrafos/numeroDeParagrafos}')
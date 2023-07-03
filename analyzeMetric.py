import os
import wordfreq
from wordfreq import zipf_frequency

def calculate_score(complex, simple):

    def calculate(sentence):
        words = wordfreq.tokenize(sentence, 'pt')
        n = len(words)
        summatory = 0
        for word in words:
            summatory += max(zipf_frequency(word, 'pt'), 1)
        return (1/n**1.19)*summatory
    
    return (calculate(simple)-calculate(complex))

n_pares = 0
n_positivos = 0
n_negativos = 0

# Open a file: file
for filename in sorted(os.listdir('processado')):

    file = open(f'processado/{filename}',mode='r')
    
    # read all lines at once
    all_of_it = file.read()

    all_of_it = all_of_it.split('\n')

    for i,par in (enumerate(all_of_it)):
        if not par:
            continue
        n_pares+=1
        comp, simp = par.split("//")
        if (calculate_score(comp, simp)>0):
            n_positivos+=1
        else:
            n_negativos+=1

    file.close()

print(f'número total de pares: {n_pares}')
print(f'número de pares com score positivo: {n_positivos}')
print(f'número de pares com score negativo: {n_negativos}')

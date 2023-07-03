ruleTypes = ["Aposto-Enumerativo", "Aposto-Especificador", "Aposto-Recapitulativo", "OC-Assindeticas", "OCS-Aditivas", "OCS-Adversativas",
            "OCS-Alternativas", "OCS-Conclusivas", "OCS-Explicativas", "OSAdj-Explicativas", "OSAdj-Restritivas", "OSAdv-Causais",
            "OSAdv-Comparativas", "OSAdv-Concessivas", "OSAdv-Condicionais", "OSAdv-Conformativas", "OSAdv-Consecutivas", "OSAdv-Finais", 
            "OSAdv-Proporcionais", "OSAdv-Temporais", "Reduzidas-Gerundio", "Reduzidas-Infinitivo", "Reduzidas-Participio", "Voz-Passiva"]

for ruleType in ruleTypes:

    print(f'Processando {ruleType}')

    filenames = [f'outputs/output_frases-{ruleType}.txt', f'outputs/output_parágrafos-{ruleType}.txt']

    for filename in filenames:

        file = open(filename,mode='r')
        
        # read all lines at once
        all_of_it = file.read()

        # close the file
        file.close()

        all_of_it = all_of_it.split('\n')

        anterior = ''
        atual = ''

        n_par = 0

        complexas = []

        processadas = []

        complexas_duplicadas = 0
        simples_duplicadas = 0

        complexa_atual = ''
        simplificada_atual = ''

        i_complexa = 0

        for i,st in enumerate(all_of_it):
            if st[:2] == 'C:':
                i_complexa = i
                complexa_atual = st
            if st[:2] == 'S:' and i==i_complexa+1:
                simplificada_atual = st
                if complexa_atual not in complexas:
                    processadas.append(complexa_atual[3:] + "//" + simplificada_atual[3:] + "\n")
                    complexas.append(complexa_atual)
                    i_complexa=0
                    complexa_atual = ''
                    simplificada_atual = ''


        file = open(f'processado/processado_{ruleType}.txt', 'a')

        for i in range(1250):
            file.writelines(processadas[i])

        file.close()


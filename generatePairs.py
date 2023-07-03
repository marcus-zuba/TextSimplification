from multiprocessing import Process
import openai
import time

openai.api_key = "OPEN-AI-API-KEY"

global_category = ""
global_rule_type = ""

def task():

    ruleFile = f"rules/rule_{global_rule_type}.txt"
    outputFile = f"outputs/output_{category}-{global_rule_type}.txt"

    rule = ""
    with open(ruleFile, "r") as file:
        rule = file.read()

    input = f"""
    com base na regra:\n
    {rule}\n
    gere 10 novos pares de {category} complexos e simplificados, seguindo o seguinte padrão:
    C: {category} complexo
    S: {category} simplificado

    C: {category} complexo
    S: {category} simplificado

    C: {category} complexo
    S: {category} simplificado

    """

    print(f"Iniciando request")
    init_req = time.time()

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-16k",
            messages=[
                {"role": "system", "content": "Pode demorar o tempo que for necessário para fornecer a resposta."}, 
                {"role": "user", "content": f"{input}"}, 
            ]
        )
        for choice in response.choices:
            content = str(choice.message.content)
            currentGeneratedPairs = (content.count("\n")+2)/3
            if content[:2]=="C:":
                print(f"Request bem sucedida, gerando {currentGeneratedPairs} pares")
                with open(outputFile, "a") as file:
                    file.write(content + "\n\n")
            else:
                    print("Request não gerou o output esperado.")
    except Exception as e:
        print(e)
        exit(1)

    end_req = time.time()
    print(f"Request finalizada após {'{0:.2g}'.format(end_req-init_req)}s\n")



if __name__ == '__main__':

    categories = ["frases", "parágrafos"]

    ruleTypes = ["Aposto-Enumerativo", "Aposto-Especificador", "Aposto-Recapitulativo", "OC-Assindeticas", "OCS-Aditivas", "OCS-Adversativas",
                "OCS-Alternativas", "OCS-Conclusivas", "OCS-Explicativas", "OSAdj-Explicativas", "OSAdj-Restritivas", "OSAdv-Causais",
                "OSAdv-Comparativas", "OSAdv-Concessivas", "OSAdv-Condicionais", "OSAdv-Conformativas", "OSAdv-Consecutivas", "OSAdv-Finais", 
                "OSAdv-Proporcionais", "OSAdv-Temporais", "Reduzidas-Gerundio", "Reduzidas-Infinitivo", "Reduzidas-Participio", "Voz-Passiva"]

    for category in categories:

        global_category = category

        for ruleType in ruleTypes:

            global_rule_type = ruleType

            generatedPairs = 0

            numberOfPairsToGenerate = 1250

            print(f"Iniciando geração de {numberOfPairsToGenerate} pares de {category} da regra {ruleType}\n")
            init_total = time.time()

            while generatedPairs < numberOfPairsToGenerate:

                process = Process(target=task)
                process.start()
                process.join(60)
                if(process.exitcode==0):
                    generatedPairs+=10
                    print(f"Thread bem sucedida. Número de pares gerados até agora: {generatedPairs}")
                else:
                    print("Thread mal sucedida. Esperando 20 segundos")
                    time.sleep(20)

                process.terminate()

            end_total = time.time()
            print(f"Foram gerados {generatedPairs} pares de frases complexas-simples em {'{0:.2g}'.format((end_total-init_total)/60)} minutos.")

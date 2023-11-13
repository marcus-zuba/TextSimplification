import os
import sys
import wordfreq
from wordfreq import zipf_frequency

def calculate_score(complex, simple):

    def removeStopWords(words):
        newWords = []
        for word in words:
            if word not in stopWords:
                newWords.append(word)
        return newWords

    def calculate(text):
        sentences = text.split(".")
        sumOfWeights = 0
        score = 0
        for sentence in sentences:
            words = wordfreq.tokenize(sentence, 'pt')
            n = len(words)
            if n == 0:
                continue
            summatory = 0
            for word in words:
                summatory += max(zipf_frequency(word, 'pt'), 1)
            score += n * (1/n**1.19) * summatory
            sumOfWeights += n
        return score/sumOfWeights
    
    return max(0, 100 * (0.0001 + (calculate(simple)-calculate(complex))))


def calculate_score_for_files(complex_file, simple_file):

    with open(complex_file) as complexFile:
        complex_sentences = [s for s in complexFile.read().split('\n') if s] 

    with open(simple_file) as simpleFile:
        simple_sentences = [s for s in simpleFile.read().split('\n') if s]

    if (len(complex_sentences) != len(simple_sentences)):
        print("O tamanho dos dois arquivos é diferente")
        exit(1)

    sumScores = 0
    numSentences = 0

    for i in range(len(complex_sentences)):
        if(len(complex_sentences[i])>0):
            sumScores += calculate_score(complex_sentences[i], simple_sentences[i])
            numSentences += 1

    return sumScores/numSentences
       

print(calculate_score_for_files(sys.argv[1], sys.argv[2]))

import wordfreq
from wordfreq import zipf_frequency

def calculate_score(simple, complex):

    def calculate(sentence):
        words = wordfreq.tokenize(sentence, 'pt')
        n = len(words)
        summatory = 0
        for word in words:
            summatory += max(zipf_frequency(word, 'pt'), 1)
        return (1/n**1.19)*summatory
    
    return (calculate(simple)-calculate(complex))

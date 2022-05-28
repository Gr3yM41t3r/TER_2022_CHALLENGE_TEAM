import re

from nltk.util import ngrams  # This is the ngram magic


re_stripper_alpha = re.compile('[^a-zA-Z]+')


'''
this method will return list of nGram of text
'''
def nGRAM(txt, NGRAM):
    if not txt:
        return None
    ng = ngrams(re_stripper_alpha.sub(' ', txt).split(), NGRAM)
    return list(ng)


def intersection(lst1, lst2):
    return list(set(lst1) & set(lst2))

'''
this method returns ngram similarity
according to this equation 
σNG(s1,s2) = |ngram(s1,n)∩ngram(s2,n)|
            ___________________________
                min(|s1|,|s2|)−n+1
'''

def nGram_similarity(s1, s2, n):
    return len(intersection(nGRAM(s1, n), nGRAM(s2, n))) / (min(len(s1.split()), len(s2.split())) - n + 1)


phrase = "Milwaukee County Executive Chris Abele says county buses are no less safe now than a year or two ago"
phrase2 = "Milwaukee County Executive Chris Abele says county buses are no less safe now than a year or two ago"
phrase3 = "Milwaukee County  says county buses are no less safe now than a year or two ago"

'''uncomment me'''
# print(nGRAM(phrase, 10))
#print(nGram_similarity(phrase, phrase2,3))
#print(nGram_similarity(phrase, phrase3,3))

import csv
import math
from collections import Counter

from Levenshtein import distance
from sklearn.metrics.pairwise import cosine_similarity

model_name = 'bert-base-nli-mean-tokens'

header = ['IdA', 'IdB', 'TextA', 'TextB', 'LenA', 'LenB', 'Levenshtein-Distance', 'Jaccard_Distance',
          'Sentence_similarity_vect', 'similarity']
data = []










def Jaccard_Similarity(text1, text2):
    words_text1 = set(text1.lower().split())
    words_text2 = set(text2.lower().split())
    intersection = words_text1.intersection(words_text2)
    union = words_text1.union(words_text2)
    if len(union) == 0:
        return 0
    return float(len(intersection)) / len(union)

print(Jaccard_Similarity("Marco Rubio says Iran deal means we have to help defend Iran from Israel or other allies","Trump says Iran deal forces U.S. to defend Iran if it's attacked by Israel"))
def Jaccard_distance(text1, text2):
    a = set(text1)
    b = set(text2)
    return 1.0 * len(a & b) / len(a | b)


def Levenshtein_Distance(text1, text2):
    return distance(text1, text2)


def cosine_similarity_ngrams(a, b):
    vec1 = Counter(a)
    vec2 = Counter(b)

    intersection = set(vec1.keys()) & set(vec2.keys())
    numerator = sum([vec1[x] * vec2[x] for x in intersection])

    sum1 = sum([vec1[x] ** 2 for x in vec1.keys()])
    sum2 = sum([vec2[x] ** 2 for x in vec2.keys()])
    denominator = math.sqrt(sum1) * math.sqrt(sum2)

    if not denominator:
        return 0.0
    return float(numerator) / denominator

##sameLignComparaison("claims_prof.csv", "similarity.csv")

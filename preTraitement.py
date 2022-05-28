import numpy as np
from nltk.tokenize import RegexpTokenizer
from nltk.util import ngrams  # This is the ngram magic

from fmeasures import fMeasure
from pretraitement import *
from similarityDetector import *
from sklearn.metrics import confusion_matrix, plot_confusion_matrix

# lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words('english'))
tfidf_vectorizer = TfidfVectorizer()
tokenizer = RegexpTokenizer(r'\w+')
re_stripper_alpha = re.compile('[^a-zA-Z]+')

header = ['IdA', 'TextBefore', 'TextAfter']
data = []


##----------------- stop words------------------------------

def removeStopWords(text):
    words = text.split()
    pretrained_Text = ""
    for r in words:
        if not r in stop_words:
            pretrained_Text += r + " "
    return pretrained_Text


##-------------------------------NGram  tools--------------


def nGRAM(txt, NGRAM):
    """Get tuples that ignores all punctuation (including sentences)."""
    if not txt: return None
    ng = ngrams(re_stripper_alpha.sub(' ', txt).split(), NGRAM)
    return list(ng)


def intersection(lst1, lst2):
    return list(set(lst1) & set(lst2))


def nGram_similarity(s1, s2, n):
    return len(intersection(nGRAM(s1, n), nGRAM(s2, n))) / (min(len(s1.split()), len(s2.split())) - n + 1)


def getResult(id, textScore, keywordsScore, athorA, authorB):
    if textScore > 0.6 and normalize(authorB) == normalize(athorA):
        return "E"
    elif textScore > 0.6 and keywordsScore > 0.5 and authorB != athorA:
        return "E*"
    elif 0.35 < textScore <= 0.6:
        if keywordsScore < 0.2:
            return 'N'
        return 'ST'
    elif textScore <= 0.35:
        if keywordsScore > 0.6:
            return 'ST'
        return 'N'
    else:
        print("waaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaA3", id)


def makeResulat(textscor, threshold, athorA, authorB):
    if textscor > threshold and authorB == athorA:
        return 'E'
    elif textscor > threshold and authorB != athorA:
        return 'E*'


def removeStopWordsProfCsv():
    header2 = ['TexteA', 'TextB', 'TextAPT', 'TextBPT', 'TFIDF', 'Jaccard_Distance', 'Levenshtein_Distance',
               'NGram-Similarity', 'EXPECTED',
               'RESULT', 'Score Keywords', 'Score entities']
    corpus = []
    corpuskeywords = []
    corpusentities = []
    with open('inputCSV/test.csv') as inputData:
        reader = csv.reader(inputData)
        claims = list(reader)
        with open("outputCSV/pretraiteCSV.csv", "w") as outputData:
            writer = csv.writer(outputData)
            writer.writerow(header2)
            counter = 1
            for claim in claims:
                # print(counter)
                counter += 1
                # data reset
                data.clear()
                corpus.clear()
                corpuskeywords.clear()
                corpusentities.clear()
                # original text A and B before Modifications
                textA = claim[6]
                textB = claim[7]
                # text A and B after removing stop words lowering and removine punctuation
                textA_After = normalize(textA)
                textB_After = normalize(textB)
                # print(claim[8], claim[9])
                # keyword 
                keywordsA = normalize(claim[14].lower())
                keywordsB = normalize(claim[15].lower())
                # entities
                entiteA = normalize(claim[8].replace('_', ' '))

                entiteB = normalize(claim[9].replace('_', ' '))
                print("entiteA", entiteA)
                print("entiteB", entiteB)
                # print('{} : {}'.format(counter, claim[10]))
                # calculating TF-IDF TEXTE
                corpus.append(textA_After)
                corpus.append(textB_After)
                tfidf_matrix = tfidf_vectorizer.fit_transform(corpus)
                cosine = cosine_similarity(tfidf_matrix, tfidf_matrix)
                tfidf_value = round(cosine[0][1], 2)

                # calculating TF-IDF kEYWORDS                
                corpuskeywords.append(keywordsA)
                corpuskeywords.append(keywordsB)
                tfidf_matrix = tfidf_vectorizer.fit_transform(corpuskeywords)
                cosine = cosine_similarity(tfidf_matrix, tfidf_matrix)
                tfidf_key_value = cosine[0][1]

                # calculating TF-IDF entities
                corpusentities.append(entiteA)
                corpusentities.append(entiteB)
                tfidf_matrix = tfidf_vectorizer.fit_transform(corpusentities)
                cosine = cosine_similarity(tfidf_matrix, tfidf_matrix)
                tfidf_entities_value = cosine[0][1]
                print("kjlkjlkjljk", tfidf_entities_value)
                # calculation Jaccard_Distance
                jaccard_distance = Jaccard_Similarity(textA_After, textB_After)
                # calculation Levenshtein_Distance
                lev_distance = Levenshtein_Distance(textA_After, textB_After)
                # calculation Ngram_similarity
                ngram_similarity = nGram_similarity(textA, textB, 3)
                # Expected Result for similarity
                expected_Similarity = claim[0]
                # Actual  model similarity
                # print("id: {}  TFIDF: {} TFIDF2: {}".format(counter,tfidf_value,tfidf_key_value))
                actual_result = getResult(counter, tfidf_value, tfidf_key_value, claim[10], claim[11])
                # actual_result = makeResulat(tfidf_key_value, threshold)
                # adding data
                data.append(textA)
                data.append(textB)
                data.append(textA_After)
                data.append(textB_After)
                data.append(tfidf_value)
                data.append(jaccard_distance)
                data.append(lev_distance)
                data.append(ngram_similarity)
                data.append(expected_Similarity)
                data.append(actual_result)
                data.append(tfidf_key_value)
                data.append(tfidf_entities_value)

                writer.writerow(data)


#removeStopWordsProfCsv()


def score():
    print("________________________________________________________")
    classes = ["E", "ST", "N", "E*"]
    total = 0
    for i in classes:
        score = fMeasure(i)
        print("{}: {}".format(i, score))
        total += score
    print("total: ", total / len(classes))


#score()


def start():
    header = ['threshold', 'fmeasure', ]
    date = []
    with open('classeDetector/EFIDF_KEYWORDS.csv', 'w+') as output:
        writer = csv.writer(output)
        writer.writerow(header)
        for i in np.arange(0, 1.02, 0.05):
            print(i)
            date.clear()
            removeStopWordsProfCsv(i)
            score()
            # score = fMeasure("E")
            # date.append(i)
            # date.append(score)
            # writer.writerow(date)

def confusiondata():
    model = []
    prediction = []

    with open('outputCSV/pretraiteCSV.csv') as input:
        reader = csv.reader(input)
        claims = list(reader)
        for i in claims:
            model.append(i[8])
            prediction.append(i[9])
    model=model[1:]
    prediction=prediction[1:]
    print(len(model))
    print(len(prediction))

    matrx = np.zeros(4)
    for i in range(len(model)):
        if model[i]=="E":
            if prediction[i]=="E":
                matrx[0,0]+=1
            if prediction[i]=="E*":
                matrx[0,1]+=1
            if prediction[i]=="ST":
                matrx[0,2]+=1
            if prediction[i]=="N":
                matrx[0,3]+=1
        elif model[i]=="E*":
            if prediction[i]=="E":
                matrx[1,0]+=1
            if prediction[i]=="E*":
                matrx[1,1]+=1
            if prediction[i]=="ST":
                matrx[1,2]+=1
            if prediction[i]=="N":
                matrx[1,3]+=1
        if model[i]=="ST":
            if prediction[i]=="E":
                matrx[2,0]+=1
            if prediction[i]=="E*":
                matrx[2,1]+=1
            if prediction[i]=="ST":
                matrx[2,2]+=1
            if prediction[i]=="N":
                matrx[2,3]
        if model[i]=="N":
            if prediction[i]=="E":
                matrx[3,0]+=1
            if prediction[i]=="E*":
                matrx[3,1]+=1
            if prediction[i]=="ST":
                matrx[3,2]+=1
            if prediction[i]=="N":
                matrx[3,3]+=1
    print(matrx)

confusiondata()
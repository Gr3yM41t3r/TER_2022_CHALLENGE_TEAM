
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import unicodedata
import inflect
import re
from sklearn.feature_extraction.text import TfidfVectorizer
import string
from nltk.stem import PorterStemmer
from nltk.stem import LancasterStemmer
from nltk.stem import SnowballStemmer

from similarityDetector import cosine_similarity

stop_words = nltk.corpus.stopwords.words('english')
newStopWords = ['says','say','said','an','000','hr']
stop_words.extend(newStopWords)


def pre_process(text):
    text = text.translate(str.maketrans('', '', string.punctuation))
    text = [word for word in text.split() if word.lower() not in stop_words]
    words = ""
    for i in text:
            stemmer = SnowballStemmer('english')
            words += (stemmer.stem(i))+" "
    return words



def remove_non_ascii(text):
    words = ""
    for word in text.split() :
        new_word = unicodedata.normalize('NFKD', word).encode('ascii', 'ignore').decode('utf-8', 'ignore')
        words +=new_word+" "

    return words



def to_lowercase(text):
    words = ""
    for word in text.split() :
        new_word = word.lower()
        words +=new_word+" " 
    return words

def remove_punctuation(text):
    words = ""
    for word in text.split() :
        new_word = re.sub(r'[^\w\s]', '', word)
        if new_word != '':
            words +=new_word+" "
    return words

def replace_numbers(text):
    p = inflect.engine()
    words = ""
    for word in text.split() :
        if word.isdigit():
            new_word = p.number_to_words(word)
            words +=new_word+" "
        else:
            words +=word+" "
    return words


def remove_stopwords(text):
    words = ""
    for word in text.split() :
        if word not in stop_words:
            words +=word+" "
    return words


def normalize(words):
    pre_process(words)
    words = remove_non_ascii(words)
    words = to_lowercase(words)
    words = replace_numbers(words)
    words = remove_punctuation(words)
    words = remove_stopwords(words)
    return words



a="Marco Rubio says Iran deal means we have to help defend Iran from Israel or other allies 2005 "
b="Trump says Iran deal forces U.S. to defend Iran if it's attacked by Israel"
ta =pre_process(a)
tb =pre_process(b)

pa = normalize(ta)
pb = normalize(tb)
print(pa)

corpus=[]
tfidf_vectorizer = TfidfVectorizer()

corpus.append(pa)
corpus.append(pb)
tfidf_matrix = tfidf_vectorizer.fit_transform(corpus)
cosine = cosine_similarity(tfidf_matrix, tfidf_matrix)
tfidf_value = cosine[0][1]
print(tfidf_value)


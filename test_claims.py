import numpy as np
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer
from nltk.util import ngrams  # This is the ngram magic
from sklearn.feature_extraction.text import TfidfVectorizer
from pretraitement import *
from fmeasures import fMeasure
from similarityDetector import *
tfidf_vectorizer = TfidfVectorizer()

claim1 = "Mike_Pence,Angie's_List,Religious_Freedom_Restoration_Act_(Indiana),Bill_Clinton,Religious_Freedom_Restoration_Act,Barack_Obama,Religious_Freedom_Restoration_Act,Illinois_Senate,Religious_Freedom_Restoration_Act_(Indiana),Native_Americans_in_the_United_States,Religious_Freedom_Restoration_Act,Religious_Freedom_Restoration_Act,Liberty,_Arizona,Jan_Brewer,Same-sex_marriage,Religious_Freedom_Restoration_Act,Indiana_University_Maurer_School_of_Law,University_of_Illinois_College_of_Law,Same-sex_marriage,The_Indianapolis_Star,Human_Rights_Campaign,Human_Rights_Campaign,Douglas_Laycock,University_of_Virginia,Indiana_Senate,American_Civil_Liberties_Union,American_Civil_Liberties_Union,Religious_Freedom_Restoration_Act,Barack_Obama,Barack_Obama,Religious_Freedom_Restoration_Act"
claim2 = "Religious_Freedom_Restoration_Act,Mike_Pence,Jeb_Bush,Hugh_Hewitt,Bill_Clinton,Religious_Freedom_Restoration_Act,Religious_Freedom_Restoration_Act,American_Civil_Liberties_Union,Laconic_phrase,Lawton_Chiles,Bob_Butterworth,Douglas_Laycock,Jewish_Renewal,New_Mexico_Supreme_Court,Religious_Freedom_Restoration_Act,University_of_Illinois_College_of_Law,Religious_Freedom_Restoration_Act,Religious_Freedom_Restoration_Act_(Indiana)"
corpuskeywords =[]
corpuskeywords.append(claim1)
corpuskeywords.append(claim2)
tfidf_matrix = tfidf_vectorizer.fit_transform(corpuskeywords)
cosine = cosine_similarity(tfidf_matrix, tfidf_matrix)
tfidf_key_value = cosine[0][1]
print(tfidf_key_value)
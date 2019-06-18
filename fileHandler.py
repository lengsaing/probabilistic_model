import os  
import string
import re
import glob 
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

nltk.download('punkt')
nltk.download('stopwords')

en_stops = set(stopwords.words('english'))
porter_stemmer = PorterStemmer()

#print(en_stops)

fileArray = list(glob.glob('20_newsgroup/**', recursive=True))

fileArray = fileArray[:4] #iterate to 5 documents
for filePath in fileArray:
    if(os.path.isfile(filePath)):
        f = open(filePath, "r")
        nltk_tokens=list()
        f1 = f.readlines()[17:]
        for x in f1:
            token_list = nltk.word_tokenize(x)
            for w in token_list:
                #checks if each word is not a stopword
                if w not in en_stops:
                    #stem word and append it to nltk_tokens
                    nltk_tokens.append(porter_stemmer.stem(w)) 

        for word in nltk_tokens:
            if(re.match(r"[^a-zA-Z0-9]+", word)):
                nltk_tokens.remove(word)
        
        print(nltk_tokens)
    else: 
        print("{} is a directory".format(filePath))

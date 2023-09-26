from nltk.tokenize import word_tokenize, PunktSentenceTokenizer
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from nltk.corpus import wordnet
from collections import Counter
from nltk.stem import PorterStemmer
from nltk import RegexpParser, Tree
from nltk import pos_tag
import re

# The text to process
input = "<p>As an Arizona Community College, YC serves the residents of Yavapai County by providing educational, economic development, a technical school education and cultural enrichment opportunities and resources at six campuses and centers throughout the district. Approximately 40% of YC’s entire curriculum is available via online learning.</p>"

# Uses the wordnet function of nltk to compute the most likely part of speach (noun, verb, adjective, or adverb) of each word
def get_part_of_speech(word):
  probable_part_of_speech = wordnet.synsets(word)
  
  pos_counts = Counter()

  pos_counts["n"] = len(  [ item for item in probable_part_of_speech if item.pos()=="n"]  )
  pos_counts["v"] = len(  [ item for item in probable_part_of_speech if item.pos()=="v"]  )
  pos_counts["a"] = len(  [ item for item in probable_part_of_speech if item.pos()=="a"]  )
  pos_counts["r"] = len(  [ item for item in probable_part_of_speech if item.pos()=="r"]  )
  
  most_likely_part_of_speech = pos_counts.most_common(1)[0][0]
  return most_likely_part_of_speech

# Tokenize an input first by sentence, then by individual word
def word_sentence_tokenize(text):
  
  sentence_tokenizer = PunktSentenceTokenizer(text)
  sentence_tokenized = sentence_tokenizer.tokenize(text)
  word_tokenized = list()
  
  for tokenized_sentence in sentence_tokenized:
    word_tokenized.append(word_tokenize(tokenized_sentence))
    
  return word_tokenized

# Remove the html and periods, then lower the case
string = re.sub(r'(</*p>|\.|\,)','', input)
string = string.lower()

# Sentence tokenize, then word tokenize
print(string)
fullyTokenized = word_sentence_tokenize(string)

# Tokenize (by word) the input and remove stopwords
stop_words = set(stopwords.words('english'))
string = word_tokenize(string)
string = [word for word in string if word not in stop_words]

#Stemming
#ps = PorterStemmer()
#string = [ps.stem(word) for word in string]

#POS tagging
posTaggedString = []
for token in fullyTokenized:
  posTaggedString.append(pos_tag(token))
#print(posTaggedString)

#Lemmatize by calculating most likely part of speach
#A lemmatizer works smarter than a stemmer by using POS tagging
lemmy = WordNetLemmatizer()
string = [lemmy.lemmatize(word, get_part_of_speech(word)) for word in string]
print(string)

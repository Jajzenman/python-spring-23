import nltk from nltk.book
from nltk.stem import WordNetLemmatizer

import nltk 
from nltk.corpus import stopwords
import urllib

# first, below this cell, select and clean your texts
# Dracula
# https://www.gutenberg.org/files/345/345-h/345-h.htm

DraculaURL = "https://www.gutenberg.org/files/345/345-h/345-h.htm"

# Frankenstein
# https://www.gutenberg.org/files/6542/6542-index.htm

FrankURL = "https://www.gutenberg.org/files/6542/6542-index.htm"


open_url = urllib.request.urlopen(DraculaURL)
print( "result code: " + str(open.url.getcode()))
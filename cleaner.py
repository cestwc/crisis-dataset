import preprocessor as p
p.set_options(p.OPT.URL, p.OPT.EMOJI)

import nltk
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('words')
from nltk.corpus import words
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, TweetTokenizer
 
stop_words = set(stopwords.words('english'))
	
import re

class TweetCleaner():
	def __init__(self, punct_remove = True, stopwords_remove = True, keep_en_only = False, long_word_remove = True, disabbreviate = True):
		self.punct = punct_remove
		self.stop = stopwords_remove
		self.en = set([w.lower() for w in words.words()]) if keep_en_only else None
		self.long = long_word_remove
		self.disabbr = disabbreviate
		self.tt = TweetTokenizer()

	def __call__(self, tweet):
		tweet = p.clean(tweet)
		if self.punct:
			tweet = remove_punct(tweet)
		if self.disabbr:
			tweet = disabbreviate(tweet)
		if self.en or self.stop or self.long:
			tokens = self.tt.tokenize(tweet)
			tokens = [w for w in tokens if (w not in stop_words or not self.stop) and ((len(w) > 3 and len(w) < 20) or not self.long)]
			if self.en:
				tokens = [w for w in tokens if w in self.en or '#' in w or '@' in w]
			tweet = ' '.join(tokens)
		return tweet


def remove_punct(text):
	new_words = []
	for word in text:
		w = re.sub(r'[^\w\s#@]','',word) 
		w = re.sub(r'\_|\d',' ',w)
		new_words.append(w)
	return ''.join(new_words).lower()
					  

def disabbreviate(text):

	text = str(text)
	text = text.lower()
	text = re.sub(r'\'s',r'\tis',text)
	text = re.sub(r'\'ll',r'\twill',text)
	text = re.sub(r'\'m',r'\tam',text)
	text = re.sub(r'\'re',r'\tare',text)
	text = re.sub(r'\'d',r'\twould',text)
	text = re.sub(r'n\'t',r'\tnot',text)
	# 	text = re.sub('[^a-zA-Z0-9]',' ',text) 
	# 	text = re.sub(r"[-()\"/;:<>{}`+=~|.!?,]", "", text) ##@
	return text

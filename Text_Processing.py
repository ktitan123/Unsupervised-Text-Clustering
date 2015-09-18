
from random import randint

def remove_stopwords(wordslist):
	stop_words=["and","the","a","an","in","on","at","they","if","is","are","or"]
	new_wordslist=[]
	for word in wordslist:
		if word not in stop_words:
			new_wordslist.append(word)
	return new_wordslist


def get_words(text):
	sentences = text.split(".")
	tokens=[]
	for sentence in sentences:
		words = sentence.split(" ")
		tokens.append(words)
	return tokens



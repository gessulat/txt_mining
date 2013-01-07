import cPickle
from stemming.porter2 import stem
from fish import ProgressFish
from nltk.tokenize import wordpunct_tokenize

def main():
	dictionary = open('../words.pickle', 'w')
	stemmed_abstracts_file = open('../stemmed_abstracts.pickle', 'w')
	abstracts = cPickle.load(open('../english_abstracts.pickle'))
	words = []
	stemmed_abstracts = {}

	fish = ProgressFish(total=len(abstracts))
	cnt = 0
	print "reading all words"
	for (key, abstract) in abstracts.items():
		sentence = wordpunct_tokenize(abstract.lower())
		new_sentence = []
		for word in sentence:
			if word.isalnum():
				stemmed_word = stem(word)
				words.append( stemmed_word )
				new_sentence.append( stemmed_word )
		stemmed_abstracts[key] = list(set(new_sentence))
		cnt += 1
		fish.animate(amount=cnt)

	print "removing duplicates"
	words = set(words)
	cPickle.dump(words, dictionary)

	print "persisting data"
	
	cPickle.dump(stemmed_abstracts, stemmed_abstracts_file)

if __name__ == "__main__":
	main()
import pickle
from stemming.porter2 import stem
from fish import ProgressFish
from nltk.tokenize import wordpunct_tokenize
def main():
	out = open('../words.pickle', 'w')
	abstracts = pickle.load(open('../dense_abstracts.pickle'))
	words = []

	fish = ProgressFish(total=len(abstracts))
	cnt = 0
	print "reading all words"
	for (key, abstract) in abstracts.items():
		sentence = wordpunct_tokenize(abstract.lower())
		for word in sentence:
			if word.isalnum():
				words.append( stem(word) )
		cnt += 1
		fish.animate(amount=cnt)

	print "removing duplicates"
	words = set(words)
	pickle.dump(words, out)


if __name__ == "__main__":
	main()
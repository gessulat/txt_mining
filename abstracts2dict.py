import pickle
from stemming.porter2 import stem

def main():
	out = file('../words.pickle', 'w')
	abstracts = pickle.load('abstracts.pickle')
	words = []
	print "reading all words"
	for (key, abstract) in abstracts.items():
		for word in abstract:
			words.append( stem(word) )
	print "removing duplicates"
	words = set(words)
	pickle.dump(words, out)


if __name__ == "__main__":
	main()
import cPickle, argparse
from stemming.porter2 import stem
from fish import ProgressFish
from nltk.tokenize import wordpunct_tokenize

def main():
	parser = argparse.ArgumentParser()
	parser.add_argument('in_abs', help='input abstracts file path: "../*_abstracts.pickle" ')
	parser.add_argument('out_stemmed_abs', default='../stemmed_abstracts.pickle', help='file path of abstracts output file: "stemmed_abstracts.pickle"')
	parser.add_argument('out_words', default='../word_base.pickle', help='file path of words output file: "word_base.pickle"')

	args = parser.parse_args()

	word_base = open(args.out_words, 'w')
	stemmed_abstracts_file = open(args.out_stemmed_abs, 'w')
	abstracts = cPickle.load(open(args.in_abs))

	print "loading pickles..."
	
	words = []
	stemmed_abstracts = {}

	fish = ProgressFish(total=len(abstracts))
	cnt = 0
	print "reading all words..."
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
	cPickle.dump(words, word_base)

	print "persisting data"
	
	cPickle.dump(stemmed_abstracts, stemmed_abstracts_file)

if __name__ == "__main__":
	main()
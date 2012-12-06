import argparse

def run( ):
	absFile = open('../abstracts.txt')
	idFile   = open('../words.txt')
	outFile = open('../new_abs_vectors.txt', 'w')



	ids = {}
	print 'reading words and building dictionary...'

	counter = 0
	dictionary = {}
	word_list = idFile.read().split(" ")
	for word in word_list:
		dictionary[word] = counter
		counter = counter+1


	print '...everything in main memory, sire!\n'

	print 'writing adjacency lists for abstracts'
	for line in absFile:
		abstract = line.split(" ",1)[1]
		abstr_dict = {}
		for abstract_word in abstract.split(" "):
			word = ''.join(e for e in abstract_word if e.isalnum() )
			word_id = dictionary[word]
			if word_id in abstr_dict:
				abstr_dict[word_id] = abstr_dict[word_id]+1
			else:
				abstr_dict[word_id] = 1
		outFile.write(str(abstr_dict)+"\n")






def main():
	run()

if __name__ == "__main__":
	main()
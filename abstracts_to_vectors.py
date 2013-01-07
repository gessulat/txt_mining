from numpy import array, zeros

word_base = ('hallo', 'welt', 'bla', 'blupp', 'muh', 'haus', 'test', 'narf')
abstract = ('hallo', 'hallo', 'bla', 'bla', 'bla', 'bla', 'narf')

def abstract_to_vector( abstract, word_base_dict):
	vector_dict = {}
	for word in abstract:
		if word in vector_dict:
			vector_dict[word] += 1
		else:
			vector_dict[word] = 1

	vector = zeros( len(word_base_dict) )
	for word, cnt in vector_dict.items():
		vector[word_base_dict[word]] = cnt

	return vector

def main():
	cnt = 0
	word_base_dict = {}
	for word in word_base:
		word_base_dict[word] = cnt
		cnt +=1

	print 'word_base: ' + str(word_base)
	print 'abstract: ' + str(abstract)
	print abstract_to_vector( abstract, word_base_dict)

	


if __name__ == "__main__":
	main()
import cPickle, argparse
from numpy import array, zeros
from fish import ProgressFish

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

def abstracts_to_vector( abstracts, word_base):
	
	print 'converting abstracts...'
	cnt = 0
	word_base_dict = {}
	for word in word_base:
		word_base_dict[word] = cnt
		cnt +=1

	cnt = 0
	fish = ProgressFish(total=len(abstracts))
	for key, abstract in abstracts.items():
		vector_abstract = abstract_to_vector( abstract, word_base_dict)
		abstracts[key] = vector_abstract
		cnt += 1
		fish.animate(amount=cnt)

	return abstracts


def main():

	parser = argparse.ArgumentParser()
	parser.add_argument('in_abs', help='input abstracts file path: "../stemmed_abstracts.pickle" ')
	parser.add_argument('in_wb', help='input abstracts file path: "../word_base.pickle" ')
	parser.add_argument('out_abs', help='file path of abstracts output file: "vector_abstracts.pickle"')

	args = parser.parse_args()
	
	print 'loading abstracts...'
	abs_file = open(args.in_abs)
	abstracts = cPickle.load(abs_file)
	abs_file.close()

	print 'loading word_base'
	wb_file = open(args.in_wb)
	word_base = cPickle.load(wb_file)
	wb_file.close()

	vector_abstracts = abstracts_to_vector( abstracts, word_base)
	
	print 'persist vector abstracts'
	output_file = open(args.out_abs,'w')
	cPickle.dump( vector_abstracts, output_file, -1 )
	output_file.close()
	




	


if __name__ == "__main__":
	main()
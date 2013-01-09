
import cPickle, argparse
from numpy import array, zeros
from fish import ProgressFish
from scipy.spatial import distance

## cosine dist example
u = array( [1,0,6] )
v = array( [1,5,6] )
distance.cosine(u, v)

def abstract_to_vector( abstract, word_base_dict ):
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

def new_calc_cosine( abstracts, keys, word_base, buffer_length ):
	cnt = 0
	word_base_dict = {}
	for word in word_base:
		word_base_dict[word] = cnt
		cnt +=1

	print 'filling buffer with vectors...'
	fish = ProgressFish(total=buffer_length)
	vector_dict = {}
	for i in range(buffer_length):
		vector_dict[keys[i]] = abstract_to_vector( abstracts[i], word_base_dict )
		fish.animate(amount=i)


	print 'calculating distances'
	no_of_docs = len(abstracts)
	matrix = zeros( (no_of_docs, no_of_docs) )
	fish = ProgressFish(total=no_of_docs*no_of_docs)
	# generate vectors on the fly if not in vector_dict
	for i in range(no_of_docs):
		# save u for all js and don't calculate it again
		# search if abs_i is in vector_dict
		if keys[i] not in vector_dict:
			u = abstract_to_vector( abstracts[i], word_base_dict) # just one time 
		else:
			u = vector_dict[keys[i]]

		for j in range(no_of_docs-i):	# do only half the work...
			if keys[j] not in vector_dict:
				v = abstract_to_vector( abstracts[j], word_base_dict)
			else:
				v = vector_dict[keys[j]]
			matrix[i][j] = distance.cosine(u,v)
			del v
			fish.animate(amount=(i*no_of_docs)+j+1)
	
	return matrix


def main():

	parser = argparse.ArgumentParser()
	parser.add_argument('in_abs_stemmed', help='input stemmed abstracts list file path: "../stemmed_abstracts.list" ')
	parser.add_argument('in_keys', help='input keys list file path: "../keys.list" ')
	parser.add_argument('in_word_base', help='input word_base file path: "../word_base.list" ')
	parser.add_argument('out_cosDist_mat', help='file path of abstracts output file: "cosine_distances.pickle"')
	parser.add_argument('buffer_size', help='big if your ram is big, small if your ram is small. i.e. 20000, 100')


	args = parser.parse_args()
	
	print 'loading abstracts list...'
	abs_file = open(args.in_abs_stemmed)
	abstracts = cPickle.load(abs_file)
	abs_file.close()

	print 'loading word base list...'
	keys_file = open(args.in_keys)
	keys = cPickle.load(keys_file)
	keys_file.close()

	print 'loading key list...'
	wb_file = open(args.in_word_base)
	word_base = cPickle.load(wb_file)
	wb_file.close()

	cosine_distances = new_calc_cosine( abstracts, keys, word_base, int(args.buffer_size) )
	
	print 'persist cosine distance matrix'
	output_file = open(args.out_cosDist_mat,'w')
	cPickle.dump( cosine_distances, output_file, -1 )
	output_file.close()
	

if __name__ == "__main__":
	main()
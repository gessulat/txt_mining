
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

def calc_cosine_dists( abstracts, word_base ):
	cnt = 0
	word_base_dict = {}
	for word in word_base:
		word_base_dict[word] = cnt
		cnt +=1

	no_of_docs = len(abstracts)
	matrix = zeros( (no_of_docs, no_of_docs) )
	fish = ProgressFish(total=no_of_docs*no_of_docs)
	for i in range(no_of_docs):
		u = abstract_to_vector( abstracts[i], word_base_dict) # just one time 
		for j in range(no_of_docs-i):	# do just half the work...
			# and do it on-the-fly to save RAM!
			v = abstract_to_vector( abstracts[j], word_base_dict)
			matrix[i][j] = distance.cosine(u,v)
			del v
			fish.animate(amount=(i*no_of_docs)+j+1)
	return matrix


def main():

	parser = argparse.ArgumentParser()
	parser.add_argument('in_vector_abs', help='input vector abstracts file path: "../stemmed_abstracts.pickle" ')
	parser.add_argument('in_word_base', help='input word_base file path: "../word_base.list" ')
	parser.add_argument('out_cosDist_mat', help='file path of abstracts output file: "cosine_distances.pickle"')

	args = parser.parse_args()
	
	print 'loading abstracts list...'
	abs_file = open(args.in_vector_abs)
	abstracts = cPickle.load(abs_file)
	abs_file.close()

	print 'loading word base list...'
	wb_file = open(args.in_word_base)
	word_base = cPickle.load(wb_file)
	wb_file.close()

	cosine_distances = calc_cosine_dists( abstracts, word_base )
	
	print 'persist cosine distance matrix'
	output_file = open(args.out_cosDist_mat,'w')
	cPickle.dump( cosine_distances, output_file, -1 )
	output_file.close()
	

if __name__ == "__main__":
	main()
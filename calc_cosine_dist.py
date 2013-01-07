
import cPickle, argparse
from numpy import array, zeros
from fish import ProgressFish
from scipy.spatial import distance


## example
u = array( [1,0,6])
v = array( [1,5,6])
distance.cosine(u, v)

def calc_cosine_dists( abstracts, word_base ):
	no_of_docs = len(abstracts)
	matrix = zeros( (no_of_docs, no_of_docs) )


def main():

	parser = argparse.ArgumentParser()
	parser.add_argument('in_vector_abs', help='input vector abstracts file path: "../vector_abstracts.pickle" ')
	parser.add_argument('in_wb', help='input word_base file path: "../word_base.pickle" ')
	parser.add_argument('out_cosDist_mat', help='file path of abstracts output file: "cosine_distances.pickle"')

	args = parser.parse_args()
	
	print 'loading abstracts...'
	abs_file = open(args.in_vector_abs)
	abstracts = cPickle.load(abs_file)
	abs_file.close()

	print 'loading word_base'
	wb_file = open(args.in_wb)
	word_base = cPickle.load(wb_file)
	wb_file.close()

	cosine_distances = calc_cosine_dists( abstracts, word_base)
	
	print 'persist vector abstracts'
	output_file = open(args.out_abs,'w')
	cPickle.dump( cosine_distances, output_file, -1 )
	output_file.close()
	

if __name__ == "__main__":
	main()
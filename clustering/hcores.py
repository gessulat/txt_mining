import cPickle, argparse
from numpy import *
from scipy.spatial import distance

def count_by_weight( dissim_matrix, weight ):
	D = []
	for row in range(0, len(dissim_matrix),1):
		#D_row = reduce(lambda x,y: x+1 if y>=weight else x, dissim_matrix[row,:] )
		D_row = len( [x for x in dissim_matrix[row,:] if x>=weight] )
		D.append(D_row)
	return D

def get_k(importance_list):
	for h in range( int(max(importance_list)), 0, -1 ):
		h_count = len([x for x in importance_list if x >= h])
		if h_count >= h:
			return h
	return None


def main():

	parser = argparse.ArgumentParser()
	parser.add_argument('in_r', help='Parameter r" ')
	parser.add_argument('in_dissim_matrix', default='../dissim_matrix_hybrid.pickle', help='The dissimilarity-Matrix to be used as a pickled Numpy-Array')
	parser.add_argument('out_cores', default='../h_cores_as_indexes.pickle', help='file path of words output file: "../h_cores_as_indexes.pickle"')

	args = parser.parse_args()

	dissim_matrix = cPickle.load(open(args.in_dissim_matrix))
	dissim_matrix = distance.squareform(dissim_matrix, checks=True)
	r = float(args.in_r)

	importance_list = count_by_weight(dissim_matrix, r)
	k = get_k(importance_list)
	cores = [ i for i in range(0,len(importance_list)) if importance_list[i]>=k s]
	
	#print dissim_matrix
	#print 'Number of Documents that are farer away than r /* r =', r, '*/, per Document: ', importance_list
	print 'calculated k is:', k
	print 'Cores are (Indexes):', cores

	savetxt(args.out_cores, array(cores, float))

	return cores

if __name__ == "__main__":
	main()
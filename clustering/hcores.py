import cPickle, argparse
from numpy import *

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

	#dissim_matrix = cPickle.load(args.in_dissim_matrix)
	# ignore input for the moment
	#r = args.in_r
	r = int(args.in_r)
	dissim_matrix = array([[0,0.5,1,0,5,0],[0,0.99,2,0,1,3]])

	importance_list = count_by_weight(dissim_matrix, r)
	k = get_k(importance_list)
	cores = [ i for i in range(0,len(importance_list)) if importance_list[i]>=k ]
	
	print dissim_matrix
	print 'Number of Documents that are farer away than r /* r =', r, '*/, per Document: ', importance_list
	print 'calculated k is:', k
	#print get_k([8,5,3,2,1]), 'good?', get_k([8,5,3,2,1])==3 # should be 3
	print 'Cores are (Indexes):', cores


	#print 'pickle this, pickle that...'
	#cPickle.dump(cores, args.out_cores)
	return cores

if __name__ == "__main__":
	main()
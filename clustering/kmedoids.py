from Pycluster import kmedoids
from numpy import array, loadtxt, set_printoptions
from scipy.spatial import distance
import pickle, argparse

def getInit( distances, cores ):
	distances = distance.squareform(distances, checks=True)
	init = []
	for dist in distances:
		minimum = 1
		cluster = None
		for c in range(len(cores)):
			if minimum > dist[cores[c]]:
				minimum = dist[cores[c]]
				cluster = c
		init.append(cluster)
	return array(init)


def main():

	parser = argparse.ArgumentParser()
	parser.add_argument('in_dissim_matrix', default='../dissim_matrix_hybrid.pickle', help='The dissimilarity-Matrix to be used as a pickled Numpy-Array')
	parser.add_argument('in_cores', default='../h_cores_as_indexes.pickle', help='file path of cores file: "../h_cores_as_indexes.pickle"')
	parser.add_argument('in_values')
	parser.add_argument('random_init')
	args = parser.parse_args()

	f = open(args.in_dissim_matrix)
	distances = pickle.load(f)
	f.close()

	cores = loadtxt(args.in_cores)
	if args.random_init != "random":
		init = getInit( distances, cores )
	set_printoptions(threshold='nan')	
	set_printoptions(linewidth=900000000)	

	result = kmedoids(distance = distances, npass=20, nclusters=len(cores))
	#result = kmedoids(distance = distances, initialid = init)

	print args.in_values + " "+str(len(cores))+" "+str(result[1])+" "+str(result[0])
	#print args.in_values + " "+str(len(cores))+" "+str(result[1])+" "+args.random_init


if __name__ == "__main__":
    main()

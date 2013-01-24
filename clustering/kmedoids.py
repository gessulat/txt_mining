from Pycluster import kmedoids
from numpy import array, loadtxt 
from scipy.spatial import distance
import pickle, argparse

def main():

	parser = argparse.ArgumentParser()
	parser.add_argument('in_r', help='Parameter r" ')
	parser.add_argument('in_dissim_matrix', default='../dissim_matrix_hybrid.pickle', help='The dissimilarity-Matrix to be used as a pickled Numpy-Array')
	parser.add_argument('in_cores', default='../h_cores_as_indexes.pickle', help='file path of cores file: "../h_cores_as_indexes.pickle"')
	parser.add_argument('in_values')
	args = parser.parse_args()


	f = open(args.in_dissim_matrix)
	distances = pickle.load(f)
	f.close()

	cores = loadtxt(args.in_cores)

	distances = distance.squareform(distances, checks=True)
	init = []
	for dist in distances:
		minimum = 1
		cluster = None
		for core in cores:
			if minimum > dist[core]:
				minimum = dist[core]
				cluster = core
		init.append(cluster)
	init = array(init)

	for i in range(len(cores)):
		for j in range(len(init)):
			if init[j] == cores[i]:
				init[j] = i

	result = kmedoids(distance = distances, initialid = init)
	print args.in_values + " clusters: "+str(len(cores))+" error: "+str(result[1])

if __name__ == "__main__":
    main()

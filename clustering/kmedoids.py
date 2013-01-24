from Pycluster import kmedoids
from numpy import array, loadtxt 
from scipy.spatial import distance
import pickle

def initalizeClusters( hcores, distances ):	
	print len(distances)
	distances = distance.squareform(distances, checks=True)

	init = array()	
	return None

print 'loading distance matrix...'
f = open('data/mr_10k_fishDist_50.p')
distances = pickle.load(f)
f.close()




print 'loading hcores...'
cores = loadtxt('data/cores/cores_mr_10k_l50_r10.p')

print 'number of hcores'
print len(cores)

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


print 'init length: '+ str(len(init))
# unneccesary
# print 'unfold compressed matrix...'
# dist = distance.squareform(dist, checks=True)

#init = None	
print init
n = 13
passes = 1

'clustering with kmedoids'
result = kmedoids(distance = distances, initialid = init)
print result
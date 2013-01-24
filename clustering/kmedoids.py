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
cores = loadtxt('data/cores/cores_mr_10k_l50_r50.p')

distances = distance.squareform(distances, checks=True)
print len(distances)
for dist in distances:
	minimum = None
	print len(dist)



print 'cores: '+ str(len(cores))
print cores
# unneccesary
# print 'unfold compressed matrix...'
# dist = distance.squareform(dist, checks=True)

init = None	
n = 12
passes = 10

'clustering with kmedoids'
result = kmedoids(distance = dist, npass = passes, nclusters = n, initialid = init)
print result
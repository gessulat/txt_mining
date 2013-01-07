from numpy import array
from scipy.spatial import distance


## example
u = array( [1,0,6])
v = array( [1,5,6])
distance.cosine(u, v)

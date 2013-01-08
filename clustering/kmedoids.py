from nltk.cluster.util import cosine_distance
import scipy
from numpy import array

def tanimoto(a, b):
	X = array(a,b)
	scipy.spatial.distance.pdist(X,)

def generic_distance( a, b, distFunc ):
	return distFunc(a,b)


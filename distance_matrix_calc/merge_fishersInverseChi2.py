import cPickle, argparse
from numpy import arccos, cos
from copy import copy
from fish import ProgressFish
from scipy.spatial import distance

def fishers_chiSquare_method( x, y, lmbd ):
    return cos( lmbd * arccos(x)+(1-lmbd) * arccos(y) ) 

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('tanPath', help='file path: to tanimoto matrix pickle"../foo.pickle" ')
    parser.add_argument('cosPath', help='file path: to cosine matrix pickle"../foo.pickle" ')
    parser.add_argument('outPath', help='file path: to merged matrix pickle"../foo.pickle" ')
    parser.add_argument('lmbd', help='between 0 and 1')
    args = parser.parse_args()
    
    print 'loading tanimoto matrix pickle...'
    f = open(args.tanPath)
    tanMatrix = cPickle.load(f)
    f.close()
    print 'loading cosine matrix pickle...'
    f = open(args.cosPath)
    cosMatrix = cPickle.load(f)
    f.close()
    
    result = copy(cosMatrix)
    length = len(tanMatrix)
    fish = ProgressFish(total = length )
    for i in range(length):
        result[i] = fishers_chiSquare_method( cosMatrix[i], tanMatrix[i], float(args.lmbd) )
        fish.animate(amount=i)
    print 'pickling to '+args.outPath
    f = open(args.outPath, 'w')
    cPickle.dump( result, f ) 
    f.close()


if __name__ == "__main__":
    main()

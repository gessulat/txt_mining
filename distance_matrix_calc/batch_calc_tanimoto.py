
import cPickle, argparse
from numpy import array, zeros, column_stack, empty
from fish import ProgressFish
from scipy.spatial import distance

## cosine dist example
u = array( [1,0,6] )
v = array( [1,5,6] )
distance.cosine(u, v)
def ref_to_vector( ref, refs):
    tmp_array = []
    for doc_refs in refs:
        if ref in doc_refs:
            tmp_array.append(1)
        else:
            tmp_array.append(0)
    return array( tmp_array, dtype=bool)

def build_refs_base( refs ):
    refs_base = list()

    print 'building refs base...'
    for doc_refs in refs:
        for ref in doc_refs:
            refs_base.append(ref)
    refs_base = list(set(refs_base))
    return refs_base

def get_vector_list( refs, refs_base):

    fish = ProgressFish(total=len(refs_base))

    vector_list = ref_to_vector( refs_base[0], refs) # init
    for i in range(1, len(refs_base)):
        column_vector = ref_to_vector( refs_base[i],refs )
        vector_list = column_stack( [ vector_list , column_vector ] )
        fish.animate(amount=i)
    return vector_list


def calc_tanimoto( vector_list ):
    matrix = distance.pdist(vector_list, 'rogerstanimoto')
    # matrix = distance.squareform( matrix )
    print matrix
    return matrix


def main():

    parser = argparse.ArgumentParser()
    parser.add_argument('in_refs', help='input references list "../refs.list"')
    parser.add_argument('io_vectors', help='if already calculated takes the input matrix otherwise builds it. path: "../refs_vector.list" ')
    parser.add_argument('out_tanDist', help='file path of tanimoto matrix output file: "../dist_tan.pickle"')


    args = parser.parse_args()
    
    print 'loading refs list...'
    refs_file = open(args.in_refs)
    refs = cPickle.load(refs_file)
    refs_file.close()

    print 'building refs_base...'
    refs_base = build_refs_base( refs )

    print 'getting ref vector file...'
    try: 
        vectors_file = open( args.io_vectors)
        vector_list = cPickle.load(vectors_file)
        vectors_file.close()
    except:
        print '  no ref vector file found! Building it...'
        vector_list = get_vector_list( refs, refs_base)
        vectors_file = open( args.io_vectors, 'w')
        cPickle.dump(vector_list, vectors_file)
        print '  persist new ref vector file...'
        vectors_file.close()
    
    del refs
    del refs_base

    print 'calculating distances'
    tanimoto_distances = calc_tanimoto(  vector_list )
    
    print 'persist tanimoto distance matrix'
    output_file = open(args.out_tanDist,'w')
    cPickle.dump( tanimoto_distances, output_file, -1 )
    output_file.close()
    

if __name__ == "__main__":
    main()

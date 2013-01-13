
import cPickle, argparse
from numpy import array, zeros
from fish import ProgressFish
from scipy.spatial import distance

## cosine dist example
u = array( [1,0,6] )
v = array( [1,5,6] )
distance.cosine(u, v)
def refs_to_vector( doc_refs, refs_base):
    vector = zeros( len(refs_base))
    for i in range(len(refs_base)):
        if refs_base[i] in doc_refs:
            vector[i] = 1
    return vector

def calc_tanimoto( refs, keys ):
    no_of_docs = len(refs)
    refs_base = list()
    print 'building refs base...'
    for doc_refs in refs:
        for ref in doc_refs:
            refs_base.append(ref)
    refs_base = list(set(refs_base))

    print 'filling buffer with vectors...'
    cnt = 0
    fish = ProgressFish(total=no_of_docs)
    vector_list = list()
    for doc_refs in refs:
        vector_list.append( refs_to_vector( doc_refs, refs_base ))
        cnt += 1
        fish.animate(amount=cnt)
    matrix = distance.pdist(vector_list, 'rogerstanimoto')
    return matrix


def main():

    parser = argparse.ArgumentParser()
    parser.add_argument('in_refs', help='input references list "../refs.list"')
    parser.add_argument('in_keys', help='input keys list file path: "../keys.list" ')
    parser.add_argument('out_tanDist', help='file path of tanimoto matrix output file: "../dist_tan.pickle"')


    args = parser.parse_args()
    
    print 'loading refs list...'
    refs_file = open(args.in_refs)
    refs = cPickle.load(refs_file)
    refs_file.close()

    print 'loading key list...'
    keys_file = open(args.in_keys)
    keys = cPickle.load(keys_file)
    keys_file.close()

    tanimoto_distances = calc_tanimoto( refs, keys )
    
    print 'persist tanimoto distance matrix'
    output_file = open(args.out_tanDist,'w')
    cPickle.dump( cosine_distances, output_file, -1 )
    output_file.close()
    

if __name__ == "__main__":
    main()

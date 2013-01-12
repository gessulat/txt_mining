
import cPickle, argparse
from numpy import array, zeros
from fish import ProgressFish
from scipy.spatial import distance

## cosine dist example
u = array( [1,0,6] )
v = array( [1,5,6] )
distance.cosine(u, v)

def calc_tanimoto( refs, buffer_length ):
    print 'building references base list...'
    cnt = 0
    no_of_docs = len(abstracts)
    fish = ProgressFish(total=no_of_docs)
    refs_base = list()
    for doc_refs in refs:
        cnt += 1
        for ref in doc_refs:
            refs_base.append(ref)
        fish.animate(amount=cnt)
    refs_base = set(refs_base)

    print 'building vectors according to base list'
    fish = ProgressFish(total=no_of_docs)
    vector_dict = {}
    for key, doc_refs in refs.items():
        vector = zeros( len(refs_base))
        for i in range(word_base):
            if ref in doc_refs:
                vector[i] = 1

    print 'calculating distances'
    matrix = zeros( (no_of_docs, no_of_docs) )
    fish = ProgressFish(total=no_of_docs*no_of_docs)
    # generate vectors on the fly if not in vector_dict
    for i in range(no_of_docs):
        # save u for all js and don't calculate it again
        # search if abs_i is in vector_dict
        if keys[i] not in vector_dict:
            u = abstract_to_vector( abstracts[i], word_base_dict) # just one time 
        else:
            u = vector_dict[keys[i]]

        for j in range(no_of_docs-i):   # do only half the work...
            if keys[j] not in vector_dict:
                v = abstract_to_vector( abstracts[j], word_base_dict)
            else:
                v = vector_dict[keys[j]]
            matrix[i][j] = distance.cosine(u,v)
            del v
            fish.animate(amount=(i*no_of_docs)+j+1)
    
    return matrix


def main():

    parser = argparse.ArgumentParser()
    parser.add_argument('in_refs', help='input refs list file path: "../refs.pickle" ')
    parser.add_argument('out_tanDist_mat', help='file path of abstracts output file: "cosine_distances.pickle"')
    parser.add_argument('buffer_size', help='big if your ram is big, small if your ram is small. i.e. 20000, 100')


    args = parser.parse_args()
    
    print 'loading abstracts list...'
    refs_file = open(args.in_refs)
    refs = cPickle.load(refs_file)
    refs_file.close()

    cosine_distances = calc_tanimoto( refs, int(args.buffer_size) )
    
    print 'persist cosine distance matrix'
    output_file = open(args.out_cosDist_mat,'w')
    cPickle.dump( cosine_distances, output_file, -1 )
    output_file.close()
    

if __name__ == "__main__":
    main()

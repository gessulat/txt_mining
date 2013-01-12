
import cPickle, argparse
from numpy import array, zeros
from fish import ProgressFish
from scipy.spatial import distance

def refs_to_vector( doc_refs, refs_base):
    vector = zeros( len(refs_base))
    for i in range(len(refs_base)):
        if refs_base[i] in doc_refs:
            vector[i] = 1
    return vector


def calc_tanimoto( refs, keys, buffer_length ):
    print 'building references base list...'
    cnt = 0
    no_of_docs = len(refs)
    fish = ProgressFish(total=no_of_docs)
    refs_base = list()
    for doc_refs in refs:
        cnt += 1
        for ref in doc_refs:
            refs_base.append(ref)
        fish.animate(amount=cnt)
    refs_base = list(set(refs_base))
    print 'refs_base length: '+str(len(refs_base))

    print 'building buffered vectors...'
    # this does not buffer but build all vectors! 
    vector_dict = {}
    fish = ProgressFish(total=buffer_length)
    cnt = 0
    for i in range(no_of_docs):
        vector_dict[keys[i]] = refs_to_vector( refs[i], refs_base ) 
        cnt +=1 
        fish.animate(amount=cnt)
        if cnt == buffer_length:
            break

    print 'calculating distances...'
    matrix = zeros( (no_of_docs, no_of_docs) )
    fish = ProgressFish(total=no_of_docs*no_of_docs)
    # generate vectors on the fly if not in vector_dict
    for i in range(no_of_docs):
        # save u for all js and don't calculate it again
        # search if abs_i is in vector_dict
        if keys[i] not in vector_dict:
            u = refs_to_vector( refs[i], refs_base) # just one time 
        else:
            u = vector_dict[keys[i]]

        for j in range(no_of_docs-i):   # do only half the work...
            if keys[j] not in vector_dict:
                v = refs_to_vector( refs[j], refs_base) # just one time 
            else:
                v = vector_dict[keys[j]]
            matrix[i][j] = distance.rogerstanimoto(u,v)
            del v
            fish.animate(amount=(i*no_of_docs)+j+1)
    
    return matrix


def main():

    parser = argparse.ArgumentParser()
    parser.add_argument('in_refs', help='input refs list file path: "../refs.list" ')
    parser.add_argument('in_keys', help='input key list file path: "../keys.list" ')
    parser.add_argument('out_tanDist_mat', help='file path of tanimoto dist output file: "tanimoto_dist.pickle.pickle"')
    parser.add_argument('buffer_size', help='big if your ram is big, small if your ram is small. i.e. 20000, 100')


    args = parser.parse_args()
    
    print 'loading abstracts list...'
    refs_file = open(args.in_refs)
    refs = cPickle.load(refs_file)
    refs_file.close()

    print 'loading keys list...'
    keys_file = open(args.in_keys)
    keys = cPickle.load(keys_file)
    keys_file.close()


    cosine_distances = calc_tanimoto( refs, keys,int(args.buffer_size) )
    
    print 'persist cosine distance matrix'
    output_file = open(args.out_cosDist_mat,'w')
    cPickle.dump( cosine_distances, output_file, -1 )
    output_file.close()
    

if __name__ == "__main__":
    main()


import cPickle, argparse
from numpy import array, zeros
from fish import ProgressFish
from scipy.spatial import distance

## cosine dist example
u = array( [1,0,6] )
v = array( [1,5,6] )
distance.cosine(u, v)

def abstract_to_vector( abstract, word_base_dict ):
    vector_dict = {}
    for word in abstract:
        if word in vector_dict:
            vector_dict[word] += 1
        else:
            vector_dict[word] = 1
    vector = zeros( len(word_base_dict) )
    for word, cnt in vector_dict.items():
        vector[word_base_dict[word]] = cnt
    return vector

def calc_cosine( abstracts, keys, word_base ):
    cnt = 0
    word_base_dict = {}
    for word in word_base:
        word_base_dict[word] = cnt
        cnt +=1

    print 'filling buffer with vectors...'
    vector_list = list()
    for abstract in abstracts:
        vector_list.append( abstract_to_vector( abstract, word_base_dict ))
    matrix = distance.pdist(vector_list, 'cosine')
    return matrix


def main():

    parser = argparse.ArgumentParser()
    parser.add_argument('in_abs_stemmed', help='input stemmed abstracts list file path: "../stemmed_abstracts.list" ')
    parser.add_argument('in_keys', help='input keys list file path: "../keys.list" ')
    parser.add_argument('in_word_base', help='input word_base file path: "../word_base.list" ')
    parser.add_argument('out_cosDist_mat', help='file path of abstracts output file: "cosine_distances.pickle"')


    args = parser.parse_args()
    
    print 'loading abstracts list...'
    abs_file = open(args.in_abs_stemmed)
    abstracts = cPickle.load(abs_file)
    abs_file.close()

    print 'loading word base list...'
    keys_file = open(args.in_keys)
    keys = cPickle.load(keys_file)
    keys_file.close()

    print 'loading key list...'
    wb_file = open(args.in_word_base)
    word_base = cPickle.load(wb_file)
    wb_file.close()

    cosine_distances = calc_cosine( abstracts, keys, word_base, )
    
    print 'persist cosine distance matrix'
    output_file = open(args.out_cosDist_mat,'w')
    cPickle.dump( cosine_distances, output_file, -1 )
    output_file.close()
    

if __name__ == "__main__":
    main()

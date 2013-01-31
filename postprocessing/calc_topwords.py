import pickle, argparse

def main():

    parser = argparse.ArgumentParser()
    parser.add_argument('in_results', help='path to result file" ')
    parser.add_argument('in_abstracts', help='path to abstracts list file" ')
    args = parser.parse_args()

    # load results file
    print 'load results file'
    f = open(args.in_results)
    f.readline()
    line = f.readline().split()
    f.close()
    dataset = line[0]
    lvalue = line[1]
    rvalue = line[2]
    core_num = line[3]
    errorvalue = line[4]
    categorized_docs = line[5:]
    print 'dataset lambda r'
    print dataset, lvalue, rvalue
    categorized_docs[0] = categorized_docs[0][1:]
    categorized_docs[-1] = categorized_docs[-1][:-1]
    centroids = list(set(categorized_docs))
    print centroids

    # load abstracts
    print 'load abstracts'
    f = open(args.in_abstracts)
    abstracts = pickle.load(f)
    f.close()

    # init centroids dict
    print 'build centroid word lists'
    centroid_words = dict()
    for centroid in centroids:
        c = int(centroid)
        centroid_words[c]=[]
     
    for i in range(len(abstracts)):
        c = int(categorized_docs[i])
        for word in abstracts[i]:
            centroid_words[c].append(word)

    print 'building centroid sets'
    centroid_sets = dict()
    for centroid, abstract in centroid_words.items():
        centroid_sets[centroid] = dict()
        word_set = list(set(abstract))
        for word in word_set:
            centroid_sets[centroid][word]=0
    
    for doc in range(len(categorized_docs)):
        centroid = int(categorized_docs[doc])
        abstract = abstracts[doc]
        for word in abstract:
            centroid_sets[centroid][word] += 1


    print 'done!'



if __name__ == "__main__":
    main()
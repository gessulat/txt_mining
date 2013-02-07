import pickle, argparse, operator

def main():

    parser = argparse.ArgumentParser()
    parser.add_argument('in_results', help='path to result file" ')
    parser.add_argument('in_abstracts', help='path to abstracts list file" ')
    parser.add_argument('in_stop', help='path to stop word file" ')
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
    for centroid, word_list in centroid_words.items():
        centroid_sets[centroid] = dict()
        word_set = list(set(word_list))
        for word in word_set:
            centroid_sets[centroid][word]=0
    
    # centroid_set_init = dict()
    # for centroid, word_list in centroid_words.items():
    #     centroid_set_init[centroid] = set(word_list)

    # centroid_sets = dict()
    # for centroid, c_set in centroid_set_init.items():
    #     centroid_sets[centroid] = c_set
    #     for other_c, other_c_set in centroid_set_init.items():
    #         if other_c != centroid:
    #             centroid_sets[centroid] = centroid_sets[centroid].difference( other_c_set)
        
    #     init_set = list(centroid_sets[centroid])
    #     centroid_sets[centroid] = {}
    #     for word in init_set:
    #         centroid_sets[centroid][word]=0

    print 'count words'
    for doc in range(len(categorized_docs)):
        centroid = int(categorized_docs[doc])
        abstract = abstracts[doc]
        for word in abstract:
            if word in centroid_sets[centroid]:
                centroid_sets[centroid][word] += 1

    print 'sort words'
    word_lists = {}
    for centroid in centroids:
        wl = sorted(centroid_sets[int(centroid)].iteritems(), key=operator.itemgetter(1))
        word_lists[centroid] = wl
   
    print 'read stop words'
    f = open(args.in_stop)
    stop_words = f.readlines()
    f.close()
    for i in range(len(stop_words)):
        stop_words[i] = str.strip(stop_words[i])

    how_many_top = 10

    for centroid in centroids:
        print 'top '+str(how_many_top)+' words for centroid: '+centroid
        print '---'
        top_list = []
        for i in range(1, len(word_lists[centroid])):
            word = word_lists[centroid][-i]
            if word[0] not in stop_words:
                top_list.append(word)
            if len(top_list) >= how_many_top:
                break
        # print top_list
        for tupel in top_list:
            word, cnt = tupel
            print word
        print '===='



if __name__ == "__main__":
    main()
import cPickle
from datetime import datetime
from guess_language import guessLanguage

def main():
	source = open("../dense_abstracts.pickle")
	out_file = open('../english_abstracts.pickle', 'w')
	out_diff = open('../english_abstracts_diff.pickle', 'w')
	print str(datetime.now())+ "filterNonEnglishAbstracts.py - deletes entries with non-English abstracts "

	if not source:
		print "This works.... NOT"
		return -1
	
	deleted_abstract_ids = []
	print "reading abstracts..."
	abstracts = cPickle.load(source)
	abs_tobeginwith = float(len(abstracts))

	print "deleting non-English ones"
	empty_cnt = 0
	for article_id, abstract in abstracts.items():
		if 'en' != guessLanguage( abstract ):
			empty_cnt += 1
			deleted_abstract_ids.append(article_id)
			del abstracts[article_id]

	print str(datetime.now())+' starting to persist references to: '+ out_file.name +' and '+out_diff.name
	print "deleted "+str(empty_cnt)+" documents"
	print "that's "+str( empty_cnt / abs_tobeginwith )+"%"

	cPickle.dump(abstracts, out_file, -1)
	cPickle.dump(deleted_abstract_ids, out_diff, -1)

	source.close()
	out_file.close()
	out_diff.close()

if __name__ == "__main__":
	main()
import pickle
from datetime import datetime

def main():
	source = open("../references.pickle")
	out = open('../dense_references.pickle', 'w')
	print str(datetime.now())+ "xml2references.py - extracts articles that cite stuff from '"+source.name+"' and writing it to '"+out.name+"'"

	if not source:
		print "This works.... NOT"
		return -1
	
	refs = pickle.load(source)
	refs_tobeginwith = len(refs)

	autist_cnt = 0
	for article_id, adj_list in refs.items():
		if len(adj_list) < 1:
			autist_cnt += 1
			del refs[article_id]

	print 'reduced articles from %i to %i (%i percent, minus %i articles)' % (refs_tobeginwith, len(refs), (refs_tobeginwith/len(refs))*100, autist_cnt)
	print str(datetime.now())+' starting to persist references to: '+ out.name

	pickle.dump(refs, out)

	source.close()
	out.close()

if __name__ == "__main__":
	main()
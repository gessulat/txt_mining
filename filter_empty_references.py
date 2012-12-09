import pickle
from datetime import datetime

def main():
	source = open("../references.pickle")
	out = open('../dense_references.pickle', 'w')
	out_diff = open('../dense_references_diff.pickle', 'w')
	print str(datetime.now())+ "xml2references.py - extracts articles that cite stuff from '"+source.name+"' and writing it to '"+out.name+"' (save diff to '"+out_diff.name+"'"

	if not source:
		print "This works.... NOT"
		return -1
	
	diff = {}
	refs = pickle.load(source)

	# statistics: store informtion about the density in numbers and the distibution of our data
	refs_tobeginwith = len(refs)
	autist_cnt = 0
	dist = {}

	for article_id, adj_list in refs.items():
		if dist.has_key(len(adj_list)):
			dist[len(adj_list)] += 1
		else:
			dist[len(adj_list)] = 1

		if len(adj_list) < 1:
			autist_cnt += 1
			del refs[article_id]
			diff[article_id] = adj_list

	change_in_percent = (float(len(refs))/float(refs_tobeginwith)) * 100.
	print 'reduced articles from %i to %i (%f percent, minus %i articles)' % (refs_tobeginwith, len(refs), change_in_percent, autist_cnt)
	print 'Distribution: ', dist
	#print str(datetime.now())+' starting to persist references to: '+ out.name 

	pickle.dump(refs, out)
	pickle.dump(diff, out_diff)

	source.close()
	out.close()
	out_diff.close()

if __name__ == "__main__":
	main()
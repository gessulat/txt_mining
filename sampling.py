import cPickle, math, random, argparse, operator
from fish import ProgressFish


def check_lengths( abstracts, references):
	length = len(abstracts)
	if len(references) != length:
		print 'input file have differen length. Thats BAD!'
		return -1
	else:
		return length

def most_refs_sampling( abstracts, references, no_of_entries):
	no_of_entries = int(no_of_entries)
	length = check_lengths( abstracts, references)
	percentage = float(no_of_entries)/length*100
	print 'reduce '+str(length)+' to '+str(no_of_entries)
	print "that's about "+str(percentage)+"% of the original size "

	fish = ProgressFish(total = int(no_of_entries) )

	new_abs = {}
	new_refs = {}
	count_refs = {}

	for key, refs in references.items():
		count_refs[key] = len(refs)
	refs_sorted_by_count = sorted(count_refs.iteritems(), key=operator.itemgetter(1))

	for i in range( int(no_of_entries) ):
		fish.animate(amount=i)
		(choice, count) = refs_sorted_by_count.pop()
		new_abs[choice] = abstracts[choice]
		new_refs[choice] = references[choice]
	return new_abs, new_refs


def random_sampling( abstracts, references, no_of_entries):
	length = check_lengths( abstracts, references)
	percentage = float(no_of_entries)/length*100
	print 'reduce '+str(length)+' to '+str(no_of_entries)
	print "that's about "+str(percentage)+"% of the original size "


	fish = ProgressFish(total = int(no_of_entries) )

	key_list = abstracts.keys()
	random.shuffle(key_list)
	new_abs = {}
	new_refs = {}

	for i in range( int(no_of_entries) ):
		fish.animate(amount=i)
		choice = key_list.pop()
		new_abs[choice] = abstracts[choice]
		new_refs[choice] = references[choice]
	return new_abs, new_refs

def persist( sampled_abs, sampled_refs, abs_file_out, refs_file_out):
	print 'persist sampled abstracts'
	cPickle.dump( sampled_abs, abs_file_out, -1 )
	print 'persist sampled references'
	cPickle.dump( sampled_refs, refs_file_out, -1 )

def main():
	parser = argparse.ArgumentParser()
	parser.add_argument('in_abs', help='input abstracts file path: "../dense_abstracts.pickle" ')
	parser.add_argument('in_refs', help='input references file path: "../dense_references.pickle"')
	parser.add_argument('out_abs', help='file path of abstracts output file: "sampled_abstracts.pickle"')
	parser.add_argument('out_refs', help='file path of references output file: "sampled_abstracts.pickle"')
	parser.add_argument('sampling_method', help="random, most_refs,...")
	parser.add_argument('no_of_entries', help="the number of data entries after the sampling (choose this depending on how fast you can calculate!)")

	args = parser.parse_args()
	abs_file = open(args.in_abs)
	refs_file = open(args.in_refs)

	if not abs_file and refs_file:
		print "Some input file is missing..."
		return -1


	abs_file_out = open(args.out_abs, 'w')
	refs_file_out = open(args.out_refs, 'w')

	if not abs_file and refs_file:
		print "Some input file is missing..."
		return -1

		
	print 'loading abstracts...'
	abstracts = cPickle.load(abs_file)
	print 'loading references...'
	references = cPickle.load(refs_file)

	#print check_lengths( abstracts, references )
	print 'starting to sample'

	if args.sampling_method == "random":
		print 'random sampling!'
		sampled_abs, sampled_refs = random_sampling( abstracts, references, args.no_of_entries )
		persist( sampled_abs, sampled_refs, abs_file_out, refs_file_out)
	if args.sampling_method == "most_refs":
		print 'sampled entries with the most references!'
		sampled_abs, sampled_refs = most_refs_sampling( abstracts, references, args.no_of_entries )
		persist( sampled_abs, sampled_refs, abs_file_out, refs_file_out)





if __name__ == "__main__":
	main()
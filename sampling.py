import cPickle, math, random, argparse
from fish import ProgressFish


def check_lengths( abstracts, references):
	length = len(abstracts)
	if len(references) != length:
		print 'input file have differen length. Thats BAD!'
		return -1
	else:
		return length


def random_sampling( abstracts, references, percentage):
	length = check_lengths( abstracts, references)
	no_of_entries_to_delete = int(math.ceil(length * (1-percentage)))
	print 'reduce '+length+' to '+str(length-no_of_entries_to_delete)
	print "that's about "+str(percentage*100)+"%"


	fish = ProgressFish(total = no_of_entries_to_delete )
	for i in range(no_of_entries_to_delete):
		fish.animate(amount=i)
		choice = random.choice( abstracts.keys() )
		del abstracts[choice]
		del references[choice]
	return abstracts, references


def main():
	parser = argparse.ArgumentParser()
	parser.add_argument('in_abs', help='input abstracts file path: "../dense_abstracts.pickle" ')
	parser.add_argument('in_refs', help='input references file path: "../dense_references.pickle"')
	parser.add_argument('out_abs', help='file path of abstracts output file: "sampled_abstracts.pickle"')
	parser.add_argument('out_refs', help='file path of references output file: "sampled_abstracts.pickle"')
	parser.add_argument('sampling_method', help="random, ...")

	args = parser.parse_args()
	abs_file = open(args.in_abs)
	refs_file = open(args.in_refs)

	if not abs_file and refs_file:
		print "Some input file is missing..."
		return -1
		
	print 'loading abstracts...'
	abstracts = cPickle.load(abs_file)
	print 'loading references...'
	references = cPickle.load(refs_file)

	#print check_lengths( abstracts, references )
	print 'starting to sample'

	sampled_abs, sampled_refs = random_sampling( abstracts, references, .5)

	print 'persist sampled abstracts'
	cPickle.dump( sampled_abs, args.out_abs, -1 )
	print 'persist sampled references'
	cPickle.dump( sampled_refs, args.out_refs, -1 )



if __name__ == "__main__":
	main()
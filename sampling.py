import cPickle, math, random

def check_lengths( abstracts, references):
	length = len(abstracts)
	if len(references) != length:
		print 'input file have differen length. Thats BAD!'
		return -1
	else:
		return length


def random_sampling( abstracts, references, percentage):
	length = check_lengths( abstracts, references)
	no_of_entries_to_delete = math.ceil(length * (1-percentage))
	for i in range(no_of_entries_to_delete):
		choice = random.choice( abstracts.keys() )
		del abstracts[choice]
		del references[choice]


def main():
	source_abs = open("../dense_abstracts.pickle")
	source_ref = open("../dense_references.pickle")

	if not source_abs and source_ref:
		print "This works.... NOT"
		

	abstracts = cPickle.load(source_abs)
	references = cPickle.load(source_ref)
	print check_lengths( abstracts, references )
	#random_sampling( abstracts, references)



if __name__ == "__main__":
	main()
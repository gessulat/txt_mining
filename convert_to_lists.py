
import cPickle, argparse
from fish import ProgressFish

def convert_to_list( abstracts, references ):
	no_of_docs = len(abstracts)
	if len(references) != no_of_docs:
		print 'abstracts and refs must have same size!'
	abs_list = list()
	refs_list = list()
	keys_list = list()
	for key in references.keys():
		print key
		


def main():

	parser = argparse.ArgumentParser()
	parser.add_argument('in_vector_abs', help='input vector abstracts file path: "../vector_abstracts.pickle" ')
	parser.add_argument('in_refs', help='input vector abstracts file path: "../references.pickle" ')
	parser.add_argument('out_vector_abs', help='input vector abstracts file path: "../list_vector_abstracts.pickle" ')
	parser.add_argument('out_refs', help='input vector abstracts file path: "../list_references.pickle" ')
	parser.add_argument('out_keys', help='input word_base file path: "../list_keyspickle" ')

	args = parser.parse_args()
	
	print 'loading abstracts...'
	abs_file = open(args.in_vector_abs)
	abstracts = cPickle.load(abs_file)
	abs_file.close()

	print 'loading references...'
	abs_file = open(args.in_refs)
	references = cPickle.load(abs_file)
	abs_file.close()


	abs_list, refs_list, key_list = convert_to_list( abstracts, references)
	
	print 'persist vector abstracts list'
	output_file = open(args.out_abs,'w')
	cPickle.dump( out_vector_abs, abs_list, -1 )
	output_file.close()

	print 'persist references list'
	output_file = open(args.out_abs,'w')
	cPickle.dump( out_refs, refs_list, -1 )
	output_file.close()

	print 'persist key list'
	output_file = open(args.out_abs,'w')
	cPickle.dump( out_wb, key_list, -1 )
	output_file.close()
	

if __name__ == "__main__":
	main()
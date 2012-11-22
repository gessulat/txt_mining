import argparse

def write_ref_ids( inputFile, outputFile=False):
	ids = []
	print 'reading all identifiers...'
	for line in inputFile:
		token = line.split(" ")
		identifier = token[0]
		ids.append(identifier)
	print 'number of identifiers: '+str(len(ids))
	print 'removing duplicates...'
	ids = set(ids)
	print 'number of identifiers without duplicates: '+str(len(ids))
	counter = 0
	print 'writing dictionary to '+outputFile.name
	sorted_ids = list(ids)
	sorted_ids.sort()
	for identifier in sorted_ids:
		output_string = str(counter)+" "+identifier+"\n"
		outputFile.write( output_string )
		counter+=1

def write_words( inputFile, outputFile=False):
	words = []
	print 'reading all words...'
	for line in inputFile:
		token = line.split(" ")
		abstract_words = token[1:]
		for abstract_word in abstract_words:
			word = ''.join(e for e in abstract_word if e.isalnum() )# removes all special characters
			words.append(word)
	print 'number of words: '+str(len(words))
	print 'removing duplicates...'
	words = set(words)
	print 'number of identifiers without duplicates: '+str(len(words))
	sorted_words = list(words)
	sorted_words.sort()
	for word in sorted_words:
		output_string = word+" "
		outputFile.write( output_string )



def main():
	parser = argparse.ArgumentParser()
	parser.add_argument('part', choices=('ids', 'words'), 
								help="What part of the xml file do you want to parse? Choose abstracts (abs) or references (refs).")
	parser.add_argument('input', help='input file path (citeseer xml file)')
	parser.add_argument('out', default=False, help="file path of an output file. If not set, this writes to the console.")
	
	args = parser.parse_args()

	sourceFilePath = args.input
	source = open(sourceFilePath)
	
	if args.out:
		outFilePath = args.out
		out = open(outFilePath, 'w')
	else:
		out = False

	if args.part == 'ids':
		write_ref_ids( source, out)
	if args.part == 'words':
		write_words( source, out)
	
	source.close()
	out.close()

if __name__ == "__main__":
	main()
import cPickle, argparse

def main():
	parser = argparse.ArgumentParser()
	parser.add_argument('path', help='file path: to pickle"../foo.pickle" ')
	args = parser.parse_args()
	
	print 'loading pickle...'
	f = open(args.path)
	pickle = cPickle.load(f)
	f.close()
	print 'printing pickle!'
	print str( pickle )

	

if __name__ == "__main__":
	main()
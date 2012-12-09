import pickle
import argparse

def main():
	parser = argparse.ArgumentParser()
	parser.add_argument('input', help='input file path (pickle-dump)')
	parser.add_argument('diff', help='file path to diff (pickle-dump)')
	parser.add_argument('out', help="file path of an output file")

	args = parser.parse_args()

	sourceFilePath = args.input
	old_file = open(sourceFilePath)
	old = pickle.load(old_file)

	diffFilePath = args.diff
	diff_file = open(diffFilePath)
	diff = pickle.load(diff_file)
		
	print str(datetime.now())+ 'appending diff ', diff.name, ' to ', old.name

	for article_id, _ in diff.items():
		if old.has_key(article_id):
			del old[article_id]
		else:
			print 'Error'
			return -1

	outFilePath = args.out
	out_file = open(outFilePath, 'w')

	print str(datetime.now())+ 'starting to persist result ...'

	pickle.dump( old, out_file )

	old.close()
	diff.close()
	out.close()

if __name__ == "__main__":
	main()
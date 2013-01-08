import cPickle
import argparse
from datetime import datetime

def main():
	parser = argparse.ArgumentParser()
	parser.add_argument('input', help='input file path (pickle-dump)')
	parser.add_argument('diff', help='file path to diff (pickle-dump)')
	parser.add_argument('out', help="file path of an output file")

	args = parser.parse_args()

	sourceFilePath = args.input
	old_file = open(sourceFilePath)

	diffFilePath = args.diff
	diff_file = open(diffFilePath)
	
	print str(datetime.now())+ ' appending diff ', diff_file.name, ' to ', old_file.name
	
	diff = cPickle.load(diff_file)
	old = cPickle.load(old_file)
	warn = False	

	for article_id, _ in diff.items():
		if old.has_key(article_id):
			del old[article_id]
		else:
			warn = True

	if warn:
		print 'WARNING: The documents do not have exactly the same base'

	outFilePath = args.out
	out_file = open(outFilePath, 'w')

	print str(datetime.now())+ ' starting to persist result ...'

	cPickle.dump( old, out_file, -1 )

	old_file.close()
	diff_file.close()
	out_file.close()

if __name__ == "__main__":
	main()
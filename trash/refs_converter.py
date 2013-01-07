import argparse

def run( ):
	refsFile = open('../references.txt')
	idFile   = open('../ids.txt')
	outFile = open('../new_ref_bindings.txt', 'w')

	ids = {}
	print 'reading all new id bindings...'

	for line in idFile:
		new_id, ref = line.split(" ",1)
		stripped = ref.strip()
		if stripped in ids:
			print 'that should never have happened...'
		else:
			ids[stripped] = new_id.strip()

	print '...everything in main memory, sire!\n'

	print "writing references with new id bindings to: '../new_ref_bindings.txt'"
	for line in refsFile:
		id_ref, refs = line.split(" ",1)
		new_ref = ids[id_ref]
		new_refs = ""
		for ref in refs.split(" "):
			if ref in ids:
				new_refs = new_refs +" "+ids[ref]
		if new_refs != "":
			outFile.write( new_refs+'\n' )



def main():
	run()

if __name__ == "__main__":
	main()
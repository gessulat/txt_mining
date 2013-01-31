from os import system
datasets = ['mr', 'r']
lvalues = [50,75]
rvalues = [5, 10, 15, 20, 25, 30]

for d in datasets:
	for l in lvalues:
		for r in rvalues:
			r_val = str(float(r)/100)
			in_path  = "../data/{0}_10k_fishDist_{1}.p".format(d,l)
			out_path = "../data/cores/cores_{0}_10k_l{1}_r{2}.p".format(d,l,r)
			command = "python hcores.py {0} {1} {2}".format( r_val, in_path, out_path)
			print command
			system( command )



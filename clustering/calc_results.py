from os import system
lvalues = [25, 50, 75]
datasets = ['r', 'mr']
rvalues = [5, 10, 15, 20, 25, 30]
print 'dataset lambda r-value error cluster'
for lval in lvalues:
	for dset in datasets:
		for rval in rvalues:
			in_matrix  = "../data/{0}_10k_fishDist_{1}.p".format(dset,lval)
			in_cores = "../data/cores/cores_{0}_10k_l{1}_r{2}.p".format(dset,lval,rval)
			in_values = "'{0} {1} {2}'".format(dset, lval, rval)
			command = "python kmedoids.py {0} {1} {2}".format( in_matrix, in_cores, in_values)
			system( command )


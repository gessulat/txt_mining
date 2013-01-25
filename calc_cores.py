from os import system
lvalues = [75]
datasets = ['r']
rvalues = [35,40]
for lval in lvalues:
    for dset in datasets:
        for rval in rvalues:
            print lval, dset, rval
            s = 'python clustering/hcores.py '+str(float(rval)/100)+' data/'+dset+'_10k_fishDist_'+str(lval)+'.p data/cores/cores_'+dset+'_10k_l'+str(lval)+'_r'+str(rval)+'.p'
            system( s )


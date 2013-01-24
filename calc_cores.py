from os import system
lvalues = [25,50,75]
datasets = ['r','mr']
rvalues = [10,15,25,30,35,40,45,50]
for lval in lvalues:
    for dset in datasets:
        for rval in rvalues:
            print lval, dset, rval
            s = 'python clustering/hcores.py '+str(float(rval)/100)+' data/'+dset+'_10k_fishDist_'+str(lval)+'.p data/cores/cores_'+dset+'_10k_l'+str(lval)+'+_r'+str(rval)+'.p'
            system( s )


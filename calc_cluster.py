from os import system
lvalues = [25,50,75]
datasets = ['r','mr']
rvalues = [10,15,25,30,35,40,45,50]
for lval in lvalues:
    for dset in datasets:
        for rval in rvalues:
            values = 'dataset: '+str(dset)+' lambda: '+str(lval)+' r-value: '+str(rval)
            s = 'python clustering/kmedoids.py '+str(float(rval)/100)+' data/'+dset+'_10k_fishDist_'+str(lval)+'.p data/cores/cores_'+dset+'_10k_l'+str(lval)+'_r'+str(rval)+'.p "'+values+'"'
            system( s )


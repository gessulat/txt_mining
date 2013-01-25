from os import system
lvalues = [25, 50, 75]
datasets = ['r', 'mr']
rvalues = [10, 15, 20, 25, 30, 35]
print 'dataset lambda r-value error cluster'
for lval in lvalues:
    for dset in datasets:
        for rval in rvalues:
            values = str(dset)+' '+str(lval)+' '+str(rval)
            s = 'python kmedoids.py ../data/'+dset+'_10k_fishDist_'+str(lval)+'.p ../data/cores/cores_'+dset+'_10k_l'+str(lval)+'_r'+str(rval)+'.p "'+values+'"'
            system( s )


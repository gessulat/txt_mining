def bufcount(filename):
    f = open(filename)                  
    lines = 0
    buf_size = 1024 * 1024
    read_f = f.read # loop optimization
    buf = read_f(buf_size)
    while buf:
        lines += buf.count('\n')
        buf = read_f(buf_size)
    return lines


import glob
import os
os.chdir("data/cores")
for filename in glob.glob("*.p"):
        print filename, bufcount(filename)
                                                

#!/usr/bin/python

import sys
import random

def split_file(src_file, file1, file2):
    in_src = open(src_file, "r")
    ou_f1 = open(file1, "w")
    ou_f2 = open(file2, "w")
    
    first = True
    for line in in_src:
        if first == True: 
            ou_f1.write(line)
            ou_f2.write(line)
            first = False; 
            continue
        
        r = random.uniform(0,1)
        if r <= 0.7: ou_f1.write(line)
        else: ou_f2.write(line)
    ou_f2.close()
    ou_f1.close()
    in_src.close()

src_file = sys.argv[1]
file1 = sys.argv[2]
file2 = sys.argv[3]

split_file(src_file, file1, file2)

	
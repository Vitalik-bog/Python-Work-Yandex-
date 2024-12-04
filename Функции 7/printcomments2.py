# -*- coding: utf-8 -*-
import sys
c = 0
for line in sys.stdin:
    c += 1
    if line.strip()[0] == '#': 
        line = line.lstrip()[1:].strip()+'\n'
        print('Line '+ str(c) +': '+line, end='')
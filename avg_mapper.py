#!/usr/bin/env python

import csv
import sys

infile =sys.stdin
next(infile)

for line in infile:
    # remove leading and trailing whitespace
	line = line.strip()
    # split the line into words
	row = line.split(',')
	date = row[0][:-14]
    # increase counters
	if row[4] == '':
		print'%s\t%s\t%s\t' %(date,-1,1)
	else:
		mag = float(row[4])
		print '%s\t%s\t%s\t' %(date,mag,1)
			


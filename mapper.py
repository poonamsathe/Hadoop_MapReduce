#!/usr/bin/env python

import csv
import sys

#with open('all_month.csv', 'rb') as csvfile:
#	spamreader = csv.reader(csvfile)
#	spamreader.next()
#	for row in spamreader:

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
	print'%s\t%s\t%s\t%s' %(date,-1, 0 ,1)
    else:
	mag = float(row[4])
	if mag < 0:
		print'%s\t%s\t%s\t%s\t' %(date,mag, 0, 1)
	elif 0 <= mag < 1:
		print '%s\t%s\t%s\t%s\t' %(date,mag, 1, 1)
	elif 1 <= mag < 2:
		print '%s\t%s\t%s\t%s\t' %(date,mag, 2, 1)
	elif 2 <= mag < 3:
		print '%s\t%s\t%s\t%s\t' %(date,mag, 3, 1)
	elif 3 <= mag < 4:
		print '%s\t%s\t%s\t%s\t' %(date,mag, 4, 1)
	elif 4 <= mag < 5:
		print '%s\t%s\t%s\t%s\t' %(date,mag, 5, 1)
	elif 5 <= mag < 6:
		print '%s\t%s\t%s\t%s\t' %(date,mag, 6, 1)
	elif 6 <= mag < 7:
		print '%s\t%s\t%s\t%s\t' %(date,mag, 7, 1)


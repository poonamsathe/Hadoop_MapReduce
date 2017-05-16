#!/usr/bin/env python

import csv
import sys
import datetime

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
	#date = row[0][:-14]
	#date_format = datetime.datetime.strptime(date,"%Y-%m-%d").date()
	#week_no = date_format.isocalendar()[1]

    # increase counters
	if row[0] == '' and row[1]  == '':
		print'%s\t%s\t' %(-1,-1,0,1)
	else:
		
		if row[0]==1 and row[1]==1:
			print '%s\t%s\t%s\t%s\t' %(row[0],row[1],1,1)


		if row[0]==2 and row[1]==1:
			print '%s\t%s\t%s\t%s\t' %(row[0],row[1],2,1)


		if row[0]==3 and row[1]==1:
			print '%s\t%s\t%s\t%s\t' %(row[0],row[1],3,1)



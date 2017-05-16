#!/usr/bin/env python
import sys
from operator import itemgetter

magnitude_count = 0
current_count = 0
current_date = None

for line in sys.stdin:
	# remove leading and trailing whitespace
	line1 = line.strip()
	
	# parse the input we got from mapper.py
	date,mag,count = line.split('\t',2)
	
	# convert count (currently a string) to int
	try:
		count = float(count)
		mag = float(mag)
	except ValueError:
        # count was not a number, so silently
        # ignore/discard this line
        	continue

    # this IF-switch only works because Hadoop sorts map output
    # by key (here: word) before it is passed to the reducer
	if current_date == date:
		current_count += count
		magnitude_count+= mag
	else:
		if current_date:
            # write result to STDOUT
			avg = magnitude_count / current_count
			print '%s\t%s' % (current_date,avg)
		current_count = count
		current_date = date
		magnitude_count = mag

# do not forget to output the last word if needed!
if current_date == date:
	print '%s\t%s' % (current_date,avg)
	




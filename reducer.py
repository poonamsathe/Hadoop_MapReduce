#!/usr/bin/env python
import sys
from operator import itemgetter

current_group = None
current_count = 0
group = None
current_date = None

for line in sys.stdin:
	# remove leading and trailing whitespace
	line1 = line.strip()
	
	# parse the input we got from mapper.py
	date,mag,group,count = line.split('\t',3)
	
	# convert count (currently a string) to int
	try:
		count = int(count)
	except ValueError:
        # count was not a number, so silently
        # ignore/discard this line
        	continue

    # this IF-switch only works because Hadoop sorts map output
    # by key (here: word) before it is passed to the reducer
	if current_group == group and current_date == date:
		current_count += count
	else:
		if current_group and current_date:
            # write result to STDOUT
			print '%s\t%s\t%s' % (current_date,current_group, current_count)
		current_count = count
		current_group = group
		current_date = date

# do not forget to output the last word if needed!
if current_group == group and current_date == date:
	print '%s\t%s\t%s' % (current_date,current_group, current_count)
	

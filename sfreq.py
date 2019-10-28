''' Created by Jeremy Reynolds for UALR Social Computing CPSC 4360
	Searches each comment for the 'query' and totals it's
	frequency for each date.

	Expects .csv with date in first column and comments in forth column.
	Outputs the frequency of 'query' for each date.
'''

import csv, re

count = 0		# Initial frequency count
date1 = '0'		# Initialize first date to be 0 (for logic)
date2 = '0'		# Initialize second date to be 0 (for logic)
query = 'good'	# The word to search each comment for
log = 'test_2019-1-1.csv'
print('Searching: ', query, ' from', log[:-13])

# If the current date is greater/equal than the next date, find 'query' and iterate count
# If the current date is less than the next date, reset and counter and continue
reader = csv.reader(open(log))
for item in reader:
	date1 = item[0][0:10]
	if date1 >= date2:
		comment = [item[3].split()]
		for words in comment:
			for word in words:
				word = re.sub(r'[^a-z0-9]','',word.lower())
				if word == query:
					count += 1
	else:
		print(date2, count)
		count = 0
	date2 = item[0][0:10]
print('Finished: ', query, ' from', log[:-13])

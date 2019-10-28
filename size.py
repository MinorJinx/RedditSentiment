''' Created by Jeremy Reynolds for UALR Social Computing CPSC 4360
	Searches for all .csv in a directory and totals 
	their size in MB and counts the number of lines (comments).

	Expects directory with .csv files.
	Outputs the total size of all files.
'''

import glob, os

print('Printing file sizes and number of lines:\n')
for log in glob.glob('*.csv'):
	size = os.path.getsize(log)/(1024*1024.0) # Converts from bytes to megabytes
	with open(log) as f:
		lines = sum(1 for line in f)
	print(log[:-13].ljust(20), str(round(size,2)).ljust(6), 'MB\t', lines)

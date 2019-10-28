''' Created by Jeremy Reynolds for UALR Social Computing CPSC 4360
	Searches given subreddit for comments
	Performs TextBlob sentiment analysis on comments
	Saves date, time, TextBlob polarity, and comments to .csv
'''

import csv, datetime as dt
from psaw import PushshiftAPI
from textblob import TextBlob

y = 2019				# Year value for daterange/filename
m = 1					# Month value for daterange/filename
d = 1					# Day value for daterange/filename
lim = 1000000000000		# Upper limit for max comments
sub = 'test'			# Subreddit to search
log = sub+'_'+str(y)+'-'+str(m)+'-'+str(d)+'.csv'

# Search subreddit using PSAW
api = PushshiftAPI()
start_epoch=int(dt.datetime(y, m, d).timestamp())
search = api.search_comments(after=start_epoch, subreddit=sub, limit=lim)
print('Searching: ', sub)

# Create .csv with column headers
with open(log, 'a', newline='') as file:
	writer = csv.writer(file)
	writer.writerow(['date', 'polarity', 'subjectivity', 'comment'])

# Writes each comment and analysis to new line in .csv
counter = 0
with open(log, 'a', newline='') as file:
	writer = csv.writer(file)
	for item in search:
		# Encodes using ascii to remove emojis, decodes and removes newlines
		i = item.body.encode('ascii', 'ignore').decode().replace('\n', '')
		date_created = dt.datetime.fromtimestamp(item.created_utc).strftime('%Y-%m-%d %H:%M:%S') #yyyy-m-d hh:mm:ss
		
		# Prevents blank space being analyzed
		if i.strip():
			counter += 1
			testimonial = TextBlob(i)
			writer.writerow([date_created, testimonial.sentiment.polarity, testimonial.sentiment.subjectivity, i])
		else:
			print(counter, date_created, "'"+i+"'")

print('\nFound: ', counter, ' from', sub)

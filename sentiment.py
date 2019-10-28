''' Created by Jeremy Reynolds for UALR Social Computing CPSC 4360
	Reads the comments produced from scrape.py and
	performs VADER sentiment analysis.

	Expects .csv with comments in fourth column.
	Outputs mean value of TextBlob and VADER values.
'''

import csv, glob, numpy
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

tb = []	# TextBlob Mean Sentiment
vd = []	# Vader Mean Sentiment
#log = 'test_2019-1-1.csv'

for log in glob.glob('*.csv'):
	print('searching', log[:-13])

	reader = csv.reader(open(log))
	analyzer = SentimentIntensityAnalyzer()
	for item in reader:
		vs = analyzer.polarity_scores(item[3])
		vd.append(vs['compound'])
		if item[1] != '0.0' and len(item[3]) > 10:
			tb.append(item[1])
	tb = [float(i) for i in tb[1:]]
	print('TB: ', numpy.mean(tb), log[:-13])
	print('VD: ', numpy.mean(vd), log[:-13])

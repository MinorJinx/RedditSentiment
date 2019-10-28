# scrape.py

Searches given subreddit for comments and performs TextBlob sentiment analysis on comments

Saves date, time, TextBlob polarity, and comments to .csv


# sentiment.py
Reads the comments produced from scrape.py and performs VADER sentiment analysis.

```
Expects .csv with comments in fourth column.
Outputs mean value of TextBlob and VADER values.
```


# sfreq.py
Searches each comment for the 'query' and totals it's frequency for each date.

```
Expects .csv with date in first column and comments in forth column.
Outputs the frequency of 'query' for each date.
```


# sfreq.py
Searches for all .csv in a directory and totals their size in MB and counts the number of lines (comments).

```
Expects directory with .csv files.
Outputs the total size of all files.
```

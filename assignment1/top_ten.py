import sys
import json
import re

def lines(fp):
	print str(len(fp.readlines()))
def contains_word(s, w):
	return w in re.findall(r"[\w']+",s)
def main():
	tweet_file = open(sys.argv[1])
	data=[]
	freq={}

	for l in tweet_file:
		data.append(json.loads(l))
	
	try:
		for tweet in data:
			for hashtag in tweet[u'entities'][u'hashtags']:
				if hashtag[u'text'] in freq: #encode('utf-8'):
					freq[hashtag[u'text']]=1+freq[hashtag[u'text']]
				else:
					freq[hashtag[u'text']]=1
	except KeyError:
		freq["NO_HASHTAG"]=0
	
	del freq["NO_HASHTAG"]
	for x in freq.keys():
		print x + " "+ str(freq[x])			
	tweet_file.close()
if __name__ == '__main__':
	main()


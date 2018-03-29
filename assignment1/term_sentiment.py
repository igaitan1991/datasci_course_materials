import sys
import json

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))
def contains_word(s, w):
    return (' ' + w + ' ') in (' ' + s + ' ')
def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    scores = {} # initialize an empty dictionary
    data = []
    for line in sent_file:
      term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
      scores[term] = int(score)  # Convert the score to an integer.
    for l in tweet_file:
      data.append(json.loads(l))
    aux = 0
    for tweet in data:
      try:
        for key in scores:
            if contains_word(tweet[u'text'].encode('utf-8'),key):
              aux = aux+scores[key]
        print aux #"This is the result:",aux
        aux=0
      except KeyError:
        print 0 #("This line is not a Tweet")
    sent_file.close()
    tweet_file.close()
if __name__ == '__main__':
    main()

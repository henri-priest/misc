from secrets import consumer_key, consumer_secret, access_token_key, access_token_secret
from tags import tags
import re, csv, json, twitter, concurrent.futures

def dummy_function(num, pow):
    """ Only used for example unity tests. Returns num rased to pow. """
    return num ** pow

def get_tweets(count, tag):
    """ Searches the Twitter API for contents of tag, count is the number of tweets to fetch. """
    api = twitter.Api(consumer_key=consumer_key,
                  consumer_secret=consumer_secret,
                  access_token_key=access_token_key,
                  access_token_secret=access_token_secret)

    tweet = api.GetSearch(term=tag, count=count)

    return tweet

if __name__ == "__main__":

    tweet_list = []

    with concurrent.futures.ThreadPoolExecutor(4) as executor:
        """ Uses the python thread wrapper module to create a thread per tag in tags.py,
        each thread calls the Twitter search API as a separate query and 50 tweets. """

        future_tweet = { executor.submit(get_tweets, 100, i): i for i in tags}

        for future in concurrent.futures.as_completed(future_tweet):
            tweet_list.append(future.result())

    with open('output.csv', 'w', newline='') as f:
        """ Format output and write to file.  """
        for row in tweet_list:
            lines = str(row).split("Status")
            lines.pop(0)
            for line in lines:
                f.write("%s\n" % str(line).encode('utf8'))

# Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream, API, Cursor
import jsonpickle

# Variables that contains the user credentials to access Twitter API
access_token = ""
access_token_secret = ""
consumer_key = ""
consumer_secret = ""


# This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print(data)
        return True

    def on_error(self, status):
        print(status)


if __name__ == '__main__':
    # This handles Twitter authetification and the connection to
    # Twitter Streaming API l = StdOutListener()

    auth = OAuthHandler(consumer_key, consumer_secret)
    # auth.set_access_token(access_token, access_token_secret)

    # stream = Stream(auth, l)

    # This line filter Twitter Streams to capture data by the keywords:
    # 'python','javascript', 'ruby'
    # stream.filter(track=['wargaming'])

    api = API(auth)

    with open('./results.txt', 'w') as results_file, \
            open('./tags.txt', 'w') as tags_file:

        for tweet in Cursor(api.search, q='WorldOfTanks OR WorldOfWarships OR WorldOfWarplanes').items(10000):
            tweet_encoded = jsonpickle.encode(tweet._json, unpicklable=False)

            # results_file.write(tweet_encoded)

            tags = tweet._json['entities']['hashtags']
            if not len(tags) is 0:
                tags_in_line = "\n".join([tag['text'] for tag in tags])
                tags_file.write("%s\n" % tags_in_line)

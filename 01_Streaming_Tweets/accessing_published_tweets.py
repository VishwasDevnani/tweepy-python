from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

import twitter_credentials

# ********** TWITTER STREAMER *********** #
class TwitterStreamer():
    """
    Class for Streaming and Processing live tweets
    """

    def __init__(self):
        pass

    def stream_tweets(self, filename,hash_tag_list):
        listener = Listerner_output(filename)
        auth  = OAuthHandler(twitter_credentials.CONSUMER_KEY, twitter_credentials.CONSUMER_SECRET)
        auth.set_access_token(twitter_credentials.ACCESS_TOKEN, twitter_credentials.ACCESS_SECRET)

        stream = Stream(auth, listener)

        # This line filter Twitter Streams to capture data by the keywords: 
        stream.filter(track=hash_tag_list)

# ******* TWITTER STREAM LISTENER ******** #
class Listerner_output(StreamListener):
    """
    It is a simple listener  that prints recieved tweets to stdout.
    """

    def __init__(self,filename):
        self.filename = filename

    def on_data(self, raw_data):
        try:
            print(raw_data)
            with open(self.filename , 'a') as fn:
                fn.write(raw_data)
            return True
        except BaseException as e:
            print("Error on data %s"%str(e))
        return True
    
    def on_error(self, status_code):
        print(status_code)

if __name__ == '__main__':
 
    # Authenticate using config.py and connect to Twitter Streaming API.
    hash_tag_list = ["donal trump", "hillary clinton", "barack obama", "bernie sanders"]
    fetched_tweets_filename = "tweets.json"

    twitter_streamer = TwitterStreamer()
    twitter_streamer.stream_tweets(fetched_tweets_filename, hash_tag_list)

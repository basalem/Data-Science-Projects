from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json
import boto3
import time


class TweetStreamListener(StreamListener):
    # on success
    def on_data(self, data):
        tweet = json.loads(data)
        try:
            if 'text' in tweet.keys():
                message_lst = [str(tweet['id']),
                       str(tweet['user']['name']),
                       str(tweet['user']['screen_name']),
                       tweet['text'].replace('\n',' ').replace('\r',' '),
                       str(tweet['user']['followers_count']),
                       str(tweet['user']['location']),
                       str(tweet['geo']),
                       str(tweet['place']),
                       str(tweet['created_at']),
                       '\n'
                       ]
                message = '\t'.join(message_lst)
                print(message) # comment this because it takes a lot of space on ec2 logs
                firehose_client.put_record(
                    DeliveryStreamName=delivery_stream_name,
                    Record={
                        'Data': message
                    }
                )
        except (AttributeError, Exception) as e:
            print(e)
        return True

    def on_error(self, status):
        print (status)


if __name__ == '__main__':
    # create kinesis client connection
    session = boto3.Session(profile_name='twitter_project')
    firehose_client = session.client('firehose', region_name='us-east-1')

    # Set kinesis data stream name
    delivery_stream_name = 'twitter_project_delivery_stream'

    # Set twitter credentials
    consumer_key = 'xxxxxxxxxxxxxxxxxx'
    consumer_secret = 'xxxxxxxxxxxxxxxxxxx'
    access_token = 'xxxxxxxxxxxxxxxx'
    access_token_secret = 'xxxxxxxxxxxxxxxxxxx'
    # set twitter keys/tokens
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    while True:
        try:
            print('Twitter streaming...')

            # create instance of the tweet stream listener
            listener = TweetStreamListener()

            # create instance of the tweepy stream
            stream = Stream(auth, listener)

            # search twitter for the keyword
            stream.filter(track=['trump','Trump','donald trump','Donald Trump','realdonaldtrump','realDonaldTrump','Donald J. Trump','republican party','JoeBiden','joebiden','Joe Biden','joe biden','biden','democrat party','2020 US Election'], languages=['en'], s$
        except Exception as e:
            print(e)
            print('Disconnected...')
            time.sleep(5)
            continue



import tweepy
import pandas as pd

from codes import consumer_key, consumer_secret, access_token, access_token_secret, bearer_token

INPUT_FILE_POS="../full_dataset_clean.tsv"

# print(consumer_key)
# print(consumer_secret)
# print(access_token)
# print(access_token_secret)

ID = "id"
DATE = "date"
TIME = "time"
LANG = "lang"
REGION = "region"
fields = [ID, DATE, TIME, LANG, REGION]

# this df has 344339998 lines
# we can only download 50K per month
# df = pd.read_csv(INPUT_FILE_POS, sep="\t", names=fields, header=0)

chunk_len = 1000

def main():
    client = tweepy.Client(bearer_token, consumer_key, consumer_secret, access_token, access_token_secret, wait_on_rate_limit=True)
    # auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    # auth.set_access_token(access_token, access_token_secret)
    # api = tweepy.API(auth)
    with pd.read_csv(INPUT_FILE_POS, sep="\t", names=fields, header=0, chunksize=chunk_len) as reader:
        for chunk in reader:
            for i in range(10):
                tid = chunk[ID][0]
                
                tweet = client.get_tweet(tid)
                print("--------", tid)
                print(tweet)
            
            break
        


# auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
# auth.set_access_token(access_token, access_token_secret)
# api = tweepy.API(auth)

# tweet = api.get_status("1219343794845425672")
# print(tweet._json)

if __name__ == "__main__":
    main()

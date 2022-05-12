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
FIELDS = [ID, DATE, TIME, LANG, REGION]

# this df has 344339998 lines
# we can only download 50K per month
# df = pd.read_csv(INPUT_FILE_POS, sep="\t", names=fields, header=0)

CHUNK_LEN = 1000

def main():
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    chunk_id = 0
    with pd.read_csv(INPUT_FILE_POS, sep="\t", names=FIELDS, header=0, chunksize=CHUNK_LEN) as reader:
        for chunk in reader:
            start_idx = chunk_id * CHUNK_LEN
            for i in range(CHUNK_LEN):
                id_in_dataset = start_idx + i
                tlang = str(chunk[LANG][id_in_dataset])  # tweet language
                if tlang != "en":
                    continue
                tid = str(chunk[ID][id_in_dataset])
                tdate = str(chunk[DATE][id_in_dataset])
                ttime = str(chunk[TIME][id_in_dataset]) 
                tregion = str(chunk[REGION][id_in_dataset])

                print("\n\n===========\nGetting tid:", tid)
                print("Getting date:", tdate)
                print("Getting time:", ttime)
                print("Getting lang:", tlang)
                print("Getting region:", tregion)
                try:
                    tweet = api.get_status(tid, tweet_mode='extended')
                    print(tweet.full_text)
                    break
                except Exception as e:
                    print(tid, e)
            
            chunk_id += 1
            break
        

if __name__ == "__main__":
    main()

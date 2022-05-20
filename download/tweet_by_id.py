import tweepy
import pandas as pd
import sys

from tokens import consumer_key, consumer_secret, access_token, access_token_secret, bearer_token
import utils

INPUT_FILE_POS = "../full_dataset_clean.tsv"
CHUNK_LEN = 10  # read 1000 lines per chunk, dataset has 344339998 lines
NUM_CHUNK_PER_SAVE = 2

def get_start_chunk(part=0):
    # There are 344339998 lines in the dataset
    # Second half starts at line 344339998 / 2 =~ 172170000
    # line 172170000 has chunk_id: 172170000 // CHUNK_LEN
    # start chunk is:
    #           0 -- if processing first half (part 0)
    #           1 -- if processing second half (part 1)
    return part * 172170000 // CHUNK_LEN


def process_chunk(chunk_status, api):
    chunk = chunk_status.chunk
    start_idx = chunk_status.chunk_id * CHUNK_LEN  # start of this chunk

    # iterate over all lines inside this chunk
    for i in range(CHUNK_LEN):
        line_num = start_idx + i
        
        if utils.should_ignore(chunk, line_num):
            continue

        tid = utils.get_tweet_id(chunk, line_num)


        author_id, full_text = utils.download_tweet(tid, api)  # might be None, None
        if utils.not_vaccine_related(full_text):
            continue
        chunk_status.save_one_tweet_in_mem(author_id, full_text, line_num)
    
    chunk_status.chunk = None



def main(part=0):
    start_chunk_id = get_start_chunk(part)

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)

    with pd.read_csv(INPUT_FILE_POS, sep="\t", names=utils.FIELDS, header=0, chunksize=CHUNK_LEN) as reader:
        chunk_id = 0
        chunk_status_collect = []
        for chunk in reader:
            if chunk_id < start_chunk_id:
                chunk_id += 1
                continue
            
            chunk_status = utils.ChunkStatus(chunk_id, chunk)
            process_chunk(chunk_status, api)
            chunk_status_collect.append(chunk_status)
            
            if len(chunk_status_collect) >= NUM_CHUNK_PER_SAVE:
                utils.save_chunk_mems_to_file(chunk_status_collect)
                chunk_status_collect = []
            
            chunk_id += 1


def print_usage():
    print("Usage: python {} [part_idx:int]\n\n"
          "part_idx:\t0 - download first half;\n"
          "\t\t1 - download second half".format(sys.argv[0])
          )


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print_usage()
        exit(-1)
    if sys.argv[1] == "0":
        main(0)
    elif sys.argv[1] == "1":
        main(1)
    else:
        print_usage()
        exit(-1)
    # main()

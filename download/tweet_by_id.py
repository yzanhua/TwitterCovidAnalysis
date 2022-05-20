import tweepy
import pandas as pd
import sys
from tqdm import tqdm

from tokens import consumer_key, consumer_secret, access_token, access_token_secret, bearer_token
import utils

INPUT_FILE_POS = "../input/seg"
CHUNK_LEN = 10000  # read 1000 lines per chunk, dataset has 344339998 lines
NUM_CHUNK_PER_SAVE = 5


def process_chunk(chunk_status, api):
    chunk = chunk_status.chunk
    start_idx = chunk_status.chunk_id * CHUNK_LEN  # start of this chunk

    # iterate over all lines inside this chunk
    for i in tqdm(range(CHUNK_LEN)):
        line_num = start_idx + i

        if utils.should_ignore(chunk, line_num):
            continue

        tid = utils.get_tweet_id(chunk, line_num)

        author_id, full_text = utils.download_tweet(
            tid, api)  # might be None, None
        if utils.not_vaccine_related(full_text):
            continue
        chunk_status.save_one_tweet_in_mem(author_id, full_text, line_num)

    chunk_status.chunk = None


def main(st_file_id, ed_file_id):
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)

    for i in range(st_file_id, ed_file_id):
        process_file(i, api)


def process_file(file_id, api):
    file_name = INPUT_FILE_POS + "{:02d}".format(file_id)
    print(file_name)
    header_val = 0 if file_id == 0 else None

    with pd.read_csv(file_name, sep="\t", names=utils.FIELDS, header=header_val, chunksize=CHUNK_LEN) as reader:
        chunk_id = 0
        chunk_status_collect = []
        for chunk in reader:
            chunk_status = utils.ChunkStatus(chunk_id, chunk, file_id)
            process_chunk(chunk_status, api)
            chunk_status_collect.append(chunk_status)

            if len(chunk_status_collect) >= NUM_CHUNK_PER_SAVE:
                utils.save_chunk_mems_to_file(chunk_status_collect)
                chunk_status_collect = []

            print("finished processing chunk id {}".format(chunk_id))

            chunk_id += 1
        if len(chunk_status_collect) > 0:
            utils.save_chunk_mems_to_file(chunk_status_collect)
            chunk_status_collect = []


def print_usage():
    print("Usage: python {} [st_id:int] [ed_id:int;default=st_id+1]\n"
          "0 <= st_id <= 47; inclusive\n"
          "1 <= ed_id <= 48; exclusive\n"
          "st_id < ed_id\n".format(sys.argv[0])
          )


if __name__ == "__main__":
    if len(sys.argv) == 3:
        try:
            st_id = int(sys.argv[1])
            ed_id = int(sys.argv[2])
        except Exception as e:
            print(e)
            print_usage()
            exit(-1)
        if st_id < 0 or st_id > 47:
            print_usage()
            exit(-1)
        if ed_id < 1 or ed_id > 48:
            print_usage()
            exit(-1)
        if st_id >= ed_id:
            print_usage()
            exit(-1)
        main(st_id, ed_id)
    elif len(sys.argv) == 2:
        try:
            st_id = int(sys.argv[1])
        except Exception as e:
            print(e)
            print_usage()
            exit(-1)
        if st_id < 0 or st_id > 47:
            print_usage()
            exit(-1)

        ed_id = st_id + 1
        main(st_id, ed_id)
    else:
        print_usage()
        exit(-1)

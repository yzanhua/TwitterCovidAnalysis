"""
Output CSV has the following 8 fileds (columns):
    author,date,file_id,full_text,line_num,region,time,tweet_id
"""

import os
import json
import csv


IN_FOLDER = "data"
OUT_FILE_NAME = "../vac_related.csv"

header_written = False

def combine(in_path, csv_writer):
    global header_written
    with open(in_path, 'r') as json_file:
        json_list = json.load(json_file)
        if len(json_list) == 0:
            return 0
        if not header_written:
            header = json_list[0].keys()
            csv_writer.writerow(header)
            header_written = True
        for tweet in json_list:
            csv_writer.writerow(tweet.values())
        return len(json_list)


def main():
    to_process = []
    for sub_folder, _, files in os.walk(IN_FOLDER):
        for name in files:
            if name.endswith(".save"):
                in_path = os.path.join(sub_folder, name)
                to_process.append(in_path)
    num_tweets = 0
    with open(OUT_FILE_NAME, 'w', newline='') as out_file:
        csv_writer = csv.writer(out_file)
        for in_path in to_process:
            print(in_path)
            num_tweets += combine(in_path, csv_writer)
    print(num_tweets)


# def try_read():
#     import pandas as pd
#     import utils
#     df = pd.read_csv(OUT_FILE_NAME, header=0)

#     for row_id in range(min(df.shape[0], 12)):
#         print("\n\n\n")
#         print(df[utils.FULL_TEXT][row_id])


if __name__ == "__main__":
    main()
    # try_read()

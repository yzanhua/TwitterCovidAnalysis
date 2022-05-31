from transformers import pipeline
import pandas as pd
import re

IN_FILE = "../vac_related.csv"

LINE_NUM = "line_num"
FULL_TEXT = "full_text"
TID = "tweet_id"
AUTHOR = "author"
FILE_ID = "file_id"

REOBJ = re.compile(r'https?://\S+')

def remove_url(input:str):
    global REOBJ
    return re.sub(REOBJ, '', input)

def preprocess(input:str):
    input = remove_url(input)
    # maybe someother pre-processing functions
    return input

def main():
    df = pd.read_csv(IN_FILE, header=0)
    # print(IN_FILE, "has shape", df.shape)
    # # for row in range(df.shape[0]):
    # print(df.head(5))
    tweet = df[FULL_TEXT][0]
    print(tweet)

    tweet = preprocess(tweet)
    print(tweet)

    c = Classifier()
    print(c.score(tweet))
    
class Classifier:
    def __init__(self) -> None:
        self.classifier = pipeline("text-classification", "clampert/multilingual-sentiment-covid19")

    def score(self, input:str):
        return self.classifier(input)


if __name__ == "__main__":
    main()

    

import json
from vac_keywords import vac_kws

ID = "id"
DATE = "date"
TIME = "time"
LANG = "lang"
REGION = "region"
FIELDS = [ID, DATE, TIME, LANG, REGION]


def should_ignore(chunk, line_num):
    if get_tweet_language(chunk, line_num) != "en":
        # ignore this tweet(line) if it is not english
        return True
    return False


def get_tweet_language(chunk, line_num):
    return str(chunk[LANG][line_num])


def get_tweet_id(chunk, line_num):
    return str(chunk[ID][line_num])


def download_tweet(tweet_id, api):
    try:
        tweet = api.get_status(tweet_id, tweet_mode='extended', trim_user=True)
    except Exception as e:
        return None, None

    author_id = -1
    text = None
    try:
        author_id = tweet.author.id
    except Exception as e:
        author_id = -1

    try:
        text = tweet.full_text.lower()
    except Exception as e:
        text = None
    return author_id, text


def not_vaccine_related(full_text):
    # input: full_text, str
    # output: bool, True if **NOT** related to vaccine
    #               False if related to vaccine
    if full_text is None:
        return True

    if any(word in full_text for word in vac_kws):
        return False

    return True


class ChunkStatus:
    def __init__(self, chunk_id, chunk, file_id) -> None:
        self.chunk_id = chunk_id
        self.chunk = chunk
        self.file_id = file_id
        self.mem = []

    def save_one_tweet_in_mem(self, author_id, full_text, line_num):
        tweet = {"line_num": line_num,
                 "full_text": full_text,
                 "tweet_id": get_tweet_id(self.chunk, line_num),
                 "date": str(self.chunk[DATE][line_num]),
                 "time": str(self.chunk[TIME][line_num]),
                 "region": str(self.chunk[REGION][line_num]),
                 "author": author_id,
                 "file_id": self.file_id
                 }
        self.mem.append(tweet)


def save_chunk_mems_to_file(cs_collect):
    if len(cs_collect) == 0:
        return
    st_id = cs_collect[0].chunk_id
    ed_id = cs_collect[-1].chunk_id
    file_id = cs_collect[0].file_id
    file_name = "data/seg{:02d}/chunk{}_{}.save".format(file_id, st_id, ed_id)
    content = [tweet for chunk_status in cs_collect for tweet in chunk_status.mem]
    with open(file_name, "w") as file:
        json.dump(content, file, ensure_ascii=False, indent=4, sort_keys=True)

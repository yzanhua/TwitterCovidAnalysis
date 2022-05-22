# Tweets Download
This folder contains all codes and logics to download full tweets using tweet ids.

Use commnad `git pull` to update codes from github repo.

**Important**: Activate your python virtual env first.

```shell
$ pwd  # show working directory; outside download (this folder)
/home/[netid]/TwitterCovidAnalysis

$ git pull  # update codes

# Activate virtual env
$ source env/bin/activate  # if using bash/zsh/etc
$ source env/bin/activate.csh  # if using tcsh/etc

# upgerade pip (this command is run before; no need to run twice)
$ pip install --upgrade pip

# download packages: (newly added: tqdm)
pip install numpy matplotlib scipy pandas tweepy tqdm

# continue working on the project.
...

```

## Keys and Tokens
`tokens.py` read keys and tokens from [tweet-keys](../tweet-keys/) folder. Please put your keys and tokens in that folder.

## Split Input:
`full_dataset_clean.tsv` contains `344339998` lines. Which is too large to process. Therefore,
we will first split it to 48 files. We'll call them segment files or segments.

```shell
$ pwd  # show working directory; outside download (this folder)
/home/[netid]/TwitterCovidAnalysis

$ ls  # check what files and folders are
download  env  full_dataset_clean.tsv  README.md  tweet-keys

$ mkdir input  # create an "input" folder.
$ ls  # check again
download  env  full_dataset_clean.tsv  input  README.md  tweet-keys

$ cd input  # go to input folder

# split the tsv; each file has 7173750; 48 files will be created.
$ split -l 7173750 -d ../full_dataset_clean.tsv seg

$ ls 
seg00 ~ seg47
```

## Create Output Folders
Create all necessary folders for output files.

```shell
$ pwd  # show working directory; outside download (this folder)
/home/[netid]/TwitterCovidAnalysis
$ cd download

$ ls  
create_dir.py  data  __pycache__  README.md  tokens.py  tweet_by_id.py  utils.py  vac_keywords.py
# it's possible that you don't have `data` folder, which we will create later.
# it's possible that you don't have `__pycache__` folder.

$ python create_dir.py  # create the `data` folder and its subfolders.

$ ls data  # seg00 ~ seg47 are 48 (empty) folders, one for each segment.
README.md  seg00 ~ seg47
```


## Download by ID
`tweet_by_id.py` downloads tweets using IDs.

Only tweets related to vaccines are saved
to [data](./data) folder.

**Important**: Activate virtual env first.

### General Usage
```shell
# activate virtual env

$ pwd  # current working directory
/home/[netid]/TwitterCovidAnalysis/download

# download tweets from input segment file `../input/segXX`.
# seg_id should be an integer from 0 to 47.  (seg_id <==> XX)
$ python tweet_by_id.py [seg_id:int] [chunk_id:int]
# An example is: python tweet_by_id.py 47 105

# A progess bar will show.
# In my pc, the progress bar will take around 40 min to complete.
# After completing one bar, 700+ more bars are expected.
# Will take days to complete. 
```

### Concurrent Download
You can invoke `tweet_by_id.py` from differnt terminal, so that these
terminals can download and process concurrently.

For example, the following codes download and process 
`../input/seg47`, `../input/seg46`, and `../input/seg27`
concurrently (if in 3 different terminals).
```shell
# terminal 1
$ python tweet_by_id.py 47

# another terminal 2
$ python tweet_by_id.py 46

# another terminal 3
$ python tweet_by_id.py 27
```

Now, I (Zanhua) am downloading segment files `seg00` ~ `seg11`,
i.e. the first `12` segments. you can start downloading the
last several segments. I'll suggest download `8` segments concurrently,
instead of `12` as what I am doing.

```shell
# in terminal x (x in [0, 1, 2, ..., 7])
# replace [47-x] with actual val.
python tweet_by_id.py [47-x]
```

### Tmux
Refer to [this github repo](https://github.com/reda-bahrani/CE510-Social-Media-Mining)
for details regarding `tmux`.

If you do not use `tmux`, then you cannot close your terminals (or the downloads are
terminated) and cannot lose internet connections.

Personally, I choose not to close my terminals. But you may want to use it.

### Logic: Vaccine Related.
If a tweet has any keywords listed in [vac_keywords.py](vac_keywords.py),
then it is vaccine related.

You can modify the list.

### Logic: Chunk
Each input segment file has `7173750` lines. A `chunk` is `10000` lines. So
there are `718` chunks per file.

We use the concept of `chunk` so that python reads in `10000` lines each time,
instead of reading the entire file.

It takes around 20 - 40 min to process each chunk. You'll see one progress bar
for one chunk. so there will be `718` progress bar for each file.

### Logic: Save
Data (vaccines related tweets) are saved to `data` folder every 5 chunk.
(100 - 200 min)

### My Current Files and Directories

```shell
$ pwd 
/home/[netid]/TwitterCovidAnalysis

# it's possible that contents in 'download/__pycache__' are different
# it's possible that contents in 'download/data/segXX' are different
$ tree -I 'env' 
.
├── download
│   ├── create_dir.py
│   ├── data
│   │   ├── README.md
│   │   ├── seg00
│   │   │   ├── chunk0_4.save
│   │   │   ├── chunk10_14.save
│   │   │   ├── chunk15_19.save
│   │   │   └── chunk5_9.save
│   │   ├── seg01
│   │   │   ├── chunk0_4.save
│   │   │   ├── chunk10_14.save
│   │   │   ├── chunk15_19.save
│   │   │   └── chunk5_9.save
│   │   ├── seg02
│   │   │   ├── chunk0_4.save
│   │   │   ├── chunk10_14.save
│   │   │   ├── chunk15_19.save
│   │   │   └── chunk5_9.save
│   │   ├── seg03
│   │   │   ├── chunk0_4.save
│   │   │   ├── chunk10_14.save
│   │   │   ├── chunk15_19.save
│   │   │   └── chunk5_9.save
│   │   ├── seg04
│   │   │   ├── chunk0_4.save
│   │   │   ├── chunk10_14.save
│   │   │   ├── chunk15_19.save
│   │   │   └── chunk5_9.save
│   │   ├── seg05
│   │   │   ├── chunk0_4.save
│   │   │   ├── chunk10_14.save
│   │   │   ├── chunk15_19.save
│   │   │   └── chunk5_9.save
│   │   ├── seg06
│   │   │   ├── chunk0_4.save
│   │   │   ├── chunk10_14.save
│   │   │   ├── chunk15_19.save
│   │   │   └── chunk5_9.save
│   │   ├── seg07
│   │   │   ├── chunk0_4.save
│   │   │   ├── chunk10_14.save
│   │   │   ├── chunk15_19.save
│   │   │   └── chunk5_9.save
│   │   ├── seg08
│   │   │   ├── chunk0_4.save
│   │   │   ├── chunk10_14.save
│   │   │   ├── chunk15_19.save
│   │   │   └── chunk5_9.save
│   │   ├── seg09
│   │   │   ├── chunk0_4.save
│   │   │   ├── chunk10_14.save
│   │   │   ├── chunk15_19.save
│   │   │   └── chunk5_9.save
│   │   ├── seg10
│   │   │   ├── chunk0_4.save
│   │   │   ├── chunk10_14.save
│   │   │   └── chunk5_9.save
│   │   ├── seg11
│   │   │   ├── chunk0_4.save
│   │   │   ├── chunk10_14.save
│   │   │   ├── chunk15_19.save
│   │   │   └── chunk5_9.save
│   │   ├── seg12
│   │   ├── seg13
│   │   ├── seg14
│   │   ├── seg15
│   │   ├── seg16
│   │   ├── seg17
│   │   ├── seg18
│   │   ├── seg19
│   │   ├── seg20
│   │   ├── seg21
│   │   ├── seg22
│   │   ├── seg23
│   │   ├── seg24
│   │   ├── seg25
│   │   ├── seg26
│   │   ├── seg27
│   │   ├── seg28
│   │   ├── seg29
│   │   ├── seg30
│   │   ├── seg31
│   │   ├── seg32
│   │   ├── seg33
│   │   ├── seg34
│   │   ├── seg35
│   │   ├── seg36
│   │   ├── seg37
│   │   ├── seg38
│   │   ├── seg39
│   │   ├── seg40
│   │   ├── seg41
│   │   ├── seg42
│   │   ├── seg43
│   │   ├── seg44
│   │   ├── seg45
│   │   ├── seg46
│   │   └── seg47
│   ├── __pycache__
│   │   ├── tokens.cpython-310.pyc
│   │   ├── utils.cpython-310.pyc
│   │   └── vac_keywords.cpython-310.pyc
│   ├── README.md
│   ├── tokens.py
│   ├── tweet_by_id.py
│   ├── utils.py
│   └── vac_keywords.py
├── full_dataset_clean.tsv
├── input
│   ├── seg00
│   ├── seg01
│   ├── seg02
│   ├── seg03
│   ├── seg04
│   ├── seg05
│   ├── seg06
│   ├── seg07
│   ├── seg08
│   ├── seg09
│   ├── seg10
│   ├── seg11
│   ├── seg12
│   ├── seg13
│   ├── seg14
│   ├── seg15
│   ├── seg16
│   ├── seg17
│   ├── seg18
│   ├── seg19
│   ├── seg20
│   ├── seg21
│   ├── seg22
│   ├── seg23
│   ├── seg24
│   ├── seg25
│   ├── seg26
│   ├── seg27
│   ├── seg28
│   ├── seg29
│   ├── seg30
│   ├── seg31
│   ├── seg32
│   ├── seg33
│   ├── seg34
│   ├── seg35
│   ├── seg36
│   ├── seg37
│   ├── seg38
│   ├── seg39
│   ├── seg40
│   ├── seg41
│   ├── seg42
│   ├── seg43
│   ├── seg44
│   ├── seg45
│   ├── seg46
│   └── seg47
├── README.md
└── tweet-keys
    ├── access-token-secret.txt
    ├── access-token.txt
    ├── api-key-secret.txt
    ├── api-key.txt
    ├── bearer-token.txt
    └── README.md

53 directories, 113 files
```





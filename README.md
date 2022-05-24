# Twitter Covid Analysis Project
This is a project that analysis people's sentiments towars Covid vaccines using
data from twitter. This is a course project for CE510 at NU 22.

Members include:
1. Zanhua Huang (ZHD1108)
2. Shujie Cao (SCO3415)

## Project Setup Guide
### Login to a NU Machine and Clone this repo
```shell
$ ssh [netid]@joker.ece.northwestern.edu
# enter your password

$ git clone [url]
# a folder called TwitterCovidAnalysis will be created
$ cd TwitterCovidAnalysis
```

### Setup Virtual Env
```shell
# make sure that you are in the project folder: TwitterCovidAnalysis
$ pwd
/home/[netid]/TwitterCovidAnalysis

# check what files are currently under the folder
# download full_dataset_clean.tsv first if you don't have one
$ ls -a
full_dataset_clean.tsv  README.md [some other files downloaded from git repo]


# create an virtual envrionment named "env"
$ python3.8 -m venv env

# a new folder called "env" is created
$ ls
env  full_dataset_clean.tsv  README.md [some other files downloaded from git repo]

# activate the virtual env:
$ source env/bin/activate  # if using bash/zsh/etc
$ source env/bin/activate.csh  # if using tcsh/etc

# make sure you are using the virtual env
$ which python
~/TwitterCovidAnalysis/env/bin/python

$ which pip
~/TwitterCovidAnalysis/env/bin/pip

# upgrade pip
$ pip install --upgrade pip

# download packages:
pip install numpy matplotlib scipy pandas tweepy tqdm

```
### Setup Twitter Developer Account
The link is [here](https://developer.twitter.com/)

After setting up a developer account, please also apply for academic research access.
Details about academic research access is [here](https://developer.twitter.com/en/products/twitter-api/academic-research).

You can apply for the academic research access from your devloper protal.

Note that tweet-keys folder contains my keys and tokens.  Now you can use my keys and tokens directly instead of creating your own.

### Saving Keys and Tokens Locally.

Save your keys and tokens under `tweet-keys` folder. 
**DO NOT distribute your keys and tokens to others.**

~~Contents inside `tweet-keys` folder will not be synced to git repo.
(so do not worry about privacy)~~
Currently the `tweet-keys` folder is synced so that both teammates can work on the project. Now you can use my keys and tokens directly instead of creating your own.

After saving the keys and tokens, your directories should look like:

```shell
$ pwd
/home/[netid]/TwitterCovidAnalysis

# results; show file structures, excluding 'env' folder
$ tree -I 'env'
.
├── download
│   ├── README.md
│   ├── tokens.py
│   └── tweet_by_id.py
├── full_dataset_clean.tsv
├── README.md
└── tweet-keys
    ├── access-token-secret.txt
    ├── access-token.txt
    ├── api-key-secret.txt
    ├── api-key.txt
    ├── bearer-token.txt
    └── README.md

2 directories, 11 files
```

## Project Details
### Part1: Data Download
The file `full_dataset_clean.tsv` contains IDs of tweets that we need to download.
This file is available from [link to zenodo](https://zenodo.org/record/6481639)

The folder [download](download) contains codes and logics to download full texts using IDs. Refer to [download/README.md](download/README.md) for more details.

An initial version of ouput file [vac_related.csv](vac_related.csv) will be produced in side folder [download](download/). This file contains entries of tweets with the following feilds:
```txt
line_num; tweet_id; region; date; time; sentiments
```

Up to now, this file is in its **initial** version. By "initial" it means the values for `sentiments` are unset. They will be appropiately set in the next section (Sentiment Analysis).

### Part2: Sentiment Analysis
This part performs sentiment analysis over each tweet. It analysis the attitude of each tweet towards covid vaccines and marks each tweet as  `positive`, `neutral` or `negative`. 

The folder [sentiments](sentiments) contains codes and logics related to sentiment analysis.  Refer to [sentiments/README.md](sentiments/README.md) for more details.

### Part3: Pearson Correlation Coefficient Test
This part related time to general attitude. It analysis people's general attitudes towards covid vaccine among a particular time. 

The folder [pearson](pearson) contains codes and logics related to sentiment analysis.  Refer to [pearson/README.md](sentimepearsonnts/README.md) for more details.

### Part4: Data Visualization and Display
This part contains codes that performs an interactive data visualization and display.

The folder [display](display) contains codes and logics related to sentiment analysis.  Refer to [display/README.md](display/README.md) for more details.

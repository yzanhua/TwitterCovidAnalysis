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
pip install numpy matplotlib scipy pandas tweepy

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

To download data:
```shell
# working directory
$ pwd
/home/[netid]/TwitterCovidAnalysis

# enable the virtual env
$ source env/bin/activate  # if using bash/zsh/etc
$ source env/bin/activate.csh  # if using tcsh/etc

# go to download folder
$ cd download

# run tweet_by_id.py; and example output
$ python tweet_by_id.py

===========
Getting tid: 1213330173736738817
Getting date: 2020-01-04
Getting time: 05:23:50
Getting lang: en
Getting region: nan
@shehryar_taseer That’s 💯 true , 
Corona virus 
swine flue 
Bird flu in December when whole Pk is busy in Marriage halls eating multiple chicken dishes 
flu shots r billion$$ industry alone in western world                                        
```

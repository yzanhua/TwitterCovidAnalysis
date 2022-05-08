# Twitter Covid Analysis Project
This is a project that analysis people's sentiments towars Covid vaccines using
data from twitter. This is a course project for CE510 at NU 22.

Members include:
1. Zanhua Huang (ZHD1108)
2. Name (NetID)

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

Save your keys and tokens under `tweet-keys` folder.
Contents inside this folder will not be pushed to git repo.
(so do not worry about privacy)

```shell
$ pwd
/home/[netid]/TwitterCovidAnalysis

# save keys and tokens 

# results; show file structures, excluding 'env' folder
$ tree -I 'env'
.
├── download
│   ├── codes.py
│   ├── tweepy_example.py
│   └── tweet_by_id.py
├── full_dataset_clean.tsv
├── README.md
└── tweet-keys
    ├── access-token-secret.txt
    ├── access-token.txt
    ├── api-key-secret.txt
    ├── api-key.txt
    └── bearer-token.txt

2 directories, 10 files
```
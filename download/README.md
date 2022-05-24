# Tweets Download
This folder contains all codes and logics to download full tweets using tweet ids.
We assume that you have already downloaded the file `full_dataset_clean.tsv` to the project root folder. This file is available from [link to zenodo](https://zenodo.org/record/6481639)

Use commnad `git pull` to update codes from github repo.

## Prepocessing
1. **Preparation**: It is important to make sure your codes are up-to-date. Also, make sure python virtual env is activated and related python packages are installed.
    ```shell
    $ pwd  # show working directory; outside download (this folder)
    /home/[netid]/TwitterCovidAnalysis

    $ git pull  # update codes

    # Activate virtual env
    $ source env/bin/activate  # if using bash/zsh/etc
    $ source env/bin/activate.csh  # if using tcsh/etc

    # upgerade pip (this command is run before; no need to run twice)
    $ pip install --upgrade pip

    # download packages:
    pip install numpy matplotlib scipy pandas tweepy tqdm

    # continue working on the project.
    ...

    ```
2. **Keys and Tokens**: The next step is to setup keys and tokens for twitter developer account.

    [tokens.py](tokens.py) read keys and tokens from [tweet-keys](../tweet-keys/) folder. Please put your keys and tokens in that folder.

2. **Split Input**:
`full_dataset_clean.tsv` contains `344339998` lines. Which is too large to process, or at least difficult for parallelization. Therefore, we will first split it to 48 files, with each containing 7173750 line.

    We'll call the split files as segment files or segments.

    The following is a step by step guide to split the input on a linux machine.

    ```shell
    $ pwd  # show working directory; outside download (this folder)
    /home/[netid]/TwitterCovidAnalysis

    $ ls  # check what files and folders are
    README.md  display    download   env  pearson    sentiments tweet-keys

    $ mkdir input  # create an "input" folder.
    $ ls  # check again
    input README.md  display    download   env  pearson    sentiments tweet-keys

    $ cd input  # go to input folder

    # split the tsv; each file has 7173750; 48 files will be created.
    $ split -l 7173750 -d ../full_dataset_clean.tsv seg

    $ ls 
    # seg00 to seg47
    ```

3. **Create Output Folders**: We need to create some folders for output files.

    ```shell
    $ pwd  # show working directory; you should be in download (this folder)
    /home/[netid]/TwitterCovidAnalysis/download

    $ ls  
    create_dir.py  data  README.md  tokens.py  tweet_by_id.py  [some other files]

    $ python create_dir.py  # create the `data` folder and its subfolders.

    $ ls data  # seg00 ~ seg47 are 48 (empty) folders, one for each segment.
    README.md  seg00 ~ seg47
    ```


## Download Vaccine Related Tweets
`tweet_by_id.py` downloads tweets using IDs.

Only tweets related to vaccines are saved
to [data](./data) folder.

**Important**: Activate virtual env first.

### General Usage
```shell
# activate virtual env

$ pwd  # current working directory
/home/[netid]/TwitterCovidAnalysis/download

# download tweets from 
# seg_id: an integer from 0 to 47, which indicates input segment file `../input/seg[seg_id]`.
# chunk_id: an integer indicating which chunk to start from for this file. Refer to sections: Logic: Chunk and Logic: Manual Rrestart below for more details
$ python tweet_by_id.py [seg_id:int] [chunk_id:int]

# An example run: 
$ python tweet_by_id.py 47 0

# A progess bar will show.
# After completing the first bar, 700+ more bars are expected.
# Will take days to complete. 
```

### Concurrent Download
You can invoke `tweet_by_id.py` from differnt terminal, so that these
terminals can download and process concurrently.

For example, the following codes download and process 
`../input/seg47`, `../input/seg46`, and `../input/seg27`
concurrently (if in 3 different terminals).
```shell
# from terminal 1
$ python tweet_by_id.py 47 0

# from another terminal 2
$ python tweet_by_id.py 46 0

# from another terminal 3
$ python tweet_by_id.py 27 0
```


```shell
# in terminal x (x in [0, 1, 2, ..., 7])
# replace [47-x] with actual val.
python tweet_by_id.py [47-x] 0
```

### Tmux (Optional)
Refer to [this github repo](https://github.com/reda-bahrani/CE510-Social-Media-Mining)
for details regarding `tmux`.

This step is optinal but if you do not use `tmux`, you cannot close your terminals and cannot lose internet connections, otherwise the downloads will be terminated.


## Logic: 
This section explains some implementation details regarding the codes.

## Vaccine Related
How we define a tweet is vaccine related? If a tweet has any keywords listed in [vac_keywords.py](vac_keywords.py), then it is vaccine related. You can ofcourse modify the list to satisfy your need.

### Chunk
In our case, each input segment file has `7173750` lines. This is still too large for a python thread to read in directly. Therefore, we define a `chunk` to be `10000` lines, meaning there are `718` chunks per segment file.

We use the concept of `chunk` so that python reads in `10000` lines each time, instead of reading the entire file.

Command `python tweet_by_id.py 27 0` will start processing segment file `seg27` from the first chunk `chunk0`. One progress bar will show in the terminal for each chunk, so there will be `718` progress bar for each file.

### Save and Output
Data (vaccines related tweets) are saved to `data` folder every 5 chunk.
(100 - 200 min)

### Manual Restart
It's possible that your downloading process is accidently terminated due to unexpected reasons including but not limited to an internet error or hardware failure.

We offer a way to manually restart the downloading process from where you left.

For example, if something goes wrong when processing `chunk 100` for file `seg77`, you can restart frin chunk 100 using command
```shell
$ python tweet_by_id 77 100
```
Sine outputs are saved every 5 chunk, the argument of restart chunk id must be multiples of 5.
```shell
$ python tweet_by_id 77 101 # 101 is not allowed.
```

## Post Processing
We'll combine all the downloaded tweets in [data](data) folder to one csv file.

```
$ python combine.py
```

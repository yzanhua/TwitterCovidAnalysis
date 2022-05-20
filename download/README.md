# Tweets Download
This folder contains all codes and logics to download full tweets using tweet ids.

## Keys and Tokens
`tokens.py` read keys and tokens from [tweet-keys](../tweet-keys/) folder. ~~The [tweet-keys](../tweet-keys/) folder is not synced with the github repo so one safely save data there.~~ Currently [tweet-keys](../tweet-keys/) folder is synced so that both teammates can work on the project. 


`tokens.py` is synced with the github repo, so we do not put our tokens and keys directly in this file.

## Download by ID
`tweet_by_id.py` downloads tweets using IDs. Currently working. Remeber to
hit [ctrl-c] to terminate program.

Tweets are downloaded to [data](./data) folder.

### TODO
Implement `not_vaccine_related` in utils.py.
```python
def not_vaccine_related(full_text):
    # input: full_text, str
    # output: bool, True if **NOT** related to vaccine 
    
    if full_text is None:
        return True
    
    # if full_text is NOT related to vaccine:
        # return True
    
    return False
```
```shell
# activate virtual env

# working directory
$ pwd
/home/[netid]/TwitterCovidAnalysis/download

# download 
$ python tweet_by_id.py 0  # download the first half of the entire tweets dataset
$ python tweet_by_id.py 1  # download the second half of the entire tweets dataset
```
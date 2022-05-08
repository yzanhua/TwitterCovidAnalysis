	# # Go to http://apps.twitter.com and create an app.
# # The consumer key and secret will be generated for you after
consumer_key=''
consumer_secret=''

# # After the step above, you will be redirected to your app's page.
# # Create an access token under the the "Your access token" section
access_token=''
access_token_secret=''

# bearer_token
bearer_token = ''

with open("../tweet-keys/api-key.txt", 'r') as file:
    consumer_key = file.readline().strip()

with open("../tweet-keys/api-key-secret.txt", 'r') as file:
    consumer_secret = file.readline().strip()

with open("../tweet-keys/access-token.txt", 'r') as file:
    access_token = file.readline().strip()

with open("../tweet-keys/access-token-secret.txt", 'r') as file:
    access_token_secret = file.readline().strip()
with open("../tweet-keys/bearer-token.txt", 'r') as file:
    bearer_token = file.readline().strip()


if __name__ == "__main__":
    print(consumer_key)
    print(consumer_secret)
    print(access_token)
    print(access_token_secret)
    print(bearer_token)

'''
Local Settings for a heroku_ebooks account. #badcanine
'''

#configuration
MY_CONSUMER_KEY = '2UtvzW3R5Dfq7U5ieJepYzZEO'
MY_CONSUMER_SECRET = ' UeDb5nw3lHdyyDh5Cmtm9PjDD1QUJ4sR34AHlnIkErizqYFZ94'
MY_ACCESS_TOKEN_KEY = ' 3407745641-3NjZw4Eqp7z9e4AgsiMEAELaZqZdAcN4IVfpJld'
MY_ACCESS_TOKEN_SECRET = '1jqXF5HyZltMmZU84GEZkpdqD3Bm5l05qKulcoXXqU9Nz'

SOURCE_ACCOUNTS = [""] #A list of comma-separated, quote-enclosed Twitter handles of account that you'll generate tweets based on. It should look like ["account1", "account2"]. If you want just one account, no comma needed.
ODDS = 8 #How often do you want this to run? 1/8 times?
ORDER = 2 #how closely do you want this to hew to sensical? 1 is low and 3 is high.
DEBUG = True #Set this to False to start Tweeting live
STATIC_TEST = False #Set this to True if you want to test Markov generation from a static file instead of the API.
TEST_SOURCE = ".txt" #The name of a text file of a string-ified list for testing. To avoid unnecessarily hitting Twitter API.
TWEET_ACCOUNT = "badcanine" #The name of the account you're tweeting to.

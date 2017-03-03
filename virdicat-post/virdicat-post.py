import twitter
import random
import os
from virdicatdb import VirdicatDb

TARGET = os.environ['TARGET_USER']
TWITTER_CONSUMER_KEY = os.environ['TWITTER_CONSUMER_KEY']
TWITTER_CONSUMER_SECRET = os.environ['TWITTER_CONSUMER_SECRET']
TWITTER_ACCESS_TOKEN_KEY = os.environ['TWITTER_ACCESS_TOKEN_KEY']
TWITTER_ACCESS_TOKEN_SECRET = os.environ['TWITTER_ACCESS_TOKEN_SECRET']

def tweet(text, media=None):
    api = twitter.Api(consumer_key=TWITTER_CONSUMER_KEY,
                      consumer_secret=TWITTER_CONSUMER_SECRET,
                      access_token_key=TWITTER_ACCESS_TOKEN_KEY,
                      access_token_secret=TWITTER_ACCESS_TOKEN_SECRET)
    
    status = api.PostUpdate(text, media)
    return status

def lambda_handler(event, context):
    db = VirdicatDb()
    content = db.get_content_options()
    
    if len(content) > 0:
        selected = random.choice(content)
        print('using' + str(selected))
        text = TARGET
        if selected['Type'] == 'MEDIA':
            tweet(text,selected['Link'])
        else:
            tweet(text + ' ' + selected['Link'])
        db.set_content_used(selected)

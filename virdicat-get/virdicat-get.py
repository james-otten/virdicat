import praw
import os
from virdicatdb import VirdicatDb

REDDIT_CLIENT_ID = os.environ['REDDIT_CLIENT_ID']
REDDIT_CLIENT_SECRET = os.environ['REDDIT_CLIENT_SECRET']
REDDIT_USER_AGENT = os.environ['REDDIT_USER_AGENT']
REDDIT_USER = os.environ['REDDIT_USER']
REDDIT_PASSWORD = os.environ['REDDIT_PASSWORD']

def create_reddit():
    return praw.Reddit(client_id=REDDIT_CLIENT_ID,
                       client_secret=REDDIT_CLIENT_SECRET,
                       user_agent=REDDIT_USER_AGENT,
                       username=REDDIT_USER,
                       password=REDDIT_PASSWORD)

def get_media_type(url):
    t = 'LINK'
    if url.split('.')[-1] != 'gifv':
        t = 'MEDIA'
    return t

def lambda_handler(event, context):
    db = VirdicatDb()
    reddit = create_reddit()
    
    last_seen_link = db.get_last_seen()
    new_last_seen = None

    items = reddit.redditor(REDDIT_USER).upvoted(limit=100)
    for item in items:
        if last_seen_link == item.url:
            break
        media_type = get_media_type(item.url)
        this_id = db.create_content(item.url, media_type)
        if new_last_seen == None:
            db.set_last_seen(this_id)

# virdicat
virdicat is a serverless twitter bot.

## virdicat-get
Gets posts upvoted by a specific reddit account and puts them in DynamoDB.

Handler: virdicat-get.lambda_handler

Configure the follwing environment variables:

| Name                 | Description                                    |
| -------------------- |----------------------------------------------- |
| REDDIT_USER          | Reddit username                                |
| REDDIT_USER_AGENT    | User agent to use when interacting with reddit |
| REDDIT_CLIENT_ID     | Client ID from reddit                          |
| REDDIT_PASSWORD      | Reddit password                                |
| REDDIT_CLIENT_SECRET | Client secret from reddit                      |

## virdicat-post
Posts an item from DynamoDB to twitter using python-twitter.

Handler: virdicat-post.lambda_handler

Configure the follwing environment variables:

| Name                         | Description                            |
| ---------------------------- |--------------------------------------- |
| TWITTER_CONSUMER_SECRET      | Consumer secret from twitter           |
| TWITTER_CONSUMER_KEY         | Consumer key from twitter              |
| TWITTER_ACCESS_TOKEN_KEY     | Access token key from twitter          |
| TWITTER_ACCESS_TOKEN_SECRET  | Access token secret from twitter       |
| TARGET_USER                  | Twitter user to tweet at (includes @)  |

## Build
The supplied makefile will pull in dependencies and create zip files ready to be uploaded to AWS Lambda.

Build with: `make`


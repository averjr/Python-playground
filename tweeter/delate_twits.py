import tweepy

access_token = ""
access_token_secret = ""
consumer_key = ""
consumer_secret = ""


def oauth_login():
    """Authenticate with twitter using OAuth"""

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)

    return api


def batch_delete(api):

    for status in tweepy.Cursor(api.user_timeline).items():
        try:
            api.destroy_status(status.id)
            print("Deleted:", status.id)
        except tweepy.TweepError as e:
            print("Failed to delete:", status.id)


if __name__ == "__main__":
    api = oauth_login()
    batch_delete(api)

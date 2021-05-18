
def getCommandFromTweetText(tweetText):
    strings = tweetText.split(" ")
    filteredStrings = [x for x in strings if not x.lower().startswith('@')]

    if len(filteredStrings) == 0:
        return False
    return {
            "command": filteredStrings[0],
            "args": filteredStrings[1:len(filteredStrings)]
    }


def extractTextFromTweet(tweet, isExtended = True):
    text = ""
    if isExtended:
        if 'retweeted_status' in dir(tweet):
            text=tweet.retweeted_status.full_text
        else:
            text=tweet.full_text
    else:
        text = tweet.text
    return text


def getCompactTweet(tweet, isExtended = True):
    return {
            "id": tweet.id_str,
            "text": extractTextFromTweet(tweet, isExtended),
            "name": tweet.user.name,
            "username": tweet.user.screen_name,
            "time": str(tweet.user.created_at),
            "image": tweet.user.profile_image_url,
            "image_https": tweet.user.profile_image_url_https,
            "likes": tweet.favorite_count,
            "retweets": tweet.retweet_count,
    }

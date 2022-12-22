import openai
import tweepy
import random


class TwitterBot():

    api_key = "6FD1PT1SYFTz3yafCSYaviifK"
    api_key_secret = "IxeSCOA5FL5VaSirT3efPbNjctpWeDY3a6WhFt5YkWwj3kLt0h"
    access_token = "1605544374523265024-Vg07LEQ5llLSfte1wArGVpqaYgI5Po"
    access_token_secret = "lXLRBl446tzfWzluXMoxDOhVMOOZoRwxYmBChQ60vxphk"

    openai.api_key = "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"

    auth = tweepy.OAuthHandler(api_key, api_key_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True)

    def __init__(self):
        error = 1
        while (error == 1):
            tweet = self.create_tweet()
            try:
                error = 0
                self.api.update_status(tweet)
            except:
                error = 1

    def lerTweets():
        


    def create_tweet(self):
        chosen_prompt = random.choice(self.prompts)
        text = chosen_prompt["text"]
        hashtags = chosen_prompt["hashtag"]

        response = openai.Completion.create(
            engine="text-davinci-001",
            prompt=text,
            max_tokens=64,
        )

        tweet = response.choices[0].text
        tweet = tweet + " " + hashtags
        return tweet


twitter = TwitterBot()
twitter.create_tweet()

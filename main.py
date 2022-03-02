# Set the testing to True if you are testing your code on a laptop and not the pi
global testing
testing = True

# Import the necessary modules
import tweepy
import os

if not testing:
    import RPi.GPIO as GPIO
import time


# This function turn the relay switch on and off
def switch(x):
    if not testing:
        GPIO.setwarnings(False)
        Relay_Ch3 = 21
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(Relay_Ch3, GPIO.OUT)
        if x:
            GPIO.output(Relay_Ch3, GPIO.LOW)
        else:
            GPIO.output(Relay_Ch3, GPIO.HIGH)
        time.sleep(1)
    else:
        if x:
            print("ON")
        else:
            print("OFF")


def bootUp():
    time.sleep(0.5)
    switch(True)
    time.sleep(0.5)
    switch(False)
    readText("Some nonsense start up tune, do, do, do, do do")


# This splits larger texts into smaller one (text over 100 bytes)
def splitLargeMessage(message):
    messages = []
    shortMessage = ""
    if len(message) < 100:
        return [message]
    for word in message.split(" "):
        shortMessage += word + " "
        if len(shortMessage) >= 100:
            shortMessage.rstrip(word + " ")
            messages.append(shortMessage.rstrip(" "))
            shortMessage = ""


# This reads out the text via Google voice (sounds the best)
def readText(message):
    if not testing:
        os.system('speaker-test -t sine -f 1 -c 2 -s 1')
        for smallMessage in splitLargeMessage(message):
            os.system('/home/pi/speech.sh "' + smallMessage + '"')
        os.system('speaker-test -t sine -f 1 -c 2 -s 1')
    else:
        for smallMessage in splitLargeMessage(message):
            print(smallMessage)


# Gets a tweet from any user, default is ME :)
def get_tweet(user="S_Easley_Walsh"):
    bearer_token = "hidden from git"
    client = tweepy.Client(bearer_token)
    query = 'from:' + user
    tweets = client.search_recent_tweets(query=query, tweet_fields=['context_annotations', 'created_at'],
                                         max_results=100)
    for tweet in tweets.data:
        return tweet.text


# Booting Up
bootUp()


# Checks for latest tweet and reads it
latestTweet = ""
while True:
    tmp = get_tweet()
    if not latestTweet == tmp:
        latestTweet = tmp
        switch(True)
        readText(latestTweet)
        switch(False)
    time.sleep(10)

import random
import sys
import os
import markovify
import time
import twitter
import string
import json
from markov import markovModel
from poems import makeRhymeLines

'''
REST api for single searches

Use Tweepy or something I give up what the fuck are you doing just commit and go to bed.
'''


def getAPI(file):
    with open(file, 'r') as prefs:
        textArray = []
        lineNum = 0
        for line in prefs:
            textArray.append(line)
            lineNum = lineNum + 1
        #print(textArray)
        for i in range(4):
            indexStart = textArray[i].index('=') + 2
            textArray[i] = (textArray[i])[indexStart:-2]
            #print(textArray[i])


        api = twitter.Api(consumer_key=textArray[0],
                          consumer_secret=textArray[1],
                          access_token_key=textArray[2],
                          access_token_secret=textArray[3]
                          )
        return api

def tweetFourLinePoem(api):
    tweetText = ""
    for i in range(4):
        tweetText = tweetText + markovModel.make_short_sentence(max_chars=34) + "\n"  # 34*4 = 136 + 4(\n)(<-Worst case)

    api.PostUpdate(tweetText)

def tweetFourLineRhymed(api):
    tweetText = ""
    part1 = makeRhymeLines()
    part2 = makeRhymeLines()
    for i in range(2):
        tweetText = tweetText + part1[i] + "\n" + part2[i] + "\n"
        print(tweetText)

    api.PostUpdate(tweetText)

#tweetFourLineRhymed(getAPI('Preferences.txt'))

def testEfficiency():
    totalTries = 0
    totalSuccesses = 0
    while True:
        tweetFourLineRhymed(getAPI('Preferences.txt'))
        print('Done')
    return True

def giveStatusId(status):
    statusArray = status.split(",")
    statusId = statusArray[2]
    print(statusId)

def replyWithFire():        #This should be the main command basically. (Don't fuck it up Larry)
    mentions = api.GetMentions()
    print(mentions[1])
    print (mentions[1].id)


def listen(api):
    with open('listenOut.txt', 'a') as f:
        for line in api.GetUserStream():
            f.write(json.dumps(line))
            f.write('\n')



#tweetFourLineRhymed(getAPI('Preferences.txt'))
api = getAPI('Preferences.txt')
#replyWithFire()

while True:
    print(api.GetStreamSample())
    listen(api)










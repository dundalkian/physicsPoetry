import random
import sys
import os
import markovify
import time
import twitter
import string
from markov import markovModel


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
        tweetText = tweetText + markovModel.make_short_sentence(max_chars=34) + "\n"  #34*4 = 136 + 4(\n)

    api.PostUpdate(tweetText)
import random
import sys
import os
import markovify
import time
import twitter

'''
So I am 90% sure that currently it creates/erases a .txt file. It then runs the aptly
named theScript() function which opens that .txt file to append. It then uses somebody else's
space magic to create a markov chain model based on Emily Dickinson poems, it then spits out
poems in 10 line groupings every second. 

Why am I doing this I hear you ask? 
    -answer coming with next update.
'''

'''
Random Ideas for the actual completion of this bot, because tests are stressful and I forget things

Learn twitter API -> make this an actual bot

You might be able to use something like Gooogle N-gram viewer (the stuff behind that) to see
if lines of text are related. Making the poems actually have topics would be great.


Syllable counting is easy (I've seen other projects have it so I am just assuming) but it
would be cool to have different options for that. 
(Not important Larry, don't waste time doing this and pretend you accomplished something)
 (^^I know you^^)
'''

with open('Preferences.txt', 'r') as pref:
    textArray = []
    lineNum = 0
    for line in pref:
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

def tweetFourLinePoem():
    tweetText = ""
    with open("hellaPoems.txt") as f:
        corpusText = f.read()

    markovModel = markovify.NewlineText(corpusText)

    for i in range(4):
        tweetText = tweetText + markovModel.make_short_sentence(max_chars=34) + "\n"  #34*4 = 136 + 4(\n)

    api.PostUpdate(tweetText)


def theScript():
    testMarkov = open("test.txt", "a")
    #testMarkov.write(bytes("Txt to write\n", 'UTF-8'))

    with open("hellaPoems.txt") as f:
        text = f.read()

    text_model = markovify.NewlineText(text)


    for i in range(5):
        print(text_model.make_short_sentence(max_chars=28) + "\n")
        testMarkov.write((text_model.make_sentence(tries=100) + "\n"))

    testMarkov.write("\n")


    testMarkov.close()


tweetFourLinePoem()











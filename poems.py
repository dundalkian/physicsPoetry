import random
import sys
import os
import markovify
import time
import twitter

#testMarkov = open("test.txt" , "wb")
#testMarkov.write(bytes("Txt to write", 'UTF-8'))


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
def getAPI():
    with open('Preferences.txt', 'r') as prefs:
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

'''
Yeah Reinhardt, I didn't comment my function, what are you going to do about it now?
'''
def areWords(str1, str2):
    found1 = False
    found2 = False
    with open('iphod2.txt', 'r') as rhymes:
        #indexStart
        for lines in rhymes:
            if str1 in lines:
                found1 = True
            if str2 in lines:
                found2 = True
    if found1 & found2:
        rhymes.close()
        return True
    else:
        #might be a case mismatch also, I honestly don't give a fuck though, deal with it.
        rhymes.close()
        return False


def isRhyme(str1, str2):
    if not areWords(str1, str2):
        return False  # eventually should redirect to the psuedowords, but Dickinson uses real words... so, just no.
    strPhone1 = ''  # Strings representing phonemes
    strPhone2 = ''
    with open('iphod2.txt', 'r') as rhymes:
        # indexStart
        for lines in rhymes:
            if str1 in lines:
                strPhone1 = lines
            if str2 in lines:
                strPhone2 = lines
    indexPhone1 = findIndex(strPhone1, '\t', 3)
    indexPhone2 = findIndex(strPhone2, '\t', 3)

    #temp takes in phonemes one at a time and works backwards, (gets OW, shit happens, gets K...)
    temp1 = strPhone1[:indexPhone1]
    temp2 =

def findIndexReverse(string, subString, n, start):
    index = string.find(subString,end=start)  # end is equal to start, idk anymore, kill me soon.
    while n > 1:
        indexStart = string.find(subString, index + len(subString))
        n = n - 1
    return index


def findIndex(string, subString, n):  # Find index of nth occurence of a string within strings
    index = string.find(subString)
    while n > 1:
        indexStart = string.find(subString, index+len(subString))
        n = n-1
    return index


def tweetFourLinePoem(api):
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

tweetFourLinePoem(getAPI())
isRhyme('\tton\t', 'zuni')











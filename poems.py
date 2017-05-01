import random
import sys
import os
import markovify
import time
import twitter
import string
from markov import markovModel


#testMarkov = open("test.txt" , "wb")
#testMarkov.write(bytes("Txt to write", 'UTF-8'))


'''
For some reason "ME" and "YESTERDAY" count as a rhyme FIX THIS!!!!!!!!!!


Why am I doing this I hear you ask? 
    -answer coming with next update.
    - ............ I just spent 3 hours on code I can't use because it was written so bad
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


'''
Yeah Reinhardt, I didn't comment my function, what are you going to do about it now?

.... Okay literally, past Larry, you are a fucking idiot, like this function is fine, but I know you wrote that
isRhyme function and that literally makes no sense. Now I have to pick up all the pieces.
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


def givePhonemeLine(str):
    strPhoneme = '' #empty string to represent phoneme
    with open('iphod2.txt', 'r') as rhymes:
        for lines in rhymes:
            if str in lines:
                strPhoneme = lines
    if strPhoneme == '':
        raise ValueError('This may not be a word, if it is ... RIP.')
    return strPhoneme

def iphodArrayFromString(iphodString):
    iphodArray = iphodString.split("\t")
    return iphodArray

def phonemeArrayFromArray(iphodInfoArray):
    phonemeArray = iphodInfoArray[3].split(".")
    return phonemeArray


#pass in only iphod phoneme arrays
# returns -1 for identical arrays, 0 if no phonemes in common, the number of shared phonemes
def numPhonemesShared(phoneArray1, phoneArray2):
    if phoneArray1 == phoneArray2:
        return -1
    minPhonemes = -1
    numPhonemes = 0
    if len(phoneArray1) >= len(phoneArray2):
        minPhonemes = len(phoneArray2)
    if len(phoneArray1) <= len(phoneArray2):
        minPhonemes = len(phoneArray1)

    for i in range(minPhonemes):
        if phoneArray1[len(phoneArray1) - 1 - i] == phoneArray2[len(phoneArray2) - 1 - i]:
           # print('At least one phone')
            #print(phoneArray1)
            #print(phoneArray2)
            numPhonemes += 1
        else:
            return numPhonemes
    return numPhonemes

#Returns -1 for no apparent rhyme or not words, 0 for identical pronounciation, 1 for apparent rhyme
def compareRhyme(str1, str2):
    if not areWords(str1, str2):
        #print('not words')
        return -1  # eventually should redirect to the psuedowords, but Dickinson uses real words... so, just no.

    strPhone1 = givePhonemeLine(str1)  # strings representing phonemes
    strPhone2 = givePhonemeLine(str2)

    iphodInfoArray1 = iphodArrayFromString(strPhone1)
    iphodInfoArray2 = iphodArrayFromString(strPhone2)

    phonemeArray1 = phonemeArrayFromArray(iphodInfoArray1)
    phonemeArray2 = phonemeArrayFromArray(iphodInfoArray2)

    phonemesShared = numPhonemesShared(phonemeArray1, phonemeArray2)

    if str1 == str2:
        return 0
    if phonemesShared == 0:
        #print(-1)
        return -1
    if phonemesShared == 1:
        if isVowel(phonemeArray1[len(phonemeArray1) - 1]):
            #print('hello there')
            return 1
        else:
            #print(-1)
            return -1
    if phonemesShared > 1:
        #print(1)
        return 1

def isVowel(str):
    Alpha = 'AEIOU'
    for i in range(5):
        index = str.find(Alpha[i])
        if index != -1:
            #print("vowel")
            return True
    #print("not vowel")
    return False

#Not needed / same as findIndex
def findIndexReverse(string, subString, start):
    i = 0
    index = 0
    while index != -1:
        #print(index)
        index = string.find(subString, index+1)
        i += 1
        if index >= start:
            index = -1
    i = i - 1

    index = findIndex(string, subString, i)
    return index

#Not needed / defucnt, left in to remind myself what a mank I am
def findIndex(string, subString, n):  # Find index of nth occurence of a string within strings
    index = string.find(subString)
    while n > 1:
        index = string.find(subString, index+len(subString))
        n = n - 1
    return index


def makeRhymeLines():
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    rhymeResult = -1
    #line1 = markovModel.make_short_sentence(max_chars=34)
    #line2 = markovModel.make_short_sentence(max_chars=34)
    numTries = 0

    while rhymeResult == -1 or rhymeResult == 0:
        line1 = markovModel.make_short_sentence(max_chars=34)
        line2 = markovModel.make_short_sentence(max_chars=34)

        #line1 = 'heaven;'
        #line2 = 'one'

        line1Array = []
        for i in range(len(alphabet)):
            if line1[len(line1) - 1] == alphabet[i]:
                line1Array = line1.split(" ")

        if len(line1Array) == 0:
            line1temp = line1[:-1]
            line1Array = line1temp.split(" ")

        line2Array = []
        for i in range(len(alphabet)):
            if line2[len(line2) - 1] == alphabet[i]:
                line2Array = line2.split(" ")

        if len(line2Array) == 0:
            line2temp = line2[:-1]
            line2Array = line2temp.split(" ")

        rhymeResult = compareRhyme('\t'+line1Array[-1]+'\t', '\t'+line2Array[-1]+'\t')
        #print(rhymeResult)
        numTries += 1

        if numTries > 100000:
            print('I fucking give up')
            raise ValueError('I am sorry, but I tried so many times I gave up, I am lazy, I know')


    print (numTries)
    return [line1,line2]
    #return numTries




'''
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
'''


def makeRhymeLinesTest():
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    rhymeResult = -1
    line1 = markovModel.make_short_sentence(max_chars=34)
    #line2 = markovModel.make_short_sentence(max_chars=34)
    numTries = 0

    while rhymeResult == -1 or rhymeResult == 0:
        #line1 = markovModel.make_short_sentence(max_chars=34)
        line2 = markovModel.make_short_sentence(max_chars=34)

        #line1 = 'heaven;'
        #line2 = 'one'

        line1Array = []
        for i in range(len(alphabet)):
            if line1[len(line1) - 1] == alphabet[i]:
                line1Array = line1.split(" ")

        if len(line1Array) == 0:
            line1temp = line1[:-1]
            line1Array = line1temp.split(" ")

        line2Array = []
        for i in range(len(alphabet)):
            if line2[len(line2) - 1] == alphabet[i]:
                line2Array = line2.split(" ")

        if len(line2Array) == 0:
            line2temp = line2[:-1]
            line2Array = line2temp.split(" ")

        rhymeResult = compareRhyme('\t'+line1Array[-1]+'\t', '\t'+line2Array[-1]+'\t')
        #print(rhymeResult)
        numTries += 1

        if numTries > 100000:
            print('I fucking give up')
            raise ValueError('I am sorry, but I tried so many times I gave up, I am lazy, I know')


    print (numTries)
    #return [line1,line2]
    return numTries

#tweetFourLinePoem(getAPI('Preferences.txt'))
#isRhyme('\tbolt\t', '\tsnow\t')
#makeTwoLines()



def testEfficiency():
    totalTries = 0
    totalSuccesses = 0
    while True:
        totalTries = totalTries + makeRhymeLinesTest()
        totalSuccesses += 1
        average = totalTries / totalSuccesses
        print (average)


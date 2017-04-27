import random
import sys
import os
import markovify
import time
import twitter
import string

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
        print('not words')
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
   # print(indexPhone1)
    indexPhone2 = findIndex(strPhone2, '\t', 3)
   # print(indexPhone2)

    #temp takes in phonemes one at a time and works backwards, (gets OW, shit happens, gets K...)
    temp1 = strPhone1[findIndexReverse(strPhone1, '.', indexPhone1):indexPhone1]
    temp2 = strPhone2[findIndexReverse(strPhone2, '.', indexPhone2):indexPhone2]
    if temp1 != temp2:
        print("not the same")
        return False
    if isVowel(temp1):
        temp1 = strPhone1[findIndexReverse(strPhone1, '.', findIndexReverse(strPhone1, '.', indexPhone1)):findIndexReverse(strPhone1, '.', indexPhone1)]
        temp2 = strPhone2[findIndexReverse(strPhone2, '.', findIndexReverse(strPhone2, '.', indexPhone2)):findIndexReverse(strPhone2, '.', indexPhone2)]
        print(temp1)
        if temp1 == '':
            #print('hello there')
            temp1 = '.' + strPhone1[findIndexReverse(strPhone1, '\t', findIndexReverse(strPhone1, '.', indexPhone1)) + 1:findIndexReverse(strPhone1, '.', indexPhone1)]
            print(temp1)
        if temp1 == '':
            #print('General')
            x=0
        print(temp2)
        if temp1 != temp2:
            print('flase')
            return False
        else:
            print('True')
            return True
    else:
        temp1 = strPhone1[findIndexReverse(strPhone1, '.', indexPhone1):indexPhone1]
        temp2 = strPhone2[findIndexReverse(strPhone2, '.', indexPhone2):indexPhone2]
        if temp1 != temp2:
            #print("why is it here")
            return False



def isVowel(str):
    Alpha = 'AEIOU'
    for i in range(5):
        index = str.find(Alpha[i])
        if index != -1:
            #print("vowel")
            return True
    #print("not vowel")
    return False
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


def findIndex(string, subString, n):  # Find index of nth occurence of a string within strings
    index = string.find(subString)
    while n > 1:
        index = string.find(subString, index+len(subString))
        n = n - 1
    return index


def tweetFourLinePoem(api):
    tweetText = ""
    with open("hellaPoems.txt") as f:
        corpusText = f.read()

    markovModel = markovify.NewlineText(corpusText)

    for i in range(4):
        tweetText = tweetText + markovModel.make_short_sentence(max_chars=34) + "\n"  #34*4 = 136 + 4(\n)

    api.PostUpdate(tweetText)

def makeTwoLines():
    with open("hellaPoems.txt") as f:
        corpusText = f.read()

    markovModel = markovify.NewlineText(corpusText)
    Alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'

    line1 = markovModel.make_short_sentence(max_chars=34)
    line2 = markovModel.make_short_sentence(max_chars=34)
    print(line1)


    indexLast1 = findIndexReverse(line1, ' ', len(line1))
    indexLast2 = findIndexReverse(line2, ' ', len(line2))

    charLast1 = line1[len(line1) - 1:len(line1)]
    charLast2 = line2[len(line2) - 1:len(line2)]

    endLine1 = len(line1)
    endLine2 = len(line2)
    booly1 = False
    for i in range(len(Alphabet)):
        booly1 = False
        if charLast1 == Alphabet[i]:
            booly1 = True



    if booly1 == False:
        endLine1 = endLine1 - 1

    booly2 = False
    for i in range(len(Alphabet)):
        booly2 = False
        if charLast1 == Alphabet[i]:
            booly2 = True



    if booly2 == False:
        endLine2 = endLine2 - 1



    last1 = line1[indexLast1+1:endLine1]
    print(last1)
    last2 = line2[indexLast2+1:endLine2]
    print(last2)

    if isRhyme('\t'+last1+'\t', '\t'+last2+'\t'):
        print(line1)
        print(line2)
        return True
    else:
        print('rip')
        return False

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

#tweetFourLinePoem(getAPI())
isRhyme('\tbolt\t', '\tsnow\t')
makeTwoLines()

test(False)
def test(x):
    if x == True:
        print('YOU DID IT')
        return True
    else:
        return test(makeTwoLines())






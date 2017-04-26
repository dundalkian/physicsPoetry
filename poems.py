import random
import sys
import os
import markovify
import time

'''
So I am 90% sure that currently it creates/erases a .txt file. It then runs the aptly
named theScript() function which opens that .txt file to append. It then uses somebody else's
space magic to create a markov chain model based on Emily Dickinson poems it then spits out
poems in 10 line groupings every second. 

Why am I doing this I hear you ask? 
    -answer coming with next update.
'''

def theScript():
    testMarkov = open("test.txt", "a")
    #testMarkov.write(bytes("Txt to write\n", 'UTF-8'))

    with open("hellaPoems.txt") as f:
        text = f.read()

    text_model = markovify.NewlineText(text)


    for i in range(10):
        #print(text_model.make_sentence(tries=140) + "\n")
        testMarkov.write((text_model.make_sentence(tries=100) + "\n"))

    testMarkov.write("\n")


    testMarkov.close()

deletePrevious = open("test.txt", "w")
deletePrevious.close()
while True:
    theScript()
    time.sleep(1)










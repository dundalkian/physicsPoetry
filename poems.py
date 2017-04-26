import random
import sys
import os
import markovify

testMarkov = open("test.txt" , "wb")
#testMarkov.write(bytes("Txt to write\n", 'UTF-8'))

with open("hellaPoems.txt") as f:
    text = f.read()

text_model = markovify.NewlineText(text)


for i in range(10):
    #print(text_model.make_sentence(tries=140) + "\n")
    testMarkov.write(bytes(text_model.make_sentence(tries=100) + "\n", 'UTF-8'))


testMarkov.close()










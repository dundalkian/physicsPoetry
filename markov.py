import random
import sys
import os
import markovify
import time
import twitter
import string

with open("hellaPoems.txt") as f:
    corpusText = f.read()

markovModel = markovify.NewlineText(corpusText)

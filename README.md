# physicsPoetry

This is a Twitter bot written using python. It currently can generate poems (or any text) given a corpus 
to work from, I am currently using Emily Dickinson to create my generation model but any text can be used.

When complete, it will allow followers of the bot on twitter to interact with the bot and request poems, 
requesting different rhyming formats (Freeform, AABB, ABAB) is possible and will be implemented soon.

You can look at the past tweets of the bot and watch it as it gets better at https://twitter.com/physicspoetry

The bot functions using a combination of the Twitter API (with Python wrapper https://github.com/bear/python-twitter),
Markovify (https://github.com/jsvine/markovify), and IPhOD 2.0
(The Irvine Phonotactic Online Dictionary - http://www.iphod.com). IPhOD provides a breakdown of the phonemes (the 
individual sounds of the word basically) of over 50,000 english words, (And like, a crap ton of fake words if you
need them) This breakdown allows words to be compared and check for rhymes, among many other cool things.

# The bot works by:

First creating a model of the corpus (currently Emily Dickinson) 

Takes that model and creates two sentences of up to 34 characters. 

Uses a local version of IPhOD to analyze the phonemes of the last word in each sentence, 

If it determines they rhyme, we keep those two lines, if they don't, we discard them. (It isn't very 
efficient I know)

Once it has two sets of lines, it arranges them ABAB style and tweets the corrisponding poem.

It then gets a ton of retweets because I am amazing.

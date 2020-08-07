"""
Program: generator.py
Generates and displays sentences using simple grammar
and vocabulary. Words are chosen at random.
"""

import random


def getWords(filename):
    """Accepts a file name as a parameter and appends the lines of the files of the file opened to words_list
    and returns it as a tuple"""
    words_list = []
    with open(filename) as file:
        for line in file:
            words_list.append(line.strip())
    
    return tuple(words_list)


articles = getWords("articles.txt")
nouns = getWords("nouns.txt")
verbs = getWords("verbs.txt")
prepositions = getWords("prepositions.txt")    
    
def sentence():
    """Builds and returns a sentence."""
    return nounPhrase() + " " + verbPhrase()

def nounPhrase():
    """Builds and returns a noun phrase."""
    return random.choice(articles) + " " + random.choice(nouns)

def verbPhrase():
    """Builds and returns a verb phrase."""
    return random.choice(verbs) + " " + nounPhrase() + " " + prepositionalPhrase()

def prepositionalPhrase():
    """Builds and returns a prepositional phrase."""
    return random.choice(prepositions) + " " + nounPhrase()

def main():
    """Allows the user to input the number of sentences
    to generate."""
    number = int(input("Enter the number of sentences: "))
    for count in range(number):
        print(sentence())
        
main()
"""
Program: generator.py
Author: Anirudh Babu
Student no.: 301105250
Description: Generates and displays sentences using simple grammar
and vocabulary. Words are chosen at random.
"""
import random

# serves as the basis for the random presence/absence of adjectives, conjunctions and independent clauses
numbers = (0,1,0,1,0,1,0,1,0,1,1,1,0,1,1,0,1,0,1,0,1,0)

def getWords(filename):
    """Accepts a file name as a parameter and appends the lines of the file to words_list
         and returns it as a tuple"""
    words_list = []
    with open(filename) as file:
        for line in file:
            # strip() is called so as to get rid of the \n character
            words_list.append(line.strip())
    
    return tuple(words_list)

# assigning tuples containing words to be used obtained by reading files provided
#"articles" = getWords("articles.txt")
articles = getWords("articles.txt")
nouns = getWords("nouns.txt")
verbs = getWords("verbs.txt")
prepositions = getWords("prepositions.txt")
conjunctions = getWords("conjunctions.txt")  
adjectives = getWords("adjectives.txt")

def sentence(clauseCount=0):
    """Builds and returns a sentence."""
    # conjunctionsClause() is called/not called randomly based on the random choice from numbers and
    # the clauseCount variable prevents conjunctionClause from being called in the second independent clause formation
    return nounPhrase() + " " + verbPhrase() + (" " + conjunctionsClause(clauseCount) if random.choice(numbers) == 1 and clauseCount == 0 else "")

def nounPhrase():
    """Builds and returns a noun phrase."""
    
    #Assigning a grammatically correct article for the word succeeding it
    nounSelected = random.choice(nouns)
    adjectivePresent = True if random.choice(numbers) == 1 else False
    adjectiveSelected = random.choice(adjectives) + " " if adjectivePresent else ""
    
    if adjectivePresent:
        #checks if the adjective starts with a vowel to determine an appropriate article
        articleSelected = articles[1] if adjectiveSelected[0] in ['A','E','I','O','U'] else random.choice([articles[0], articles[2]])
    else:
        #checks if the noun starts with a vowel to determine an appropriate article
        articleSelected = articles[1] if nounSelected[0] in ['A','E','I','O','U'] else random.choice([articles[0], articles[2]])
    
    return articleSelected + " " + adjectiveSelected + nounSelected

def verbPhrase():
    """Builds and returns a verb phrase."""
    # prepositionsClause() is called/not called randomly based on the random choice from numbers
    return random.choice(verbs) + " " + nounPhrase() + (" " + prepositionalPhrase() if random.choice(numbers) == 1 else "")

def prepositionalPhrase():
    """Builds and returns a preposition phrase"""
    return random.choice(prepositions) + " " + nounPhrase()

def conjunctionsClause(counter):
    """Builds and returns a conjunction and an independent clause"""
    # the counter variable is responsible for preventing recursion to avoid 
    # long sentences containing multiple independent clauses
    counter += 1
    return random.choice(conjunctions) + " " + sentence(counter)

def main():
    """Allows the user to input the number of sentences
    to generate."""
    number = int(input("Enter the number of sentences: "))
    for count in range(number):
        print(f'{count + 1}){sentence()}\n')
        
main()
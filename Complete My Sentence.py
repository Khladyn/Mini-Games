from wonderwords import RandomSentence
from wonderwords import RandomWord

'''
Your friend was caught sleeping in class and has suddenly been called to recite.
You must help your friend form complete sentences by whispering to his ear.
There are two mode in this game: odd or even. Each mode refers to the indices
of the missing words in a sentence. You will be asked to provide a noun, verb,
adjective, etc. for each turn.

The sentence doesn't have to be grammatically correct. Due to the limitations
of the package used, some valid words may not even be recognized. In such a case,
you can just enter another word and move on... good luck!

'''

# Get a random sentence with a subject, predicate, direct object and adjective
sentence = RandomSentence().sentence().split()

# Placeholder for preposition/pronoun
sentence.insert(4, "my")

mode = input("Play 'odd' or 'even'? ")

valid_verbs = RandomWord().filter(include_parts_of_speech=["verbs"])
valid_nouns = RandomWord().filter(include_parts_of_speech=["nouns"])
valid_adjectives = RandomWord().filter(include_parts_of_speech=["adjectives"])

if mode == "even":

    for i in range(len(sentence)):
        if i == 0:

            word = input("Give me a quantifier: ").capitalize()

        elif i == 2:
            
            word = input("Give me a noun: ")

            while word not in valid_nouns:
                word = input("Give me a valid noun: ")

        elif i == 4:

            word = input("Give me a preposition/pronoun: ")

        else:
            word = sentence[i]
            new_sentence = ' '.join(sentence[:i+1])
            print(new_sentence)

        sentence[i] = word

elif mode == "odd":

    for i in range(len(sentence)):
        if i == 1:

            word = input("Give me an adjective: ")

            while word not in valid_adjectives:
                word = input("Give me a valid adjective: ")

        elif i == 3:
            
            word = input("Give me a verb: ")

            while word not in valid_verbs:
                word = input("Give me a valid verb: ")

        elif i == 5:

            word = input("Give me a noun: ")

            while word not in valid_nouns:
                word = input("Give me a valid noun: ")
            
            sentence[i] = word
            new_sentence = ' '.join(sentence[:i+1])
            print(new_sentence)
            break

        else:
            word = sentence[i]
            new_sentence = ' '.join(sentence[:i+1])
            print(new_sentence)

        sentence[i] = word

print("\nHuh?")
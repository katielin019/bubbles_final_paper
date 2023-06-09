'''
    entro.py calculates the entropy of a given string or file

    This uses the negative sum of the log (to the base of 2) of the probability
    times the probability of a char to occur in a certain string as the entropy.
'''
# Source: https://github.com/creyD/entro.py/blob/ab61e24d67ef2cdb0f50f3a814c5be04a8238d05/entro.py

import math
import argparse


# Calculates the entropy of a given string (as described in the docstring)
def calcEntropy(string):
    alphabet, alphabet_size, entropy = {}, 0, 0

    for char in string:
        if char in alphabet:
            alphabet[char] += 1
        else:
            alphabet[char] = 1
        alphabet_size += 1

    for char in alphabet:
        alphabet[char] = alphabet[char] / alphabet_size
        entropy += alphabet[char] * math.log(alphabet[char], 2)

    return -entropy, alphabet

# Calculates the entropy of a given string and returns only its entropy (as measured in bits)
def getEntropy(string):
    alphabet, alphabet_size, entropy = {}, 0, 0

    for char in string:
        if char in alphabet:
            alphabet[char] += 1
        else:
            alphabet[char] = 1
        alphabet_size += 1

    for char in alphabet:
        alphabet[char] = alphabet[char] / alphabet_size
        entropy += alphabet[char] * math.log(alphabet[char], 2)

    return -entropy

# Outputs a given entropy including the original text and the alphabet with probabilities
def printEntropy(original, entropy, alphabet, simple):
    print('---')
    if simple == False:
        print('Content: ' + original)
        print('Probabilities: ' + str(alphabet))
    print('Entropy: ' + str(entropy) + ' bits')
    print('---')


# Reads a file by a given path
def getFile(path):
    f = open(path, 'r')
    content = f.read().replace('\n', ' ')
    f.close()
    return content.strip()


# List of the arguments one can use to influence the behavior of the program
parser = argparse.ArgumentParser(description='Calculate the information entropy of some strings.')

# INPUT ARGUMENTS
parser.add_argument('strings', nargs='*', default='', type=str, help='Strings to calculate the entropy of.')
parser.add_argument('--files', nargs='*', type=str, default='', help='Provide file path(s) to calculate the entropy of.')

# OUTPUT OPTIONS
parser.add_argument('--simple', nargs='?', type=bool, default=False, help='Determines the explicitness of the output. (True = only entropy shown)')

# CONVERT OPTIONS
parser.add_argument('--lower', nargs='?', type=bool, default=False, help='Converts given strings or textfiles to lowercase before calculating.')
parser.add_argument('--upper', nargs='?', type=bool, default=False, help='Converts given strings or textfiles to uppercase before calculating.')
parser.add_argument('--squash', nargs='?', type=bool, default=False, help='Removes all whitespaces before calculating.')
args, unknown = parser.parse_known_args()

# Prepares the queue of different strings
queue = []

# Add all the provided strings to the list
for string in args.strings:
    queue.append(string)

# Add all the provided files to the list
for file in args.files:
    string = getFile(file)
    queue.append(string)

# Interates over the collected strings and prints the entropies
for string in queue:
    if args.lower != False:
        string = string.lower()
    elif args.upper != False:
        string = string.upper()

    if args.squash != False:
        string = string.replace(" ", "")

    a, b = calcEntropy(string)
    printEntropy(string, a, b, args.simple)

# Calculating the conditional entropy of a text
# Source: http://datasciencepadawan.blogspot.com/2015/03/computing-text-conditional-entropy-with.html?m=1

def ngram_list(text, n):
    ngram = []
    count = 0
    for token in text[:len(text)-n+1]:
        ngram.append(text[count:count+n])
        count = count + 1
    return ngram

def ngram_counts(text, n):
    ngram_dict = {}
    ngram_arr = ngram_list(text, n)

    for item in ngram_arr:
        ngram_dict[' '.join(item)] = (ngram_dict[' '.join(item)] + 1) if ' '.join(item) in ngram_dict else 1
    return ngram_dict

def conditional_entropy(data):
    unigram = ngram_counts(data, 1)
    bigram = ngram_counts(data, 2)
    N = sum(unigram.values())
    H = 0

    for key in bigram.keys():
        H -= bigram[key] / (1.0 * N) * math.log(bigram[key] / (1.0 * unigram[key.split(' ')[1]]), 2)
    return H

def experimental_entropy(data):
    unigram = ngram_counts(data, 2)
    bigram = ngram_counts(data, 3)
    N = sum(unigram.values())
    H = 0

    for key in bigram.keys():
        H -= bigram[key] / (1.0 * N) * math.log(bigram[key] / (1.0 * unigram[key.split(' ')[1]]), 2)
    return H

def test():
    print("pls work")
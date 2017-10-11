import random
import time

references = " .,!?0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
attempted_word = ""

# Kata yang akan di Brute Force
data = "I Am a Student In STMIK Bumigora, And I Loive It"

# File want to brute force
files = open('word.txt','r').read()
word =""
for a in files:
    word += a

# Checking the time of brute force
def timeit(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print "|| Time to find the word in {.__name__} took : {:.15f} seconds to finish.\n".format(func, time.time() - start)
        return result
    return wrapper


@timeit
def solve_word(word):
    global attempted_word
    for character in word:
        for entry in references:
            if character == entry:
                attempted_word += character
                continue
    return attempted_word
print ""
print "||======================== Brute Force Algoritma ========================================================================================"
print "|| Created by : Darmawan Zulkifli                                               "
print "|| Licence    : Before you updateting this script, confirm to me please !!      "
print "||_______________________________________________________________________________________________________________________________________"
print "||                                                                              "
print "||                                                                              "
print "|| The word is: {0:}\n\n|| Brute Foce: {1:}\n\n|| Length of Data was: {2:}\n\n|| Is correct? : {3:}".format(solve_word(word),
                                                                                 attempted_word,
                                                                                 len(word),
                                                                                 attempted_word in word)
print "||                                                                              "
print "||=========================**********************========================================================================================"

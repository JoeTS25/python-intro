def print_upper_words(words)
""" Print each word uppercase
"""
    for word in words:
        print(word.upper())

def print_upper_words2(words)
""" Print words that start with 'e' or E """
    for word in words:
        if word.startswith("e") or word.startswith("E"):
            print(word.upper())

def print_upper_words3(words, starts)
""" Be able to pass in a set of letters and only print out words that
    start with one of those letters """
    for word in words:
        for char in starts:
            if word.starts(char):
                print(word.upper())
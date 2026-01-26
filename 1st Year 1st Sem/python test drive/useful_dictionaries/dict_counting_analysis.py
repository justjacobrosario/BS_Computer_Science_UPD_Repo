"""
2.1 Counting Occurrences — Problem: count_frequency
Problem Statement
 Given a sequence of integers, count how many times each value appears.

Example Calls
 count_frequency((1,2,2,3,1,2)) → {1:2, 2:3, 3:1}
 count_frequency(()) → {}
 """

def count_frequency(seq):
    dic = {}
    for item in seq:
        if item in dic:
            dic[item] += 1
        else:
            dic.update({item : 1})
    return dic

print("item freq", count_frequency((1,2,2,3,1,2)))

"""
2.2 Letter Counting — Problem: count_letters
Problem Statement
 Count frequency of each alphabetic character (case-insensitive) in a given string.

Example Calls
 count_letters("Hello") → {'h':1,'e':1,'l':2,'o':1}
 count_letters("") → {}
 """

def count_letters(strng):
    dic = {}
    for letter in strng:
        letter = letter.lower()
        if letter in dic:
            dic[letter] += 1
        else:
            dic.update({letter : 1})
    return dic

print("letter freq:", count_letters("Hello"))

"""
2.3 Word Counting — Problem: word_frequency
Problem Statement
 Given a string with words separated by spaces, count occurrences of each word.

Example Calls
 word_frequency("the cat and the dog") → {'the':2, 'cat':1, 'and':1, 'dog':1}
"""

def word_frequency(phrase):
    dic = {}
    words = phrase.split(" ")
    for word in words:
        word = word.lower()
        if word in dic:
            dic[word] += 1
        else:
            dic.update({word : 1})
    return dic

print("word freq:", word_frequency("the cat and the dog"))

"""
2.4 Counting by Property — Problem: count_by_parity
Problem Statement
 Count how many even and odd numbers appear in a list.

Example Calls
 count_by_parity((1,2,3,4,5)) → {'even':2, 'odd':3}
"""

def count_by_parity(seq):
    dic = {
    "even" : 0,
    "odd" : 0
    }
    for num in seq:
        if num % 2 == 0:
            dic["even"] += 1
        elif num % 2 != 0:
            dic["odd"] += 1
    return dic

print("parity freq:", count_by_parity((1,2,3,4,5)))
from collections import Counter
import operator

def read_file(path):
    file = open(path, 'r')
    for line in file:
        print line

def find_most_frequent_word(path):
    file = open(path, 'r')
    word_counter = {}
    for line in file:
        for word in line.split(" "):
            if word in word_counter:
                word_counter[word] += 1
            else:
                word_counter[word] = 1
    print sorted(word_counter.iteritems(),key=operator.itemgetter(1), reverse= True)
find_most_frequent_word('HR Interview Material.txt')
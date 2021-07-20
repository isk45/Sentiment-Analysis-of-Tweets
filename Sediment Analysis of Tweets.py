# -*- coding: utf-8 -*-
"""Welcome To Colaboratory

def strip_punctuation(a):
    for x in punctuation_chars:
        if x in a:
            a = a.replace(x,"")
    return(a)

def get_pos(a):
    pos = 0
    a = a.lower()
    a = strip_punctuation(a)
    lst = a.split(" ")
    for i in positive_words:
        if i in lst: 
            pos+=1
    return pos

def get_neg(a):
    neg = 0
    a = a.lower()
    a = strip_punctuation(a)
    lst = a.split(" ")
    for i in negative_words:
         if i in lst: 
            neg+=1
    return neg

punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
# lists of words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())

negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())

outfile = open("resulting_data.csv", "w")
outfile.write('Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score')
outfile.write('\n')

infile = open("project_twitter_data.csv", "r")
print(infile.readline())
neg = []
pos = []
net = []
retweets = []
replies = []
for line in infile:
    lis = line.strip().split(',')
    pos.append(get_pos(lis[0]))
    neg.append(get_neg(lis[0]))
    retweets.append(lis[1])
    replies.append(lis[1])
    
for i in range(len(pos)):
    t = pos[i]-neg[i]
    net.append(t)
infile.close()

for i in range(len(pos)):
    outfile.write('{},{},{},{},{}\n'.format(retweets[i],replies[i],pos[i],neg[i],net[i]))
outfile.close()


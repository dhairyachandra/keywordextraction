# coding=utf-8
import collections

#Input from a text file
file = open('input.txt') 
a= file.read()

#Stopwords
stopwords = set(line.strip() for line in open('stopwords.txt'))
stopwords = stopwords.union(set(['mr','mrs','one','two','said']))
wordcount = {}

for word in a.lower().split():
    word = word.replace(".","")
    word = word.replace(",","")
    word = word.replace(":","")
    word = word.replace("!","")
    word = word.replace("?","")
    word = word.replace("\"","")
    word = word.replace("!","")
    word = word.replace("â€œ","")
    word = word.replace("â€˜","")
    word = word.replace("*","")
    if word not in stopwords:
        if word not in wordcount:
            wordcount[word] = 1
        else:
            wordcount[word] += 1
            
# Print most common word
n_print = int(4) #Change int(n) for number of keywords
string=""
word_counter = collections.Counter(wordcount)
for word, count in word_counter.most_common(n_print):
    string=string+","+word

# Close the file
file.close()

l = []
for word in word_counter.most_common(n_print):
    l.append(word[:1])

#Print final string
print(string)

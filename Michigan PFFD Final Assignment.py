import matplotlib.pyplot as plt
import csv
projectTwitterData = open("project_twitter_data.csv", "r")
resultingData = open("resulting_data.csv", "w")

punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
string = "#in.cred..ible!"
def strip_punctuation(word):
    for character in punctuation_chars:
        for letter in word:
            if character == letter:
                word = word.replace(character, "")
    return word

positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())

def get_pos(astring):
    pos_num = 0
    astring = strip_punctuation(astring.lower()).split(" ")
    for word in astring:
        if word in positive_words:
            pos_num += 1
    return pos_num

negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())

def get_neg(astring):
    neg_num = 0
    astring = strip_punctuation(astring.lower()).split(" ")
    for word in astring:
        if word in negative_words:
            neg_num += 1
    return neg_num

with open("project_twitter_data.csv") as proj_t:
    line = []
    for lin in proj_t:
        line.append(lin.strip())


def analyse_data(resultingData):
    resultingData.write("Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score")
    resultingData.write("\n")

    dataLine = projectTwitterData.readlines()
    dataLine.pop(0)
    for line in dataLine:
        line = line.strip().split(',')
        resultingData.write("{}, {}, {}, {}, {}".format(line[1], line[2], get_pos(line[0]), get_neg(line[0]),
                                                        (get_pos(line[0]) - get_neg(line[0]))))
        resultingData.write("\n")

analyse_data(resultingData)
projectTwitterData.close()
resultingData.close()

x=[]
y=[]

with open('resulting_data.csv', 'r') as csvfile:
    header = next(csvfile)
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        x.append(int(row[4]))
        y.append(int(row[0]))

plt.scatter(x, y, marker='o')
plt.title('Project - Part 2: Sentiment Analysis')
plt.xlabel('Net Score')
plt.ylabel('Number of Retweets')
plt.grid()
plt.show()
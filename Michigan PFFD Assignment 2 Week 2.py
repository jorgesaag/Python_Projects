#The dictionary Junior shows a schedule for a junior year semester.
#The key is the course name and the value is the number of credits.
#Find the total number of credits taken this semester and assign it to the variable credits.
#Do not hardcode this – use dictionary accumulation!

Junior = {'SI 206':4, 'SI 310':4, 'BL 300':3, 'TO 313':3, 'BCOM 350':1, 'MO 300':3}
credits = 0
for value in Junior.values():
    credits += value
print(credits)

#Create a dictionary, freq, that displays each character in string str1 as the key and its frequency as the value.

str1 = "peter piper picked a peck of pickled peppers"
freq = {}
for i in str1:
    if i not in freq:
        freq[i] = 0
    freq[i] = freq[i] + 1
print(freq)

#OR

from collections import Counter

str1 = "peter piper picked a peck of pickled peppers"
freq = Counter(str1)
for i in str1:
    print(i, freq[i])

#Provided is a string saved to the variable name s1.
#Create a dictionary named counts that contains each letter in s1 and the number of times it occurs.

s1 = "hello"
counts = {}
for i in s1:
    if i not in counts:
        counts[i] = 0
    counts[i] = counts[i] + 1
print(counts)

#OR

s1 = "hello"
def char_frequency(s1):
    dict = {}
    for n in s1:
        keys = dict.keys()
        if n in keys:
            dict[n] += 1
        else:
            dict[n] = 1
    return dict
counts = char_frequency(s1)
print(counts)

#Create a dictionary, freq_words, that contains each word in string str1 as the key and its frequency as the value.

str1 = "I wish I wish with all my heart to fly with dragons in a land apart"
str2 = str1.split()
freq_words = {}
for i in str2:
    if i not in freq_words:
        freq_words[i] = 0
    freq_words[i] = freq_words[i] + 1
print(freq_words)

#OR

def word_count(str):
    counts = dict()
    words = str.split()
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts
freq_words = word_count(str1)
print(freq_words)

#Create a dictionary called wrd_d from the string sent,
#so that the key is a word and the value is how many times you have seen that word.

sent = "Singing in the rain and playing in the rain are two entirely different situations but both can be good"
sent2 = sent.split()
wrd_d = {}
for i in sent2:
    if i not in wrd_d:
        wrd_d[i] = 0
    wrd_d[i] = wrd_d[i] + 1
print(wrd_d)

#Create the dictionary characters that shows each character from the string sally and its frequency.
#Then, find the most frequent letter based on the dictionary. Assign this letter to the variable best_char.

sally = "sally sells sea shells by the sea shore"
characters = {}
for i in sally:
    if i not in characters:
        characters[i] = 0
    characters[i] = characters[i] + 1
print(characters)
keys = list(characters.keys())
best_char = keys[0]
for key in keys:
    if characters[key] > characters[best_char]:
        best_char = key
print(best_char)

#OR

sally = "sally sells sea shells by the sea shore"
characters = {}
for i in sally:
    characters[i] = characters.get(i, 0) + 1
sorted(characters.items(), key=lambda x: x[1])
best_char = sorted(characters.items(), key=lambda x: x[1])[-1][0]

#Find the least frequent letter. Create the dictionary characters that shows each character from string sally
#and its frequency. Then, find the least frequent letter in the string and assign the letter to the variable worst_char.

sally = "sally sells sea shells by the sea shore and by the road"
characters = {}
for i in sally:
    if i not in characters:
        characters[i] = 0
    characters[i] = characters[i] + 1
print(characters)
keys = list(characters.keys())
worst_char = keys[0]
for key in keys:
    if characters[key] < characters[worst_char]:
        worst_char = key
print(worst_char)

#OR

sally = "sally sells sea shells by the sea shore and by the road"
characters = {}
for i in sally:
    characters[i] = characters.get(i, 0) + 1
sorted(characters.items(), key=lambda x: x[1])
worst_char = sorted(characters.items(), key=lambda x: x[1])[-13][0]

#Create a dictionary named letter_counts that contains each letter and the number of times it occurs in string1.
#Challenge: Letters should not be counted separately as upper-case and lower-case.
#Instead, all of them should be counted as lower-case.

string1 = "There is a tide in the affairs of men, Which taken at the flood, leads on to fortune. Omitted, all the voyage of their life is bound in shallows and in miseries. On such a full sea are we now afloat. And we must take the current when it serves, or lose our ventures."
letter_counts = {}
for i in string1:
    i = i.lower()
    letter_counts[i] = letter_counts.get(i, 0) + 1
print(letter_counts)

#Create a dictionary called low_d that keeps track of all the characters in the string p and notes
#how many times each character was seen. Make sure that there are no repeats of characters as keys,
#such that “T” and “t” are both seen as a “t” for example.

p = "Summer is a great time to go outside. You have to be careful of the sun though because of the heat."
low_d = {}
for i in p:
    i = i.lower()
    low_d[i] = low_d.get(i, 0) + 1
print(low_d)
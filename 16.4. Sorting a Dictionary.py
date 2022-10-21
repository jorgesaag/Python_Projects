#Previously, you have used a dictionary to accumulate counts, such as the frequencies of letters or words in a text.
#For example, the following code counts the frequencies of different numbers in the list.

L = ['E', 'F', 'B', 'A', 'D', 'I', 'I', 'C', 'B', 'A', 'D', 'D', 'E', 'D']

d = {}
for x in L:
    if x in d:
        d[x] = d[x] + 1
    else:
        d[x] = 1
for x in d.keys():
    print("{} appears {} times".format(x, d[x]))

#The dictionary’s keys are not sorted in any particular order.
#In fact, you may get a different order of output than someone else running the same code.
#We can force the results to be displayed in some fixed ordering, by sorting the keys.

L = ['E', 'F', 'B', 'A', 'D', 'I', 'I', 'C', 'B', 'A', 'D', 'D', 'E', 'D']

d = {}
for x in L:
    if x in d:
        d[x] = d[x] + 1
    else:
        d[x] = 1
y = sorted(d.keys())
for k in y:
    print("{} appears {} times".format(k, d[k]))

#With a dictionary that’s maintaining counts or some other kind of score, we might prefer to get the outputs sorted
#based on the count rather than based on the items. The standard way to do that in python is to sort based on a
#property of the key, in particular its value in the dictionary.
#Here things get a little confusing because we have two different meaning of the word “key”.
#One meaning is a key in a dictionary. The other meaning is the parameter name for the function
#that you pass into the sorted function.
#Remember that the key function always takes as input one item from the sequence and
#returns a property of the item. In our case, the items to be sorted are the dictionary’s keys,
#so each item is one key from the dictionary. To remind ourselves of that, we’ve named the parameter
#in tha lambda expression k. The property of key k that is supposed to be returned is its associated value
#in the dictionary. Hence, we have the lambda expression lambda k: d[k].

L = ['E', 'F', 'B', 'A', 'D', 'I', 'I', 'C', 'B', 'A', 'D', 'D', 'E', 'D']

d = {}
for x in L:
    if x in d:
        d[x] = d[x] + 1
    else:
        d[x] = 1

y = sorted(d.keys(), key=lambda k: d[k], reverse=True)
for k in y:
    print("{} appears {} times".format(k, d[k]))

#Here’s a version of that using a named function.

L = ['E', 'F', 'B', 'A', 'D', 'I', 'I', 'C', 'B', 'A', 'D', 'D', 'E', 'D']

d = {}
for x in L:
    if x in d:
        d[x] = d[x] + 1
    else:
        d[x] = 1

def g(k):
    return d[k]

y =(sorted(d.keys(), key=g, reverse=True))

# now loop through the keys
for k in y:
    print("{} appears {} times".format(k, d[k]))

#When we sort the keys, passing a function with key=lambda x: d[x] does not specify to sort the keys of a dictionary.
#The lists of keys are passed as the first parameter value in the invocation of sort.
#The key parameter provides a function that says how to sort them.
#An experienced programmer would probably not even separate out the sorting step.
#And they might take advantage of the fact that when you pass a dictionary to something that is expecting a list,
#its the same as passing the list of keys.

L = ['E', 'F', 'B', 'A', 'D', 'I', 'I', 'C', 'B', 'A', 'D', 'D', 'E', 'D']

d = {}
for x in L:
    if x in d:
        d[x] = d[x] + 1
    else:
        d[x] = 1

# now loop through the sorted keys
for k in sorted(d, key=lambda k: d[k], reverse=True):
      print("{} appears {} times".format(k, d[k]))

#Eventually, you will be able to read code like that and immediately know what it’s doing.
#For now, when you come across something confusing, like line 11, try breaking it down.
#The function sorted is invoked. Its first parameter value is a dictionary,
#which really means the keys of the dictionary.
#The second parameter, the key function, decorates the dictionary key with a post-it note containing that
#key’s value in dictionary d. The last parameter, True, says to sort in reverse order.
#There is another way to sort dictionaries, by calling .items() to extract a sequence of (key, value) tuples,
#and then sorting that sequence of tuples. But it’s better to learn the pythonic way of doing it,
#sorting the dictionary keys using a key function that takes one key as input and looks up the value in the dictionary.
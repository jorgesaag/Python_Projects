#When constructing your own nested data, it is a good idea to keep the structure consistent across each level.
#For example, if you have a list of dictionaries, then each dictionary should have the same structure, meaning
#the same keys and the same type of value associated with a particular key in all the dictionaries.
#The reason for this is because any deviation in the structure that is used will require extra code to handle
#those special cases. The more the structure deviates, the more you will have to use special cases.
#For example, let’s reconsider this nested iteration, but suppose not all the items in the outer list are lists.

nested1 = [1, 2, ['a', 'b', 'c'],['d', 'e'],['f', 'g', 'h']]
for x in nested1:
    print("level1: ")
    for y in x:
        print("     level2: {}".format(y))

#Now the nested iteration fails. We can solve this with special casing, a conditional that checks the type.
#You can imagine how many special case if-thens we’d need, and how complicated the code would get,
#if we had many layers of nesting but not always a consistent structure.

nested1 = [1, 2, ['a', 'b', 'c'],['d', 'e'],['f', 'g', 'h']]
for x in nested1:
    print("level1: ")
    if type(x) is list:
        for y in x:
            print("     level2: {}".format(y))
    else:
        print(x)


#When you have nested data structures, especially lists and/or dictionaries,
#you will frequently need nested for loops to traverse them.

nested1 = [['a', 'b', 'c'],['d', 'e'],['f', 'g', 'h']]
for x in nested1:
    print("level1: ")
    for y in x:
        print("     level2: " + y)

#Line 3 executes once for each top-level list, three times in all. With each sub-list, line 5 executes once for each
#item in the sub-list. Try stepping through it in Codelens to make sure you understand what the nested iteration does.
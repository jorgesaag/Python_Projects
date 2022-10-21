#Python provides an alternative way to do map and filter operations, called a list comprehension.
#Many programmers find them easier to understand and write. List comprehensions are concise ways to create lists
#from other lists. The general syntax is:

# [<transformer_expression> for <loop_var> in <sequence> if <filtration_expression>]

#where the if clause is optional. For example:

things = [2, 5, 9]

yourlist = [value * 2 for value in things]

print(yourlist)

#The transformer expression is value * 2. The item variable is value and the sequence is things.
#This is an alternative way to perform a mapping operation. As with map, each item in the sequence is transformed
#into an item in the new list. Instead of the iteration happening automatically, however, we have adopted the syntax
#of the for loop which may make it easier to understand.

#Just as in a regular for loop, the part of the statement for value in things says to execute some code once for
#each item in things. Each time that code is executed, value is bound to one item from things.
#The code that is executed each time is the transformer expression, value * 2, rather than a block of code
#indented underneath the for statement. The other difference from a regular for loop is that each time the expression
#is evaluated, the resulting value is appended to a list.
#That happens automatically, without the programmer explicitly initializing an empty list or appending each item.

#The if clause of a list comprehension can be used to do a filter operation.
#To perform a pure filter operation, the expression can be simply the variable that is bound to each item.
#For example, the following list comprehension will keep only the even numbers from the original list.

def keep_evens(nums):
    new_list = [num for num in nums if num % 2 == 0]
    return new_list

print(keep_evens([3, 4, 6, 7, 0, 1]))

#You can also combine map and filter operations by chaining them together, or with a single list comprehension.

things = [3, 4, 6, 7, 0, 1]
#chaining together filter and map:
# first, filter to keep only the even numbers
# double each of them
print(map(lambda x: x*2, filter(lambda y: y % 2 == 0, things)))

# equivalent version using list comprehension
print([x*2 for x in things if x % 2 == 0])


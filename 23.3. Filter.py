#Now consider another common pattern: going through a list and keeping only those items that meet certain criteria.
#This is called a filter.

def keep_evens(nums):
    new_list = []
    for num in nums:
        if num % 2 == 0:
            new_list.append(num)
    return new_list

print(keep_evens([3, 4, 6, 7, 0, 1]))

#Again, this pattern of computation is so common that Python offers a more compact and general way to do it,
#the filter function. filter takes two arguments, a function and a sequence.
#The function takes one item and return True if the item should.
#It is automatically called for each item in the sequence.
#You don’t have to initialize an accumulator or iterate with a for loop.

def keep_evens(nums):
    new_seq = filter(lambda num: num % 2 == 0, nums)
    return list(new_seq)

print(keep_evens([3, 4, 6, 7, 0, 1]))


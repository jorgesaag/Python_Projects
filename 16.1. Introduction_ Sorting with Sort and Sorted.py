#When we first introduced lists, we noted the existence of a method sort. When invoked on a list,
#the order of items in the list is changed. If no optional parameters are specified, the items are arranged
#in whatever the natural ordering is for the item type. For example, if the items are all integers,
#then smaller numbers go earlier in the list. If the items are all strings, they are arranged in alphabetic order.

L1 = [1, 7, 4, -2, 3]
L2 = ["Cherry", "Apple", "Blueberry"]

L1.sort()
print(L1)
L2.sort()
print(L2)

#Note that the sort method does not return a sorted version of the list. In fact, it returns the value None.
#But the list itself has been modified. This kind of operation that works by having a side effect on the list can
#be quite confusing. In this course, we will generally use an alternative way of sorting, the function sorted rather
#than the method sort. Because it is a function rather than a method, it is invoked on a list by passing the
#list as a parameter inside the parentheses, rather than putting the list before the period. More importantly,
#sorted does not change the original list. Instead, it returns a new list.

L2 = ["Cherry", "Apple", "Blueberry"]

L3 = sorted(L2)
print(L3)
print(sorted(L2))
print(L2) # unchanged

print("----")

L2.sort()
print(L2)
print(L2.sort())  #return value is None


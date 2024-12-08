#Create a set from a list and remove duplicates.
a=[1,2,2,3,4,5,8,8,9,9,9,9,10]
b=set(a)
print(b)

#Write a Python program to find the union of two sets {1, 2, 3} and {3, 4, 5}.

a={1, 2, 3}
b={3, 4, 5}

print(a.union(b))

#Find the intersection of two sets {1, 2, 3} and {2, 3, 4}.

a={1,2,3}
b={2,3,4}
print(a.intersection(b))

#Check if {1, 2} is a subset of {1, 2, 3, 4}.

a={1,2}
b={1,2,3,4}
print(a.issubset((b)))

#Remove an element from a set and handle the case if the element is not found.
my_set = {1, 2, 3, 4}
my_set.discard(5)
print(my_set)
#my_set.discard(5)
#print(my_set)


#Find the difference between two sets {1, 2, 3} and {2, 3, 4}.
a={1,2,3}
b={2,3,4}
print(a.difference(b))

#Write a Python program to add multiple elements to a set.

a={1,2,3,4}
a.update((6,7))
print(a)

#Create a frozen set and demonstrate how it differs from a regular set.

#fruits = {"Apple", "Banana", "Cherry", "Apple", "Kiwi"}
#fset = frozenset(fruits)

#print(fset)
#fset.add("Orange")
#print(fset)
#shows error cause we cannot add the attributes to a frozen set
fruits = {"Apple", "Banana", "Cherry", "Apple", "Kiwi"}

print(fruits)
fruits.add("Orange")
print(fruits)

#Write a program to find elements that are in either of two sets but not in both (symmetric difference).

a={"chintu","reddy","moulya","reddy"}
b={"Cherry","banana","reddy","apple"}
c=a.symmetric_difference(b)
print(c)

#Check if a set is empty.

a = {}
if len(a) == 0:
    print("Empty")
else:
    print("Not Empty")

a = {}
if a == {}:
    print("Empty")
else:
    print("Not Empty")







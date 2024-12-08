#Create a tuple containing numbers from 1 to 10 and access the 5th element.

a=(1,2,3,4,5,6,7,8,9)
print(type(a))
print(a[4])

#Write a Python program to check if an element exists in a tuple.

a = (2,4,5,3,6,8,9)
b=8
c = [i for i in a if i == b]
print(["Element exists" if c else "Element does not exists"])

#Convert a list [1, 2, 3, 4, 5] into a tuple.

a=[1,2,3,4,5]
b=tuple(a)
print(type(b))
print(b)

#Find the length of the tuple (10, 20, 30, 40, 50).

a=(10, 20, 30, 40, 50)
b=len(a)
print(b)

#Write a Python program to count the occurrences of the element 2 in the tuple (1, 2, 3, 2, 4, 2).

a=(1, 2, 3, 2, 4, 2)
print(a.count(2))

#Unpack the tuple (100, 200, 300) into three variables and print them.

mytuple=(100, 200, 300)
a, b, c=mytuple
print(a)
print(b)
print(c)

#Write a Python program to concatenate two tuples (1, 2, 3) and (4, 5, 6).

a=(1,2,3)
b=(4,5,6)
c=a+b
print(c)

#Convert the string "Python" into a tuple of characters.

a="Python"
b=tuple(a)
print(b)

#Write a Python program to find the index of the first occurrence of 5 in the tuple (1, 3, 5, 7, 5, 9).

a=(1, 3, 5, 7, 5, 9)
b=a.index(5)
print(b)

#Explain why tuples are immutable and how this property can be useful in programming.



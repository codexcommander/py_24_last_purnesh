#Write a Python program to find the largest and smallest numbers in a list.
from os import remove

#a=[12,3,4,27,89,1,34,23,42]
#print(max(a))
#print(min(a))
#b=a[0]
#c=a[0]
#for i in a:
#    if i>b:
#        b=i
#    if i<c:
#        c=i
#print(c)
#Remove duplicates from the list [1, 2, 2, 3, 4, 4, 5].

#a=[1, 2, 2, 2, 3, 4, 4, 5]
#b=set(a)
#print(b)
#b=a[0]
#count=0
#for i in a:
#    if a.count(i)>1:
#        a.remove(i)
#print(a)

#Sort a list of strings alphabetically.

#a=['a', 'c', 'b']
#a.sort()
#print(a)

#Rotate the list [1, 2, 3, 4, 5] one position to the right.

#li=[1, 2, 3, 4, 5]
#lis=li[-1:]+li[:-1]
#print(str(lis))

#Merge two lists [1, 2, 3] and [4, 5, 6] without duplicates.
#l1=[1,2,3]
#l2=[4,5,5,6]
#a=set(l1)
#b=set(l2)
#c=list(a.union(b))
#print(c)

#Find the second largest number in the list [10, 20, 4, 45, 99].

#li=[10, 20, 4, 45, 99]
#li.sort()
#b=li[-2]
#print(b)

#Flatten a nested list [[1, 2], [3, 4], [5]]

#lis=[[1, 2], [3, 4], [5]]

#flat_list=[a for b in lis for a in b]
#print(flat_list)

#Write a Python program to count occurrences of an element in a list.

#li=[1,2,2,3,4,5,5,6,6,6,7]
#print(li.count(6))

#Find the intersection of two lists [1, 2, 3] and [2, 3, 4].

#a=[1,2,3]
#b=[2,3,4]
#c=set(a).intersection(b)
#print(c)

#def intersection(a,b):
#    return set(a).intersection(b)

#print(intersection(a,b))

#Write a Python program to remove all elements from a list that are divisible by 3.

#li=[3,4,5,6,7,8,9,10]
#new_li=[item for item in li if item % 3 != 0]
#print(new_li)

















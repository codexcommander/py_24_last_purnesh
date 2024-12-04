#Write a Python program to count the number of vowels in a given string.
a=input()
v="aeiouAEIOU"
c=0
for i in a:
    if i in v:
        c=c+1
print(c)

#Reverse the string "Python is fun!" without using slicing.
a="Python is fun!"
b=a.split()
c=""
for i in a:
    c=c+i
    if c in ("apple","banana","cherry"):
        if c == "cherry":
            print(c)
            break
        print(c, end=",")
        c=""
        print(c)
for i in b:
    c=i+" "+c
print(c)

#Check if the string "madam" is a palindrome.
a="madam"
b=a[::-1]
if a==b:
    print("Palindrome")
else:
    print("not Palindrome")

#Find and replace the word "Python" with "Programming" in the string "I love Python."
a="I love Python"
b=a.replace("Python","Programming")
print(b)

#Convert the string "hello world" to the title case.

a="hello world"
b=a.title()
print(b)

#Extract all the digits from the string "abc123xyz456".

a="abc123xyz456"

import math

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

n = 11
print(is_prime(n))




















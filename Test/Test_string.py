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
for i in a:
    if i.isdigit():
        print(i, end="")
print()
#Join a list of strings ["Python", "is", "awesome"] into a single string separated by spaces.

a=["Python", "is", "awesome"]
#a="".join(a)
#print(a)
c=""
for i in a:
    c=c+" "+i
print(c[1:])

#Write a Python program to check if a given string starts with "Hello".

a=input()
#b=a.startswith("Hello")
#if b:
#    print("True")
#else:
#   print("false")

a=a.split()
if a[0]=="Hello":
    print("true")
else:
    print("false")

#Count the occurrence of each character in the string "hello".

a="hello"
#for i in a:
#    b=a.count(i)
#    print(b, end=" ")

c=0
b=len(a)
for i in a:
    for j in range(b):
        if i==a[j]:
            c+=1
    print(c)
    c=0

#Split the string "apple, banana, cherry" by commas.
print("apple","banana","cherry",sep=",")










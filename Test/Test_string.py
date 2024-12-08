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
#digits=[]

#for char in a:
#    if char.isdigit():
#        digits.append(char)
#print(digits)

digits = [char for char in a if char.isdigit()]
print(digits)

#Join a list of strings ["Python", "is", "awesome"] into a single string separated by spaces.
a=["Python", "is", "awesome"]
b=" ".join(a)
print(b)

#Write a Python program to check if a given string starts with "Hello".

a = input()
if a.startswith("Hello"):
    print("The string starts with 'Hello'.")
else:
    print("The string does not start with 'Hello'.")


#Count the occurrence of each character in the string "hello".
a = "hello"
count={}
for char in a:
    if char in count:
        count[char] += 1
    else:
        count[char] = 1
print(count)

#Split the string "apple, banana, cherry" by commas.
a = "apple, banana, cherry"
b = a.split(", ")
print(b)
























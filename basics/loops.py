<<<<<<< HEAD
#Program to read N numbers and print 10 numbers after N numbers
a=int(input())
c=1
while c<=10:
    a=a+1
    print(a)
    c=c+1

#write a program to read N numbers and print average of N numbers from 1

b=int(input())
s=0
d=0
while d<b:
    d=d+1
    s=s+d
print(s/b)

#write a program that takes two integers M and N, and prints a solid rectangle pattern of M rows and N columns using the asterisk character (*)
a=int(input())
b=int(input())
c=1
while c<=a:
    print("* "*b)
    c=c+1

#for loops

#write a program that reads a string and prints the first character (The character at index 0) of the given string on N lines, where N is the length of the given string
a = input()
b = len(a)
for i in range(b):
    print(a[0])

#write a program which reads N inputs and prints the sum of the given input integers
n = int(input())
s = 0
for i in range(n):
    b = int(input())
    s = s + b
print(s)

#Given two integers M and N, write a program to print the sum of the numbers from M to N.
m = int(input())
n = int(input())
s = 0
for i in range(m,n+1):
    s = s + i
print(s)

#Write a program that reads a number N and prints two Right Angled Triangles of N rows, using numbers starting from 1.

n = int(input())
for i in range(1, n+1):
        print(str(i)*i)
for j in range(1, n+1):
            print(str(j)*j),

#Write a program that reads a number N and prints a Pyramid of N rows,
n = int(input())

for i in range(1,n+1):
    row =" "*(2*(n-i))+"* " * i + "* " * (i-1)
    print(row)






=======
a= 10
b= 10
c= [1,2,3]
d= [1,2,3]
print(a == b)
print(c == d)
print(a is b)
print(c is d)
>>>>>>> 1d4c10f8fa6ae2d0598c148b1670823696cb0802

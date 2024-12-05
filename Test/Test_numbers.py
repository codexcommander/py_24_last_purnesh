#Write a program to check if a given number is prime.

#def is_prime(n):
#   if n<2:
#      return "Not a Prime number"
#   i=2
#   while i*i<=n:
#   if n%i==0:
#         return "Not a Prime number"
#          i += 1
#   return "Prime number"
#print(is_prime(13))

#n=int(input())
#if n<2:
#   print("Not a Prime number")
#for i in range (2,n):
#   if n%i==0:
#       print("Not a Prime number")
#       break
#  else:
#        print("Prime number")

#def is_prime(n):
#    if n<=1:
#        return False
#    for i in range(2,n):
#        if n%i==0:
#            return False
#    return True
#def prime_nums(n):
#    prime_li=[]
#    for num in range(2,n+1):
#        if is_prime(n):
#            prime_li.append(num)
#        return prime_li


def is_prime(n):
    if n<2:
        return False
    i=2
    while i<=n:
        if n%i==0 and i !=n:
            return False
        i+=1
    return True
print(is_prime(13))
#def prime_nums(n):
#    prime_li=[]
#    for num in range(2,n+1):
#        if is_prime(num):
#            prime_li.append(num)
#    return prime_li
#n = int(input())
#print(prime_nums(n))

#def is_prime(n):
#    prime_li=[]
#    for i in range(1,n+1):
#        for j in range(1,i+1):
#            if i%j==0 and j != i and j != 1:
#                c +=1
#        if c == 0 and i != 1:
#            prime_li.append(i)
#    return prime_li
#n = int(input())
#res = is_prime(n)
#print(res)

#Find the greatest common divisor (GCD) of two numbers.
#def gcd(n,m):
#    a=[]
#    b=[]
#    c = []
#    for i in range(1,n+1):
#        if n%i==0:
#            a.append(i)
#    for i in range(1,m+1):
#        if m%i==0:
#            b.append(i)
#    for i in range(len(a)):
#        for j in range(len(b)):
#            if a[i] == b[j]:
#                c.append(b[j])
#    d = c[0]
#    for i in c[1:]:
#        if d > i:
#            continue
#        else:
#            d = i
#    return d
#res = gcd(22,48)
#print(res)

n=int(input())
m=int(input())
c=0
for i in range(1,n+1):
    if n%i==0 and m%i==0:
        c=i
print(c)

#least common multiple
#def lcm(a,b):
#    d=[]
#    f=[]
#    c=[]
#    for i in range(1,a+1):
#        d.append(a*i)
#    for i in range(1,b+1):
#        f.append(b*i)
#    for i in range(len(d)):
#        for j in range(len(f)):
#            if d[i]==f[j]:
#                c.append(d[i])
#    return c[0]

#print(lcm(16,20))
#def lcm(m,n):
#    a = 0
#    for i in range(1,m*n):
#        b = m*i
#        for j in range(1,n*m):
#            if b == n *j :
#                a = n * j
#                break
#        if a > 0 :
#            return a
#   return a

#m = int(input())
#n = int(input())
#res = lcm(m,n)
#print(res)

#Generate a Fibonacci sequence up to 50.

def fibonacci(n):
    a=[0,1]
    for i in range(1,n+1):
        b=a[i-1]+a[i]
        a.append(b)
    return a
print(fibonacci(50))

#Convert the decimal number 255 to binary, octal, and hexadecimal.
a=255
b=hex(a)
print(b)
c=bin(a)
print(c)
d=oct(a)
print(d)

#Calculate the factorial of a number using recursion.

#def fact(n):
#    b=1
#    for i in range(1,n+1):
#        b=b*i
#    return b

#print(fact(5))

def fact(n):
    if n==1 or n==0:
        return n
    else:
        return (n*fact(n-1))

print(fact(10))

#def fact(n):
#    a=1
#    for i in range(n):
#        a=n*fact(n-1)
#        break
#    return a

#print(fact(5))

#Check if a number is a perfect square.

import math
def isqrt(i):
    return i==math.isqrt(i)**2
print(isqrt(12))


#a=int(input())
#if (a**0.5)**2==a:
#    print("True")
#else:
#   print("False")

#Determine if a number is even or odd without using the modulus operator.

a=int(input())
if a/2 != a//2:
    print("odd")
else:
    print("even")

#Write a program to reverse the digits of an integer, e.g., 123 -> 321.

a=int(input())
b=str(a)
c=b[::-1]
print(c)

#Round the number 12.34567 to 3 decimal places.

a=12.34567
print(round(a,3))

#Write a program to find the sum of digits of the number 9876.

a=9876
b=str(a)
sum=0
for i in b:
    sum+=int(i)
print(sum)










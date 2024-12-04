#Write a program to check if a given number is prime.

#def is_prime(n):
#   if n<2:
#      return "Not a Prime number"
#   i=2
#   while i*i<=n:
#       if n%i==0:
#          return "Not a Prime number"
#          i += 1
#   return "Prime number"
#n = int(input())
#print(is_prime(n))

#n=int(input())
#if n<2:
#   print("Not a Prime number")
#for i in range (2,n):
#   if n%i==0:
#       print("Not a Prime number")
#       break
#  else:
#        print("Prime number")
import math

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


#def is_prime(n):
#    if n<2:
#        return False
#    i=2
#    while i<=n:
#        if n%i==0 and i !=n:
#            return False
#        i+=1
#    return True
#def prime_nums(n):
#    prime_li=[]
#    for num in range(2,n+1):
#        if is_prime(num):
#            prime_li.append(num)
#    return prime_li
#n = int(input())
#print(prime_nums(n))

def is_prime(n):
    prime_li=[]
    for i in range(1,n+1):
        c = 0
        for j in range(1,i+1):
            if i%j==0 and j != i and j != 1:
                c +=1
        if c == 0 and i != 1:
            prime_li.append(i)
    return prime_li
n = int(input())
res = is_prime(n)
print(res)

















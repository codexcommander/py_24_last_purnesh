def py():
    for i in range(40,80):
       print(i)
py()

def pt():
    pt_li=[]
    for i in range(30):
        pt_li.insert(0,i)
    print(pt_li)
print(pt())

#false case:
def pt():
    pt_li=[]
    for i in range(30):
        pt_li.insert(0,i)
print(pt())


def pt():
    pt_li=[]
    for i in range(30):
        pt_li.append(i)
    return pt_li

print(pt())

def js():
    js_li=[]
    for i in range(20,50,3):
        js_li.append(i)
    return js_li

rig=js()
print(rig)
rig.append(12345)
print(rig)

def usp():
    start=input("enter first input:")
    end=input("enter second input:")
    usp_li=[]
    for i in range(int(start),int(end)):
        usp_li.append(i)
    return usp_li

print(usp())

def usd():
    start=input("enter first input:")
    end=input("enter second input:")
    if start.isnumeric():
        start=int(start)
    if end.isnumeric():
        end=int(end)
    usd_li=[]
    for i in range(int(start),int(end)):
        usd_li.append(i)
    return usd_li

print(usd())

#multiplication table
def table(a):
    tble_li=[]
    for i in range(1,11):
        tble_li.append(a,"*",i,a*i)
    return tble_li

import math

def is_prime(n):
    if n < 2:
        return False
    i = 2
    while i*i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

print(is_prime(11))

m_li=[]
j=1
j=2
def multiples(mul):
    global j
    j=5
    for i in range(1,11):
        m_li.append(f'{mul}*{i}={j*mul}')
    return  m_li
print(multiples(5))
m_li=[]
def hello_test(x):
    for i in range(x):
        m_li.append(i)
    return m_li
print(j)
print(hello_test(5))















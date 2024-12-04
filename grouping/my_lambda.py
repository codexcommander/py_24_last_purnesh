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

a = lambda : 21 % 2 == 0
print(a)
print(a())

mul = lambda i, j: i*j
print(mul(9, 8))

pm = lambda y: sum(y)
print(pm([1, 2, 3, 4, 5, 6]))


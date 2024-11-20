
a = [8, "chintu", True, 12 , [1, 2, "reddy", False]]
print(a)
print(type(a))
print(id(a), end="\n#####\n")

print(a[2])
print(a[0:2])
print(a[1][:3])
print(a[0::3])

b = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(b[1::2])
print(b[1:7:2])
print(b[::-1])
print(a + b)

c = [1, 2, 3, 4]
# print(dir(ll))
c.append(4)
c.append(5)
c.append(5)
c.append([8, 2, 34])
c[-1].append(12)

d = c.append((33, 89, 22, 45))
print(d)
print(c)

print(c.count(2))
print(c.count(8))

e = c[-2].count(12)
print(e)
print(c)
print(c.count(20))

c.pop(3)
c.pop(-1)

f = c.pop(-1)
print(c)

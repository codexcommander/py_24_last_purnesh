
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

#sorting for only int, only strings
numbers = [4, 2, 9, 1]
numbers.sort()
print(numbers)

numbers_tuple = (6, 9, 3, 1)
numbers_set = {5, 5, 10, 1, 0}
numbers_tuple_sorted = sorted(numbers_tuple)
numbers_set_sorted = sorted(numbers_set)
print(numbers_tuple_sorted)
print(numbers_set_sorted)

l =['abc' , 'cd' , 'xy' , 'ba' , 'dc']
l.sort()
print(l)

l7 = [3, 7, 5, 9, 2, 1, 4]
l7.insert(-8, 10)
print(l7)

l7.insert(-7, ["hello", 4444, 555, 666])
print(l7)


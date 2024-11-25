s = set()
s.add(1)
s.add(3)
print(s)

s = {3, 4}
s.update({1, 2, 7, 9})
print(s)

s = {"apple", "grapes", "orange", "guava"}
s.remove("grapes")
print(s)

s = {"apple", "grapes", "orange", "guava"}
s.clear()
print(s)

s = {"apple", "grapes", "orange", "guava"}
s.pop()
print(s)

A = {1, 3, 5}
B = {0, 2, 4}
print( A | B)
print(A.union(B))

A = {1, 3, 5}
B = {1, 2, 3}
print(A & B)
print(A.intersection(B))

A = {1, 3, 5}
B = {1, 2, 3}
print(A - B)
print(A.difference(B))

A = {1, 3, 5}
B = {1, 2, 3}
print(A ^ B)
print(A.symmetric_difference(B))

A = {1, 3, 5}
B = {3, 5, 1}
if A == B:
    print('Set A and Set B are equal')
else:
    print('Set A and Set B are not equal')

A = {1, 3, 5}
B = {3, 5, 1}
print(A.isdisjoint(B))

A = {1, 3, 5}
B = {3, 5, 1}
print(A.issubset(B))

A = {1, 3, 5}
B = {3, 5, 1}
print(A.discard(B))





#Write a Python program to count the frequency of characters in a string using a dictionary.
a = "Purnesh reddy"
f = {}
c=0
for c in a:
    if c in f:
        f[c] += 1
    else:
        f[c] = 1

print(f)

#Merge two dictionaries and handle duplicate keys.
d1 = {'a': 1, 'b': 2, 'c': 3}
d2 = {'b': 20, 'd': 4}
merged_dict = d1.copy()
merged_dict.update(d2)

print(merged_dict)

#



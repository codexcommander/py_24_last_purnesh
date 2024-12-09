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

#Retrieve a value from a dictionary without causing a KeyError if the key doesn't exist.

my_dict = {"a": 1, "b": 2}
value = my_dict.get("c", "default_value")
print(value)

#Write a Python program to create a dictionary from two lists of equal length.

keys = ["name", "age", "city"]
values = ["Chintu", 26, "bglr"]

result_dict = dict(zip(keys, values))

print("Dictionary:", result_dict)

#Update a dictionary with new key-value pairs.

a = {"a": 1, "b": 2}
#b = {"b": 3, "c": 4}
#a.update(b)

#print(a)
a["b"] = 3
a["c"] = 4

print(a)

#Find the key with the maximum value in the dictionary {'a': 10, 'b': 20, 'c': 5}.

my_dict = {'a': 10, 'b': 20, 'c': 5}

max_key=max(my_dict,key=my_dict.get)
print(max_key)

#Check if a given key exists in a dictionary.

my_dict = {'a': 10, 'b': 20, 'c': 5}
key="b"

if key in my_dict:
    print("Key exists in the dictionary")
else:
    print("Key doesnt exists in the dictionary")

#Delete a key-value pair from a dictionary and return its value.

my_dict = {"a": 1, "b": 2, "c": 3}
key = "b"
deleted_value = my_dict.pop(key,2 )

print(deleted_value)
print(my_dict)

#Sort a dictionary by its keys or values.

#Write a Python program to reverse the key-value pairs in a dictionary.

my_dict = {'apple': 1, 'banana': 2, 'orange': 3}

new_dict = {value: key for key, value in my_dict.items()}

print(new_dict)














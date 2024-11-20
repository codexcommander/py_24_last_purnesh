#int
a=23
b=type(a)
print(b)

b="23"
c=int(b)
print(c)

e=("26"+"28")
print(e)
f=int(e)
print(f)

#float

a=2.4
print(type(a))

a=2.0
b=23
c=3+6j
print(type(a))
print(type(b))
print(type(c))

#strings

a="practicing strings"
print(type(a))
print(id(a))

#string slicing
print(a[0:5])
print(a[2:9])

#string concatination
a="Purnesh"
b="Reddy"
print(a+b)
print(a+" "+b)

#uppercase
a="Purnesh reddy chinthaparthy"
print(a.upper())

#lowercase
a="Purnesh reddy chinthaparthy"
print(a.lower())

#strip
a="   Purnesh reddy chinthaparthy   "
print(a.strip())

#split
a="Purnesh reddy chinthaparthy"
print(a.split("reddy"))

#replace
a="Purnesh reddy chinthaparthy"
print(a.replace("h","@"))

#captalize
a="Purnesh reddy chinthaparthy"
print(a.capitalize())

#casefold
a="Purnesh reddy chinthaparthy"
print(a.casefold())

#center
a="Purnesh"
print(a.center(12,"*"))

#count
a="Purnesh reddy chinthaparthy"
print(a.count("r"))

#encode
a="My name is Ståle"
print(a.encode())

#endswith
a="Purnesh reddy chinthaparthy"
print(a.endswith("thy"))

#expandtabs

a="Pur\tnesh r\teddy chinth\tapart\thy"
print(a.expandtabs(5))

#find
a="Purnesh reddy chinthaparthy"
print(a.find("reddy"))

#index
a="Purnesh reddy chinthaparthy"
print(a.index("ch"))

#isalnum
a="chintu635"
print(a.isalnum())
a="chi"
print(a.isalnum())

#isalpha
a="c123"
print(a.isalpha())
a="chh"
print(a.isalpha())

#lstrip
a="           Purnesh reddy chinthaparthy       "
b=a.lstrip()
print("this is ",b,"in a darkspace")

#rstrip
a="           Purnesh reddy chinthaparthy       "
b=a.rstrip()
print("this is ",b,"in a darkspace")

#partition
a="Purnesh reddy chinthaparthy"
b=a.partition("reddy")
print(b)

#rpartition
a="Purnesh reddy surname chinthaparthy"
b=a.rpartition("reddy")
print(b)

a="this is marathom race"
print(a.replace("i","@"))

li = [1, 2, 3]
li2 = [1, 2, 3]
li.append(10)
print(id(li))
print(id(li2))
print(li)











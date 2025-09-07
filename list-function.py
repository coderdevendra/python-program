# List functions part(1)

a=["Thor","Hulk","Ironmen","captain America"]

print(a)
# to find the length of a list
print(len(a))
# to count an occurence of a particuler element

print(a.count("Thor"))
# to add to the list

a.append("Spidermam")
print(a)
# a.extend("Spiderman")
# print((a))
# to add to a specify location

a.insert(1,"vision") #kisi proper location pr insert krna ke liye insert method use kiya jata hai
print(a)

# to remove from a list
a.remove("Thor")
print(a)
# to remove from a certain location
a.pop(1)
print(a)

# List functions part - 2
b=["Thor","Hulk","Ironman","Captain America"]
# to create a copy of a list

c=[]
print(c)
c=b.copy()
print(c)
# to access an element
print(b.index("Ironman"))
# to ended the list
d=["Spiderman","Vision"]
b.extend(d)
print(b)
# to reverse the list
b.reverse()
print(b)
# to sort the list
b.sort()
print(b)
x=[1,8,9,7,5,2,4,3,6]
x.sort()
print(x)
# to clear all the data from the list

b.clear()
print(b)




























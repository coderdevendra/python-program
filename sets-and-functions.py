'''
->sets
sets are unorderd collection of data. every element inside the set is
unique and mutable.

-> sets are written inside the curly brackets.
-> the value inside a set is separated by coma(,).
-> mutable means once created , they can be changed.
'''

a={"Ironman","Hulk","Thor","Captain America"}
print(a)
print(type(a))
for i in a:
    print(i)

# Set functions part - 1

# add function
a.add("spiderman")
print(a)

# pop function
a.pop()
print(a)

# remove function
a.remove("Thor")
print(a)

# discard function
a.discard("Hulk")
print(a)

# copy function
b=a.copy()
print(b)

# part -2  set functions


i={"ironman","hulk","thor","captain america"}
j={"superman","batman","wonder-woman"}
k={"hulk","thor"}

# isdisjoint
print(i.isdisjoint(k))

# issubset

print(k.issubset(i))
# issuperset

print(j.issuperset(k))

# update
m = i.update(j)
print(m)

# clear
i.clear()
print(i)

# set functions part - 3
x={"ironman","hulk","thor","captain america"}
y={"superman","batman","wonder-woman"}
z={"hulk","thor","ajay"}
# union
print(x.union(z))

# difference
print(x.difference(z))

# difference_update
print(x.difference_update(z))
# intersection
p=(x.intersection(z))
print(p)
# intersection update
x.difference_update(z)
print(x)
# symmetric difference
n=x.symmetric_difference(z)
print(n)
# symmetric difference update
x.symmetric_difference_update(z)
print(x)









# list iteration

# iteration using for loop

a=["Ironman","Thor","Captain America","Hulk"]

for i in a:
    print(i)

# iteration using for loop with range and length function

for i in range(len(a)):
    print("Indx No",i,"=",a[i])

# iteration using while loop

i=0
while i<len(a):
    print(i,a[i])
    i += 1
 



# using short hand for loop

[print(i) for i in a]





















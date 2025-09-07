# write a program for pattern problem
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5


for i in range (1,6):       # rows
    for j in range(1,i):    # columns
        print(j, end=" ")
        i=i+1
    print()

# write a probgram
# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5

for i in range (1,6):        # rows
    for j in range(1,i+1):   # columns
        print(i,end=" ")
    print()


# write a program
#         *
#       * *
#     * * *
#   * * * *
# * * * * *

for i in range (1,6):
    for j in range(5,i,-1):
        print(" ", end=" ")
    for k in range (i):
        print("*", end = " ")
    print()

# write a program

# 1
# 2 1
# 3 2 1
# 4 3 2 1
# 5 4 3 2 1

for i in range (1,6):
    for j in range (i,0,-1):
        print(j, end=" ")
    print()

# pattern problem
# 1
# 2 4
# 3 6 9
# 4 8 12 16
# 5 10 15 20 25
# 6 12 18 24 30 36
# 7 14 21 28 35 42 49


for i in range(1,8):
    for j in range(1,i+1):
        print(i*j,end=" ")
    print()




















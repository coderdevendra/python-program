# write a program to create a area calculator

print("---Area Calculator---")
while True:
    print("""press 1 to get the area of square
    press 2 get the area of rectangle
    press 3 get the area of circle
    press 4 get the area of triangle""")

    choice=int(input("Enter a number between 1-4 :"))

    if choice==1:
        while True:
            side = float(input("Enter the length of one side :"))
            area=side**2
            print("area of square : ",area)
            repeat=input("Do you want to try again with square? (yes/no)")
            if repeat=="no":
                break
    elif choice==2:
        while True:
            length=float(input("Enter the length of rectangle :"))
            width=float(input("Enter the width of rectangle:"))
            area= length*width
            print("area of rectangle : ",area)
            repeat = input("Do you want to try again with rectangle? (yes/no)")
            if repeat == "no":
                break
    elif choice==3:
        while True:
            radius = float(input("Enter the radius of the circle :"))
            area = (22/7)*(radius**2)
            print("area of circle : ",area)
            repeat = input("Do you want to try again with circle? (yes/no)")
            if repeat == "no":
                break
    elif choice==4:
        while True:
            base=float(input("Enter the base of the triangle : "))
            hight=float(input("Enter the hight of the triangle : "))
            area=(1/2)*base*hight
            print("area of triangle : ",area)
            repeat = input("Do you want to try again with triangle? (yes/no)")
            if repeat == "no":
                break
    else:
        print("Invalid choice")

    repeat1=input("Do you want to menu again? (yes/no)")
    if repeat1=="no":
        break











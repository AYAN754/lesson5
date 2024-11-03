print("y == yes and n == no")
a = str(input("do you have a medical cause?: "))
b = int(input("enter your attemdence: "))
if (a == "y"):
    if (b >= 75):
        print("you can attend exam")
    print("you can attend exam")
else:
    print("you can not attend exam")
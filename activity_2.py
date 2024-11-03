a = int(input("enter your unit"))
if (a <= 50):
    if(a >= 50 and a <= 100):
        print("per-unit cost will be 3.25, and the tax on the bill will be 35")
    print("per-unit cost will be 2.60, and the tax on the bill will be 25")
elif(a >= 100 and a <= 200):
    print("per-unit cost will be 5.26, and the tax will be 45")
else:
    print("the cost of the unit is 8.45, and the tax is 75.")
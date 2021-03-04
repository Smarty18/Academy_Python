def isTriangle (a, b, c):
    if (a+b>=c) and (a+c>=b) and (b+c>=a):
        if (a+b==c) or (a+c==b) or (b+c==a):
            print ("degenere")
        else:
            print("Sì")
    else:
        print("No!")

isTriangle(2,3,1)
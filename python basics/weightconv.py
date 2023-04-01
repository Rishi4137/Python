weight=int(input("Enter weight :"))
scale=input("Kilogram(K) or pounds(P) ")
if (scale=='k' or scale=='K'):
    print("weight in pounds :"+str(weight/2.22))
elif (scale=='p' or scale=='P'):
    print("weight in pounds :"+str(weight*2.22))
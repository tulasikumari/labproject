#check weather 5 is in the list of first 5 numbers or not.
# list =>[1,2,3,4,5] 
a=int(input("enter the first number"))
b=int(input("enter the second number"))
c=int(input("enter the third number"))
d=int(input("enter the fourth number"))
e=int(input("enter the fifth numbrer"))
list =[1,2,3,4,5]
for i in list:
    if i==5:
        print("includes number 5")
        break
    else:
       print("does not include 5")
       break
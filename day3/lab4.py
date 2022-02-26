  #Given three integers, print the smallest one.(Three integer should be user input)
a=int(input("enter a number"))
b=int(input("enter the number"))
c=int(input("enter the number"))
if a<b and a<c:
    print(f"the smallest number is {a}")
if b<c and b<a:
    print(f"the smallest number is {b}")
if c<a and c<b:
    print(f"the smallest number is {c}")
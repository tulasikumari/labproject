#program to count the number of even and odd numbers from a series of numbers. 
even=[]
odd=[]
for i in range(1,51):
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
print(f"number of even numbers are {len(even)}")
print(f"number of odd numbers are {len(odd)}")


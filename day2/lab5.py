# given the number of student in each class, print the smallest possible number of desk
# when a desk is used for two students.
a = int(input("enter the number of student in class A"))
b = int(input ("enter the number of student in calss B"))
c= int (input ("enter the number of student in class C"))
deskInA=a//2
deskInB=b//2
dwskInC=c//2
if a % 2!=0:
    deskInA +=1
if b % 2!=0:
    deskInB +=1
if c % 2!=0

# given the number of student in each class, print the smallest possible number of desk
# when a desk is used for two students.
a = int(input("enter the number of student in class A"))
b = int(input ("enter the number of student in calss B"))
c= int (input ("enter the number of student in class C"))
deskIna=a//2
deskInb=b//2 
deskInc=c//2
if a % 2!=0:
    deskIna +=1
if b % 2!=0:
    deskInb +=1
if c % 2!=0 :
    deskInc +=1
total=deskIna+deskInb+deskInc
print(f"the total number of desks requried is {total}")
  
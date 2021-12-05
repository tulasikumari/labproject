# take input for number of apple and people and divide accordingly
apples=int(input("enter the numbers of apples"))
people=int(input("enter the numbers of people"))
divided= apples // people
baskect= apples % people
print(f" each person gets {divided} apples and {baskect} apples are reamining in the baskect")

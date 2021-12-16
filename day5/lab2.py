#To convert temperature to and from celsis=c,fahrenheit=f
#c=(5/9)*(f-32)
temp1=int(input('enter the temperature in fahrenheit'))
c=(5/9)*(temp1-32)

print(c)

temp2=int(input('enter the temperature in celsius'))
f=(temp2*9/5)+32
print(f)
# find BMI of a person where take mass and height as input from the user 
# BMI=mass in kg/(height in m)**2
# kg = kilogram
# m = meter
mass=float(input("enter the mass of person in kg"))
height=float(input("enter the height of person in m"))
BMI=mass  / (height**2)
print(f"the BMI of the given data is {BMI}")
30# convert given minutes into time displayed in digital clock
minute =int(input("enter the time in minute"))
hours=minute//60
remainding=minute%60
print(f"the displayed is {hours}:{remainding}")
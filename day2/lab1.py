# convert second to day, hours , minute  and second
second=int(input("enter the value for second"))
day = second/86400
hours = second / 3600
minute = second / 60
print(f"total day for given second: {day}")
print(F"total hours for given second: {hours}")
print(f"total minute for given second: {minute}")
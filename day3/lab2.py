#WAP which acceps marks of four subjects and display total marks, percentege and grade.
#hint:more 70%-> distinction, more than 60% ->first, more than 40%->pass,less than 40%->fail
subjectA=int(input("enter the marks of maths"))
subjectB=int(input("enter the marks of physics"))
subjectC=int(input("enter the marks of chemistry"))
subjectD=int(input("enter the marks of computing"))
total=subjectA+subjectB+subjectC+subjectD
percentege=total/4
if percentege>=70:
    division="distinction"
elif percentege>=60:
    division="first"
elif percentege>=40:
    division="pass"
else:
    division="fail"
print(f"maths: {subjectA}")
print(f"physics: {subjectB}")
print(f"chemistry: {subjectC}")
print(f"computing: {subjectD}")
print(f"totalMarks: {total}")
print(F"percentage: {percentege}")
print(f"division: {division}")
 
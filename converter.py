import re

def ctof (c):
    return (9.0/5) * c +32

def ftoc (f):
    return (5.0/9) * (f-32)

temp=raw_input("Enter temperature: ")
unit=raw_input("Enter units: ")
    
if unit == "c":
    c=int(temp)
    f = ctof(c)
    print f

elif unit == "f":
    f=int(temp)
    c = ftoc(f)
    print c
else:
    print "Please enter c or f"
#to catch exceptions use a try...except, exception can be given to a variable and seen with the .args method

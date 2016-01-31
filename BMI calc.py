def bmi(w,h):
    BMI= (w/(h*h))*703
    return BMI
    
w=174.0
h=70.0

mybmi = bmi(w,h)
print "Your BMI is:", mybmi
if mybmi <18.5:
    print "Gain Weight"
else:
    if mybmi >24.5:
        print "Lose Weight"
    else:
        print "Healthy"

from bmi import bmi

weights=[123.0, 23.9, 232.9, 331.8]
heights=[77.0, 55.0, 64.0, 82.0]
names=["John", "Joe", "Jacob", "julie"]


for i in range(len(weights)):
    print i
    print names[i]
    print weights[i]
    print heights[i]
    bmi(weights[i], heights[i])
    print bmi
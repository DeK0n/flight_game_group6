#random weather function
import random
x=random.randint(1,100)
# current chance of bad weather is set to 20%
if x < 80:
    weather = "Weather is good"
    landingCondition = 1
else:
    weather = "Weather is bad"
    landingCondition = 0





#random weather function
def weather():
    import random
    x=random.randint(0,100)
    # current chance of bad weather is set to 20%
    if x <= 80:
        landing = True
    else:
        landing = False
    return landing
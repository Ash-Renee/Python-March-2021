def randInt(min=1,max=666):
    import random
    num = random.random()*(max-min) + min
    return(int(num))
print(randInt())
print(randInt(max=87)) 	    # should print a random integer between 0 to 50
print(randInt(min=34)) 	    # should print a random integer between 50 to 100
print(randInt(min=23, max=666))    # should print a random integer between 50 and 500
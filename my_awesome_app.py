# import lecture




# from random import randint or:
# import random or:
from random import *


# my_number = random.randint(0,100)
my_number = randint(0,100)

def choice(x, y):
    if my_number >= 50:
        return x
    else:
        return y


print(choice("Heads", "tails"))





import random
import string
def genearate(name):

    name = name.split(' ')[0]
    d = string.digits

    d = ''.join(random.choices(d,k=4))
    username = name+d

    return username

print(genearate("raju mayura"))
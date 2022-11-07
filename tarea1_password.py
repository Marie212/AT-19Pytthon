import random
def contras(): 
    letter = "abcdefghijklmnopqrstuvwxyz"
    mayusc = letter.upper()
    number = "0123456789"

    passw1= random.choice(letter)
    passw2= random.choice(mayusc)
    passw3= random.choice(number)
    passw4 = passw1 + passw2+ passw3
    passw6 = ""
    passw = letter + mayusc + number
    limit = random.randint(6, 13)

    for i in range(0, limit):
        passw5= random.choice(passw)
        passw6 = passw6 + passw5  
    codigo = passw6 + passw4
    return codigo

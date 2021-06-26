import random
import string

def possibleChars(type):
    possChars = string.string.ascii_letters
    if type == 'default'
        possibleChars.join(string.string.ascii_letters)
    elif type == 'strong':
        possibleChars.join(string.string.ascii_letters)
        possibleChars.join(string.string.ascii_letters)



def passGen(length, type="default"):
    output=''
    for i in range(length):
        char = ''
        char = random.choice(string.ascii_letters)
        output = output+char
    return output


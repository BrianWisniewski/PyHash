from generate import passGen

def promptUser():
    print('What would you like to do?')
    print('Create (C), Store(S), Read(R)')
    userIn = input()
    return userIn

def checkInput(Input):
    if Input != 'C' or Input != 'S' or Input != 'R':
        print('Please enter a valid input.')
        return False
    else:
        return True


if __name__ == '__main__':
    choice = promptUser()
    passLength = int(input())
    password = passGen(passLength)
    print(password)
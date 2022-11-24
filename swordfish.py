#program asks user for a name and password using break and continue statements

while True:
    print('Enter your name..?')  #Asks user for his name
    name=input()
    if name!='joe':                #checks the authenticity
        continue
    print('Hello Joe, Enter your password,(Its a fish)')  #asks password
    password=input()
    if password=='swordfish':
        break

print('Access granted')

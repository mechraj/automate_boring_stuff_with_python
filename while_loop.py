#Program to understand while loop

while True:              #intializes wile loop whose condition is always true.
    print('Enter your name.? ') #asks user for his name
    name=input()
    if name=='your name':    #checks the condition
        break                #breaks out of while loop
print('Thank you')
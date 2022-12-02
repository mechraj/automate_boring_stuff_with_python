#program that stores bithdates and if any name is not in the list, it 
#provides the user with a option to update it.

birthdays={'bob':'Apr 1','alice':'May 25','brandon':'13 Aug'} #List of brthdays

while True:
    print('Enter a name (Blank to quit)')  #Asks user to enter a name
    name=input()
    if name=='': 
        break
    if name in birthdays:  #checks the name in dictionary
        print(birthdays[name]+' is the birth date of '+name)
    else:
        print('The name is not in list. Would you like to add it.?(y/n) ')
        response=input()
        #if user wants to update the list
        if response=='y':
            print('Please enter the birthdate of '+name)
            date=input()
            birthdays[name]=date
            print('List update successfully')
        else:
            break


#Checks whether a name is in the list

my_pets=['loosie','leslie','sheldon','raj']

name=input("Enter the name of your pet: ")
if name not in my_pets:
    print('I do not have a pet named '+str(name)+'.')
else:
    print(str(name)+' is my pet')
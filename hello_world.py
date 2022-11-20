#This program prints hello world, asks user his name and age

print('Hello World!')
print('What is your name?')

user_name=input()           #Ask for a name
print('It is a pleasure to meet you '+user_name)
print('The length of your name is: ')		
print(len(user_name))		#prints the length of name
print("What is your age?")         #Ask for age
age=input()
print('You will be '+ str(int(age)+1)+' next year.!')		#prints the age user will be nexy year



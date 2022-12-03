#validates the input from th user

#to validate the age
while True:
    print('Enter your age.! ')
    age=input()
    if age.isdecimal():
        break
    print('Age can ony be a number')

#to validate the password
while True:
    print('Enter your password: ')
    password=input()
    if password.isalnum():
        break
    print('Passwors must include letters and numbers.')
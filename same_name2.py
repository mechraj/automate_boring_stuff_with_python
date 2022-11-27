#program to modify global variable inside a function

def spam(): #Initializes a function
    global eggs  #global variable used inside a fundtion
    eggs='spam'  #glabal variable value changed inside of function

eggs=75
spam()
print(eggs)
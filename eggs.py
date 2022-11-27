#program to understand scope

def spam():  #function is initialized
    eggs=99
    bacon()  #calling another function inside a function
    print(eggs)

def bacon():  
    ham=101
    eggs=500

spam()

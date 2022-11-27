#program to understand scope

def spam():  #function is initialized
    print(eggs)

eggs=99 #global variable
spam()
print(eggs)

#program to test local and global variable

def spam():  #initialazing variable
    eggs='egg_local'  
    print(eggs)   #prints egg_local

def bacon():
    eggs='bacon_local'
    print(eggs) #prints bacon_local
    spam()
    print(eggs)  #prints bacon_local

eggs='global'
spam()
print(eggs) #prints global

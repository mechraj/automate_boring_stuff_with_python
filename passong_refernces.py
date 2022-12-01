#program to understand how arguments get passed to functions

def eggs(someparameter):
    someparameter.append('hello')

spam=[1,2,3]
eggs(spam)
print(spam)

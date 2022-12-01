#program to store cats name

cat_names=[]  #List of cat names
while True:
    print('Enter the name of cat '+ str(len(cat_names)+1)+' :'+'(Enter nothing to quit)')
    name=input()
    if name=='':
        break
    else:
        cat_names=cat_names+[name]
print('You have following cats in your list.')
for cat in cat_names:
    print(cat)

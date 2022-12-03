#Program loops throgh guests lists and summarizes all the items they are bringing

#steps
#1.make a dictionary to assign names and the items hey are bringing.
#2.loop through the dictionary to check who is bringing what

guest_contribution={'alice':{'oranges':7, 'apple':5},
'megan':{'chicken':7, 'apple':10},
'claudia':{'grapes':17, 'banana':1}
}

#iterates through the dictionary and finds out quantity of all items brought by guests
def all_items(guest,item):
    items_brought=0
    for k,v in guest.items():
        items_brought=items_brought+v.get(item,0)
    return items_brought

print("Items brought by guest includes.")
print('Apples -'+str(all_items(guest_contribution,'apple')))
print('Oranges -'+str(all_items(guest_contribution,'oranges')))

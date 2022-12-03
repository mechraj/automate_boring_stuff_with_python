#program to print contents in a tabular form using l and r justify methods on strings
def print_picnic(dict_item,left_width,right_width):
    print('PICNIC ITEMS'.center(left_width+right_width,'-'))
    for k,v in dict_item.items():
        print(k.ljust(left_width,'.')+str(v).rjust(right_width))

picnicItems = {'sandwiches': 4, 'apples': 12, 'cups': 4, 'cookies': 8000}
print_picnic(picnicItems, 12, 5)
print_picnic(picnicItems, 20, 6)

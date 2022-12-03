#program that loops over a string and counts the number of characters in the string.
import pprint #Imports pretty print
message='It was a bright cold day in April.and the clocks where striking thirteen.'

count={}
for character in message:
    count.setdefault(character,0) #loops over each character in message
    count[character]=count[character]+1 

pprint.pprint(count) #pretty prints the output
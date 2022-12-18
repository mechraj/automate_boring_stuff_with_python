#Program checks if the input by the user is a phone mumber with pattern 000-000-0000

#sample text to find the phone number in
message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'
#loop through each character in a range of 12 characters
#if any range of 12 matches the pattern then print it out.


#function to check mobile number.
def is_phone_number(text):
    if len(text)!=12:
        return False
    for i in range(0,3):
        if not text[i].isdecimal():
            return False
    if text[3]!='-':
        return False
    for i in range(4,7):
        if not text[i].isdecimal():
            return False
    if text[7]!='-':
        return False
    for i in range(8,12):
         if not text[i].isdecimal():
            return False
    return True

#looping through the message
for i in range(len(message)):
    chunk=message[i:i+12]
    if is_phone_number(chunk):
        print('Phone number found: '+ chunk)
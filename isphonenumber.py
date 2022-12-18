#Program checks if the input by the user is a phone mumber with pattern 000-000-0000

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

print('415-555-4242 is a phone number:')
print(is_phone_number('415-555-4242'))
print('Moshi moshi is a phone number:')
print(is_phone_number('Moshi moshi'))
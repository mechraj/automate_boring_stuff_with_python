#!python 3
#pw.py- An insecure password manager.

#dictionary of passwords
passwords={'mail':'F7minlBDDuvMJuxESSKHFhTxFtjVB6' ,
'blog': 'VmALvQyKAxiVH5G8v01if1MLZF3sdt',
'luggage':'12345'}

import sys,pyperclip
#to check user provides 2 arguments [file name and account name]
if len(sys.argv)<2:
    print('Usage: python pw.py [account] - copy account password')
    sys.exit()
    account=sys.argv[1]  #first command line- account name
    if account in passwords:
        pyperclip.copy(passwords[account])
        print('The password for '+account+' is copied to clipboard')
    else:
        print('There is not account named '+account)


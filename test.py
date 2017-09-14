#!python
password={'email':'1234','blog':'1234567','notebook':'abcd'}
import sys
import pyperclip
if len(sys.argv)<2:
    print('usage:copy pass word')
    
account=sys.argv[1]
if account in password:
    pyperclip.copy(password[account])
    print('pass word for'+account+'copied')
else:
    print(account+'not found')

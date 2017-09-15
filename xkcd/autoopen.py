#! python
# auto open website from winR
import webbrowser
import sys
import pyperclip
if len(sys.argv)>1:
    #get add from command line
    address=''.join(sys.argv[1:])
else:
    #get addess from clipboard
    address=pyperclip.paste()

webbrowser.open('https://github.com/'+address)

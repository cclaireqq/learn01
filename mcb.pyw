#!python
# mcb.pyw saved and loads pieces of text to the clipboard
#usage:py.exe mcb.pyw save<keyword>- save clipboard to keyword参数包括mcb save keyword，保存内容到keyword
#usage:py.exe mcb.pyw<keyword> loads keyword to clipboard列出关键字,参数包括mcb list
# py.exe mcb.pyw list-loads all keyword to clipboard,列出所有关键字 ( mcb keyword
import shelve
import pyperclip
import sys
mcbShelf=shelve.open('mcb')
#save the clipboard content
if len(sys.argv)==3 and sys.argv[1].lower()=='save':
    mcbShelf[sys.argv[2]]=pyperclip.paste()
elif len(sys.argv)==2:
    if sys.argv[1].lower()=='list':
        pyperclip.copy(str(list(mcbShelf.keys())))
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])

#!python
import shelve
shelfFile=shelve.open('myData')
flowers=['lily','lotus','rose']
shelfFile['flowers']=flowers
shelfFile.close

shelfFile=shelve.open('myData')
type(shelfFile)
shelfFile['flowers']
shelfFile.close

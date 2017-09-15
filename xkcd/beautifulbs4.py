
import requests,bs4
#从网上下载页面加载并返回txt对象
#res=requests.get('http://yuehui.163.com/viewuser.do?id=614870881')
#res.raise_for_status()
#noStrachSoup=bs4.BeautifulSoup(res.text,"lxml")
#type(noStrachSoup)
# 从硬盘传递file对象
exampleFile=open('example.html')
exampleSoup=bs4.BeautifulSoup(exampleFile)
type(exampleSoup)
#有了BeautifulSoup对象后，定位html特定对象
#面向对象编程。某模块，某类引入之后，将要处理的对象整理，继承父类，通过将对象
#类中有方法，将对象名作为参数传入，该对象的数据被整理和处理，继承该方法以及特定属性
exampleFile2=open('example.html')
exampleSoup2=bs4.BeautifulSoup(exampleFile2.read())
elems=exampleSoup2.select('#header')
type(elems)
len(elems)
type(elems[0])
elems[0].getText()
str(elems[0])
elems[0].attrs
Pelems=exampleSoup2.select('p')
str(Pelems[0])
Pelems[0].getText()
str(Pelems[1])
Pelems[1].getText()
str(Pelems[2])
Pelems[2].getText()

#同过属性获得数据
import bs4
soup=bs4.BeautifulSoup(open('example.html'))
spanElem=soup.select('span')[0]
str(spanElem)
spanElem.get('id')
spanElem.get('some_nonexistent_addr')==None
spanElem.attrs

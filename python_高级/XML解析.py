# -*- coding: UTF-8 -*-

from xml.dom.minidom import parse

#使用 minidom解析器打开xml文件
doc = parse("Demo.xml")
root = doc.documentElement
print("根节点：",root)
#通过名称获取元素
books=root.getElementsByTagName("book")
for book in books:
    #获取元素的属性值
    print("book_name:",book.getAttribute('category'))
    title = book.getElementsByTagName('title')
    print('titile:',title[0].childNodes[0].data)
    author =book.getElementsByTagName('author')
    print('author:',author[0].childNodes[0].data)
    year = book.getElementsByTagName('year')
    print('year:',year[0].childNodes[0].data)
    price = book.getElementsByTagName('price')
    print('price:',price[0].childNodes[0].data)






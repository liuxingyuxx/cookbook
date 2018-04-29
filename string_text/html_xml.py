#在生成HTML或者XML文本的时候，如果正确的转换特殊标记字符是一个很容易被忽视的细节。 特别是当你使用 print() 函数或者其他字符串格式化来产生输出的时候。 使用像 html.escape() 的工具函数可以很容易的解决这类问题。

#如果你想以其他方式处理文本，还有一些其他的工具函数比如 xml.sax.saxutils.unescapge() 可以帮助你

s = 'Elements are written as "<tag>text</tag>".'

import html 
print(s)
print(html.escape(s))


#如果你正在处理的是ASCII文本，并且想将非ASCII文本对应的编码实体嵌入进去， 可以给某些I/O函数传递参数 errors='xmlcharrefreplace' 来达到这个目

s = 'Spicy Jalapeño'
s.encode('ascii', errors='xmlcharrefreplace')


#为了替换文本中的编码实体，你需要使用另外一种方法。 如果你正在处理HTML或者XML文本，试着先使用一个合适的HTML或者XML解析器

s = 'Spicy &quot;Jalape&#241;o&quot.'
from html.parser import HTMLParser
p =HTMLParser()
html = p.unescape(s)

t = 'The prompt is &gt;&gt;&gt;'
from xml.sax.saxutils import unescapge 
xml = unescapge(t)

print([s], [t])



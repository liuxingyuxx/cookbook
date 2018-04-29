#strip() 方法能用于删除开始或结尾的字符 lstrip() 和 rstrip() 分别从左和从右执行删除操作

s = ' hello   world \n'
print([s.strip()], [s.lstrip()], [s.rstrip()])


#character stripping
t = '-----ahk;lvdv-----'
print(t.strip("-"))


#如果你想处理中间的空格，那么你需要求助其他技术。比如使用 replace() 方法或者是用正则表达式替换
s = 'hello     world'
print(s.replace(' ', ''))
#不会改变s
print(s)

print("*"*40)

import re 
print(re.sub(r'\s+', ' ', s))
print(s)

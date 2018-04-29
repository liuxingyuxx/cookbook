#find() findall(), compile()

text1 = '11/27/2012'
text2 = 'Nov 27, 2012'

import re 
if re.match(r'\d+/\d+/\d+', text1):
    print('YES')
else:
    print("NO")

print(re.match(r'(\d+/\d+/\d+)', text1))

#compile can match several times
datepat = re.compile(r'\d+/\d+/\d+')

if datepat.match(text2):
    print("YES")
else:
    print("NO")

#match() 总是从字符串开始去匹配，如果你想查找字符串任意部分的模式出现位置， 使用 findall() 方法去代替。比如：

text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'

res = datepat.findall(text)
print(res)


datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
m = datepat.match('11/24/2012')
print("m: %s" % m)
print("m.group(0):%s " % m.group(0))
print("m.group[1]: %s" % m.group(1))

for day, month, year in datepat.findall(text):
    print('{}-{}-{}'.format(year, month, day))



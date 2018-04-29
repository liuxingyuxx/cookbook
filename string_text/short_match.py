#操作符后面加上?修饰符 变成非贪婪模式

import re

text2 = 'Computer says "no." Phone says "yes."'
str_pat = re.compile(r'"(.*)"')

print(str_pat.findall(text2))
print("SHORT match" + ("*" * 30))
str_pat_short = re.compile(r'"(.*?)"')
print(str_pat_short.findall(text2))

#多行匹配 re.DOTALL

import re 
comment1 = re.compile(r'/\*(.*)\*/')
comment2 = re.compile(r'/\*(.*)\*/', re.DOTALL)

text = '''/* this is a
... multiline comment */
... '''

a = comment1.findall(text)
b = comment2.findall(text)
print(a)
print("*"*20 + '多行匹配' + "*"*20)
print(b)


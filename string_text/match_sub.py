#sub() 函数中的第一个参数是被匹配的模式，第二个参数是替换模式。反斜杠数字比如 \3 指向前面模式的捕获组号
"""
text = 'yeah, but no, but yeah, but no, but yeah'
text.replace('yeah', 'yep')
'yep, but no, but yep, but no, but yep'
"""

text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
import re 
sub = re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\1-\2', text)
print(sub)

datepa = re.compile(r'(\d+)/(\d+)/(\d+)')
sub_compi = datepa.sub(r'\3--\1--\2', text)
print(sub_compi)

#如果除了替换后的结果外，你还想知道有多少替换发生了，可以使用 re.subn() 来代替

subn, n = datepa.subn(r'\3--\1--\2', text)
print(n)

# flags = re.IGNORECASE
text = 'UPPER PYTHON, lower python, Mixed Python'
res = re.findall(r'python', text, flags=re.IGNORECASE)
res_sub = re.sub(r'python', 'snake', text, flags=re.IGNORECASE)
print(res)
print('*' * 30)
print(res_sub)





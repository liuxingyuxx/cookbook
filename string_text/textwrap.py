#以指定列宽格式化字符串

s = "Look into my eyes, look into my eyes, the eyes, the eyes,the eyes, not around the eyes, don't look around the eyes, look into my eyes, you're under."

import textwrap
print(textwrap.fill(s, 60))
print(textwrap.fill(s, 30))


print(textwrap.fill(s, 38, initial_indent='   '))
print(textwrap.fill(s, 40, subsequent_indent='    '))


#特别是当你希望输出自动匹配终端大小的时候。 你可以使用 os.get_terminal_size() 方法来获取终端的大小尺寸

import os 
size = os.get_terminal_size().columns
print(size)
print(textwrap.fill(s, size))


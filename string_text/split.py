#使用多个界定浮分割字符串

import re 
line = 'dhklsd   khj;ofjk.roji;jsfv rjs'
res = re.split(r'[,.;\s]\s*', line)
print(res)

#正则表达式中是否包含一个括号捕获分组。 如果使用了捕获分组，那么被匹配的文本也将出现在结果列表中
res_ = re.split(r'([,.;\s])\s*',line)
print(res_)

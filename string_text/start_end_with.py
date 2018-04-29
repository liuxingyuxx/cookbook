#问题
#你需要通过指定的文本模式去检查字符串的开头或者结尾，比如文件名后缀，URL Scheme等等。
#
#解决方案
#检查字符串开头或结尾的一个简单方法是使用 str.startswith() 或者是 str.endswith() 方法。比如：
#
filename = 'spam.txt'
start = filename.endswith('.txt')
end = filename.startswith('python')


import os 
#os.listdir() 方法用于返回指定的文件夹包含的文件或文件夹的名字的列表。这个列表以字母顺序。 它不包括 '.' 和'..' 即使它在文件夹中
filename = os.listdir('.') #. represent the current file
print(filename)

#如果你想检查多种匹配可能，只需要将所有的匹配项放入到一个元组中去
li = [name for name in filename if name.endswith(('.py', '.md'))]
print(li)
print (any(name.endswith('.h') for name in filename))



import re 
url = 'http:www.python.org'
re.match('http|https|ftp', url)


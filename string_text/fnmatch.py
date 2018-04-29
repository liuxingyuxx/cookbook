#你想使用 Unix Shell 中常用的通配符(比如 *.py , Dat[0-9]*.csv 等)去匹配文本字符串

#from fnmatch import fnmatch,fnmatchcase
#>>> fnmatch('foo.txt', '*.txt')
#True
#>>> fnmatch('foo.txt', '?oo.txt')
#True
#>>> fnmatch('Dat45.csv', 'Dat[0-9]*')
#True
#>>> names = ['Dat1.csv', 'Dat2.csv', 'config.ini', 'foo.py']
#>>> [name for name in names if fnmatch(name, 'Dat*.csv')]
#['Dat1.csv', 'Dat2.csv']

# fnmatchcase 表示对大小写敏感  fnmatch在Linux中敏感 在Windows中不敏感 

>>> # On OS X (Mac)
>>> fnmatch('foo.txt', '*.TXT')
False
>>> # On Windows
>>> fnmatch('foo.txt', '*.TXT')
True
>>>

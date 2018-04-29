#创建一个内嵌变量的字符串，变量被它的值所表示的字符串替换掉。

#format
s = '{name} has {n} messages'
s_fo = s.format(name='LXY', n='8')
print(s_fo)

#format_map() 与 var()
name = 'LXY_'
n = 9
s_fo_var = s.format_map(vars())
print(s_fo_var)

class Info:
    def __init__(self, name, n):
        self.name = name 
        self.n = n 

a = Info('Furry', 12)
s__ = s.format_map(vars(a))
print(s__)



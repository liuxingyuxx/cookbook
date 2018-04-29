#通过某种对齐方式来格式化字符串

text = 'Hello World'
l = text.ljust(20)
print(l)
l = text.ljust(2,'=')

r = text.rjust(20)
r_ = text.rjust(20, "_")

c = text.center(20, '$')
print(r, r_)

print(c)


#format
l = format(text, '>20')
l_ = format(text,"=>20s")
c = format(text, '^20')
c_ = format(text, '*^20s')
print([l],[l_])
print([c], [c_])


mul = '{:>10s} {:>10s}'.format('Hello', 'World')
print(mul)


"""
format() 函数的一个好处是它不仅适用于字符串。它可以用来格式化任何值，使得它非常的通用。 比如，你可以用它来格式化数字：

>>> x = 1.2345
>>> format(x, '>10')
'    1.2345'
>>> format(x, '^10.2f')
'   1.23   '
>>>
"""

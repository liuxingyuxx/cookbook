#join,format

parts = ['Is', 'Chicago', 'Not', 'Chicago?']

a = ' '.join(parts)
b = '--'.join(parts)
print([a], [b])

c = '{}     {}'.format(a, b)
print(c)


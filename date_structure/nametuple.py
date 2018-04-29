#通过名称来访问元素，而不是下标

from collections import namedtuple
Subscriber = namedtuple("Subscriber", ('addr', 'date'))
sub = Subscriber('liuxy@qq.com', '2018-0-1')
print(sub)
print(sub.addr)
print(sub.date)

Stock = namedtuple('Stock', ('name', 'shares', 'price'))
def compute_cost(records):
    total = 0.0 
    for record in records:
        # 一定要注意 *
        s = Stock(*record)
        total += s.shares * s.price 
    return total

records = [('apple',3,9), ('pearl', 8, 4), ('nut', 30, 1.2)]
sum = compute_cost(records)
print (sum)

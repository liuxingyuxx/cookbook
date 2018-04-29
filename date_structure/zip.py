#怎样在数据字典中执行一些计算操作（比如求最小值、最大值、排序等等）为了对字典值执行计算操作，通常需要使用 zip() 函数先将键和值反转过来

prices = {
            'ACME': 45.23,
                'AAPL': 612.78,
                    'IBM': 205.55,
                        'HPQ': 37.20,
                            'FB': 10.75
                            }

min_price = min(zip(prices.values(), prices.keys()))
max_price = max(zip(prices.values(), prices.keys()))
print(min_price, max_price)

print_sort = sorted(zip(prices.values(), prices.keys()))

#执行这些计算的时候，需要注意的是 zip() 函数创建的是一个只能访问一次的迭代器。 比如，下面的代码就会产生错误：

price_and_names = zip(prices.values(), prices.keys())
print(max(price_and_names))
#OK
print(min(price_and_names))
#Wrong

#字典运算
prices={'ACME':45.23,
        'AAPL':512.78,
        'IBM':205.66,
        'HP':66.23,
        'FB':10.55}
min_price=min(zip(prices.values(),prices.keys()))#用zip()将键和值反转过来
max_price=max(zip(prices.values(),prices.keys()))
print(list(zip(prices.values(),prices.keys())))#output [(45.23,'acme'),(512.78,'aapl')...]
#python 3.x中zip()返回一个对象，如果想要展示列表，需要手动list()转化
print(min_price)#output (10.55,'fb')
print(max_price)#output (512.78,'aapl')
prices_sorted=sorted(zip(prices.values(),prices.keys()))#output [(10.55,'fb'),(45.23,'acme')....]
print(prices_sorted)
#zip()函数创建的知识一个只能访问一次的迭代对象，多次调用会产生错误。
pn=zip(prices.values(),prices.keys())
min_p=min(pn)#正确
#max_p=max(pn)#会报错,不能第二次调用
print('min(prices):',min(prices))
print('max(prices):',max(prices))
print('min(prices.values()):',min(prices.values()))
print('max(prices.values()):',max(prices.values()))
print('min(prices,key=lambda k:prices[k]):',min(prices,key=lambda k:prices[k]))#output key
print('max(prices,key=lambda k:prices[k]):',max(prices,key=lambda k:prices[k]))
min_value=prices[min(prices,key=lambda k:prices[k])]
max_value=prices[max(prices,key=lambda k:prices[k])]
print(min_value)
print(max_value)


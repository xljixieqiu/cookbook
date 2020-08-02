#展开嵌套的序列
from collections import Iterable

def flatten(items, ignore_types=(str, bytes)):
    for x in items:
        if isinstance(x, Iterable) and not isinstance(x, ignore_types):
            print(x)
            yield from flatten(x)
        else:
            print(x)
            yield x
items = [1, 2, [3, 4, [5, 6], 7], 8]
# Produces 1 2 3 4 5 6 7 8
for x in flatten(items):
    pass\
    #print(x)
#参数ignore_types和检测语句isinstance(x,ignore_types)用来将字符串和字节排除在可迭代对象之外，防止它们再展开成单个字符串
items1=['Dave', 'Paula', ['Thomas', 'Lewis']]
for x in flatten(items1):
    print(x)
#yield from在你在生成器中调用其他生成器时比较有用。如果不用yield from，就要调用for循环来代替
'''
yield from flatten(x)
==
for i in flatten(x):
    yield i
    '''
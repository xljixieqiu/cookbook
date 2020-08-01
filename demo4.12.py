#对不同集合上元素的迭代
#itertools.chain()方法，接受一个可迭代对象序列作为输入，并返回一个迭代器
from itertools import chain
a=[1,2,3,4]
b=['x','y','z']
for x in chain(a,b):
    print(x)
#chain()常见用法是对不同集合中的所有元素进行操作
#itertools.chain() 接受一个或多个可迭代对象作为输入参数。 然后创建一个迭代器，依次连续的返回每个可迭代对象中的元素。 这种方式要比先将序列合并再迭代要高效的多。
# Inefficent
for x in a + b:
    pass

# Better
for x in chain(a, b):
    pass
#第一种方案中， a + b 操作会创建一个全新的序列并要求a和b的类型一致。 chian() 不会有这一步，所以如果输入序列非常大的时候会很省内存。 并且当可迭代对象类型不一样的时候 chain() 同样可以很好的工作。

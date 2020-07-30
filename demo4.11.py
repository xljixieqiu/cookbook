#同时迭代多个序列
#zip()的使用
from itertools import zip_longest
xpts = [1, 5, 4, 2, 10, 7]
ypts = [101, 78, 37, 15, 62, 99]
for x,y in zip(xpts,ypts):
    print(x,y)
'''output 
1 101
5 78
4 37
…………'''
#zip(a,b)会生成一个可返回元组（x，y）的迭代器。迭代长度和短序列的长度一致。
a = [1, 2, 3]
b = ['w', 'x', 'y', 'z']
for i in zip(a,b):
    print(i)
'''output
1 w
2 x
3 y
'''
#如果这不是你想要的效果，可以使用itertools.zip_longest()函数
for i in zip_longest(a,b):
    print(i)
'''output
(1, 'w')
(2, 'x')
(3, 'y')
(None, 'z')
'''
for i in zip_longest(a,b,fillvalue=0):
    print(i)
'''output
(1, 'w')
(2, 'x')
(3, 'y')
(0, 'z')
'''
#zip()可以接受多于两个序列的参数
c=[10, 11, 12]
for i in zip(a,b,c):
    print(i)
#zip()返回一个迭代器，如果要将结对的值保存在列表中，需要使用list()
print(zip(a,b))
l=list(zip(a,b))
print(l)
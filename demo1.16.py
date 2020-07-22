#过滤序列元素
#一般方法--列表推导
import math
from itertools import compress
mylist = [1, 4, -5, 10, -7, 2, 3, -1]
print('大于零：',[n for n in mylist if n > 0])
print('小于等于零：',[n for n in mylist if n <= 0])
#列表推导的缺点就是如果输入的list很大，会产生一个非常大的结果接，占用大量内存。
#可以用生成表达式迭代产生过滤的元素
pos =(n for n in mylist if n > 0)
for x in pos:
    print(x)
#filter()函数接收一个函数 f 和一个list，这个函数 f 的作用是对每个元素进行判断，返回 True或 False，filter()根据判断结果自动过滤掉不符合条件的元素，返回由符合条件元素组成的新list。
values = ['1', '2', '-3', '-', '4', 'N/A', '5']
def is_int(val)
    try:
        x=int(val)
        return True
    except Exception:
        return False
ivals=list(filter(is_int,values))#
print(ivals)
#output['1','2','-3','4','5']
#列表推导和表达式通常是过滤数据最简单的方法。它们在过滤的时候还可以转换数据
print([math.sqrt(n) for n in mylist if n > 0])
#output [1.0, 2.0, 3.1622776601683795, 1.4142135623730951, 1.7320508075688772]
clip_neg=[n if n >0 else 0 for n in mylist]
print(clip_neg)
#itertools.compress()的使用。它以一个 iterable 对象和一个相对应的 Boolean 选择器序列作为输入参数。 然后输出 iterable 对象中对应选择器为 True 的元素。
addresses = [
    '5412 N CLARK',
    '5148 N CLARK',
    '5800 E 58TH',
    '2122 N CLARK',
    '5645 N RAVENSWOOD',
    '1060 W ADDISON',
    '4801 N BROADWAY',
    '1039 W GRANVILLE',
]
counts = [ 0, 3, 10, 4, 1, 7, 6, 1]
more5=[n>5 for n in counts]
print(more5)
more5_list=list(compress(addresses,more5))
print(more5_list)
#和 filter() 函数类似， compress() 也是返回的一个迭代器。因此，如果你需要得到一个列表， 那么你需要使用 list() 来将结果转换为列表类型。
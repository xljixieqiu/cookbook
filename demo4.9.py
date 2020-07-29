#排列组合的迭代
#遍历一个集合中元素所有的排列或组合。有3种方案：1.itertools.permutations()
from itertools import permutations,combinations,combinations_with_replacement
#permutations()接受一个集合，并产生一个元组序列。每个元组由集合中所有元素的一个排列组成
items=['a','b','c']
for p in permutations(items):
    print(p)
#也可以指定长度
for p in permutations(items,2):
    print(p)
#2.itertools.combinations()可得到输入集合中元素的所有组合
for c in combinations(items,3):#3个元素的组合
    print(c)
for c in combinations(items,2):#2个元素的组合
    print(c)
for c in combinations(items,1):#1个元素的组合
    print(c)
#3.itertools.combinations_with_replacement():同一个元素会被多次选择比如会出现（a,a,a）
for c in combinations_with_replacement(items,3):
    print(c)

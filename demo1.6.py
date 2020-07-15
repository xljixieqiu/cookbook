#字典中的键映射多个值
from collections import defaultdict
d=defaultdict(list)
d['a'].append(1)
d['a'].append(2)
d['b'].append(4)
print(d)#list 为列表，如果想保持元素的插入顺序，用列表
d=defaultdict(set)
d['a'].add(1)
d['a'].add(2)
d['b'].add(4)
print(d)#set 为集合，如果想去掉重复的元素，用集合
d={}
d.setdefault('a',[]).append(1)
d.setdefault('a',[]).append(2)
d.setdefault('b',[]).append(4)
print(d)#serdefault的用法，每次都需要创建一个一个新的初始值的实例，即[]
#用defaultdict创建一个多值映射字典
dd=defaultdict(list)
pairs=[['a',1],['a',2],['b',4]]
for key,value in pairs:
    dd[key].append(value)
print(dd)
#测试list和set的区别
pairs=[['a',1],['a',2],['b',4],['b',4]]
dl=defaultdict(list)
ds=defaultdict(set)
for key,value in pairs:
    dl[key].append(value)
print('dl:',dl)#'b':[4,4]
for key,value in pairs:
    ds[key].add(value)
print('ds:',ds)#'b':{4}

#合并多个字典或映射
#两种方法 1.collections.ChainMap()  2.dict.update()
from collections import ChainMap
a={'x':1,'z':3}
b={'y':2,'z':4}
c=ChainMap(a,b)
print(c['x'])#output 1 (from a)
print(c['y'])#output 2 (from b)
print(c['z'])#output 3 (from a)
#ChainMap接受多个字典并将他们在逻辑上变为一个字典，并没有生成一个新的字典c
#ChainMap只在内部创建了一个容纳这些字典的列表，并重新定义了一些常见的字典操作来遍历这个列表
print(len(c))
print(list(c.keys()))
print(list(c.values()))
#对c的更新或删除操作总是影响列表中的第一个字典
c['z']=10
c['w']=20
del c['x']
#del c['y']  会报错
print('a:',a)
print('b:',b)#b没有变化
#作用范围变量（没看懂）
values=ChainMap()
values['x']=1
#add a new mapping
values=values.new_child()
values['x']=2
values=values.new_child()
values['x']=3
print(values)
print(values['x'])
#discard last mapping
values=values.parents
print(values['x'])
values=values.parents
print(values['x'])
print(values)
#update()方法将两个字典合并
merged=dict(b)
merged.update(a)
print(merged)
#update()会创建一个完全不同的字典对象，原字典做了修改，不会反应到新的合并字典中
a['x']=13
print(a)
print(merged)#merged没有改变
#ChainMap使用原来的字典，它不创建新的字典，所以不会出现上面的情况
merged=ChainMap(a,b)
print(merged['x'])#output 13
a['x']=43
print(merged['x'])#output 43

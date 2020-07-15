#字典排序
from collections import OrderedDict
import json
d=OrderedDict()
d['foo']=1
d['bar']=2
d['spam']=4
d['grok']=3
for key in d:
    print(key,d[key])
#output 'foo' 1 'bar' 2 'spam' 4 'grok' 3  按照插入顺序
dd=json.dumps(d)
print(dd)
#OrderedDict大小是普通dict大小的两倍，因为内部维护着另外一个链表。用来记录顺序。

#映射名称到序列元素
#collections.namedtuple()的方法
from collections import namedtuple
Subscriber=namedtuple('Subscriber',['address','joined'])
sub=Subscriber('jonesy@example.com','2012-10-19')
print(sub,type(sub))#output Subscriber(addr='jonesy@example.com', joined='2012-10-19')
print(sub.address)
print(sub.joined)
#尽管 namedtuple 的实例看起来像一个普通的类实例，但是它跟元组类型是可交换的，支持所有的普通元组操作，比如索引和解压。
print(len(sub))
addr,joined=sub
print(addr,joined)
#普通元组代码
def compute_cost(records):
    total = 0.0
    for rec in records:
        total += rec[1] * rec[2]
    return total
#使用命名元组的版本
Stock = namedtuple('Stock', ['name', 'shares', 'price'])
def compute_cost(records):
    total = 0.0
    for rec in records:
        s = Stock(*rec)#rec为列表或元组
        total += s.shares * s.price
    return total
#_replace()方法,改变属性值。它会创建一个全新的命名元组并将对应的字段用新的值取代
s=Stock('ACME',100,132.45)
print('_replace之前:',s)
s=s._replace(shares=75)
print('_replace之后：',s)
#当命名元组有可选或者缺失字段时，可以用_replace()填充数据
S=namedtuple('S',['name','shares','price','date','time'])
s_prototype=S('',0,0,None,None)
def dict_to_stock(s):#s为字典
    return s_prototype._replace(**s)
a={'name':'ACME','shares':'100','price':123.45}
print(dict_to_stock(a))
b={'name':'ACME','shares':'100','price':123.45,'date':'12/12/2012'}
print(dict_to_stock(b))
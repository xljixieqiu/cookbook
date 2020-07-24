#转换并同时计算数据
import os
#计算平方和
nums=[1,2,3,4,5]
s=sum(x*x for x in nums)
print(s)
#一些例子
path='d:/python work/email/'
dirs=os.listdir(path)
if any(name.endswith('.py') for name in dirs):
    print('There be python')
else:
    print('there is no python')
s=('Amce',100,123.45)
print(','.join(str(x) for x in s))
portfolio = [
    {'name':'GOOG', 'shares': 50},
    {'name':'YHOO', 'shares': 75},
    {'name':'AOL', 'shares': 20},
    {'name':'SCOX', 'shares': 65}
]
min_shares=min(p['shares'] for p in portfolio)
print(min_shares)
#下面连个语句是等效的
s=sum((x * x for x in nums))#显示传递一个生成器表达式对象
s=sum(x * x for x in nums)#省略了括号，更加优雅
#使用生成表达式会比创建一个临时表更高效。临时表会创建一个额外的表，如果元素数量非常大，它会创建一个巨大的仅仅使用一次就被丢弃的临时数据结构
#示例如下
s=sum([x * x for x in nums])
#使用min()或 max()等聚集函数时，可能更倾向与生成器版本，它们接受的key关键字很有帮助
min_shares1=min(s['shares'] for s in portfolio)#output 20
min_shares2=min(portfolio,key=lambda s:s['shares'])#output {'name':'AOL','shares':'20}
print(min_shares1)
print(min_shares2)
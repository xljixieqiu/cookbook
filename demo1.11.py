#命名切片，内置slice()函数的使用
#list自带的方法
record='..................100..............512.65..............'
cost=int(record[18:21])*float(record[35:41])
print('老方案:',cost)
#slice()
share=slice(18,21)
price=slice(35,41)
cost=int(record[share])*float(record[price])
print('新方案',cost)
items=[0,1,2,3,4,5,6]
a=slice(2,4)
print(items[2:4])
print('items[a]:%s,items:%s'%(items[a],items))
items[a]=[10,11]
print('after items[a]=[10,11], items:',items)
items[2:4]=[12,13]
print('after items[2:4]=[12,13],items:',items)
del items[a]
print('after del items[a],items:',items)
#slice()的三个属性
b=slice(5,50,2)
print(b.start)#开始
print(b.stop)#结束
print(b.step)#步长
#indices(size)方法的使用
s='HelloWorld'
indices_b=b.indices(len(s))#所有值会适当缩小，以满足边界限制。这里的50就缩小成10了
print(indices_b)
for i in range(*indices_b):#python允许在list或者tuple前加一个*号，表示将list或者tuple的元素变成可变参数传进去。此例中把（5，10，2）变成了5，10，2
    print(s[i])
#*的另外用法
#1.*：将多个元素转化个一个tuple
def calc(number):
    sum=0
    for i in number:
        sum+=i
    return sum
print(calc((1,2,3,4,5)))#此时必须传入一个tuple或者list
#修改一下
def calcs(*number):
    sum=0
    for i in number:
        sum+=i
    return sum
print(calcs(1,2,3,4,5))#此时传入多个元素。
#参数前加个*，但在函数内部接受到的是一个tuple
#2.**：将参数打包成一个dict
def add(**x):
    print(x)
    sum=0
    for i in x.values():
        sum+=i
    return sum
print(add(a=1,b=4,c=6))
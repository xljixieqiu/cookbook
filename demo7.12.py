#访问闭包中定义的变量
#问题
#你想要扩展函数中某个闭包，允许他能访问和修改函数的内部变量
#解决
#通常来讲，闭包的内部变量对于外界来讲是完全隐藏的。但是你可以通过编写访问函数并将其作为函数属性绑定到闭包上来实现这个目的。
import sys
from timeit import timeit
def sample():
    n=0
    def func():
        print('n=',n)
    def get_n():
        return n
    def set_n(value):
        nonlocal n
        n=value
    #attach as function attributes
    func.get_n=get_n
    func.set_n=set_n
    return func
#下面是使用的例子
f=sample()
print(f())#n=0 注意：f就是一个闭包，闭包本质上是一个函数。所以使用时需要带括号
f.set_n(10)
print(f())#n=10
print(f.get_n())#10

#讨论
#为了说明清楚他是如何工作的，有两点需要解释下。
#首先，nonlocal声明可以让我们编写函数来修改内部变量的值。
#其次，函数属性允许我们用一种很简单的方式将访问方法绑定到闭包函数上，这个跟实例方法很像
#还可以进一步的扩展，让闭包模拟类的实例。你要做的仅仅是复制上面的内部函数到一个字典实例中并返回他即可
class ClosureInstance:
    def __init__(self,locals=None):
        if locals is None:
            locals=sys._getframe(1).f_locals
        #update instance dictionary with callables
        self.__dict__.update((key,value) for key,value in locals.items() if callable(value))
    def __len__(self):
        return self.__dict__['__len__']()
#example use
def Stack():
    items=[]
    def push(item):
        items.append(item)
    def pop():
        return items.pop()
    def __len__():
        return len(items)
    return ClosureInstance()
#下面是一个交互式会话来掩饰它是如何工作的
s=Stack()
print(s)#一个ClosureInstance对象
s.push(10)
s.push(20)
s.push('hello')
print(len(s)) #3
print(s.pop())   #hello
print(s.pop())  #20
print(s.pop())  #10
#有趣的是，这个代码运行起来会比一个普通的类定义要快很多。你可能会像下面这样测试他跟一个雷的性能对比
class Stack2:
    def __init__(self):
        self.items=[]
    def push(self,item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def __len__(self):
        return len(self.items)
#你会得到如下效果
print(timeit('s.push(1);s.pop()','from __main__ import s'))

s2=Stack2()
print(timeit('s2.push(1);s2.pop()','from __main__ import s2'))
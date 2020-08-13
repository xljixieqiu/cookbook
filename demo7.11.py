#内联回调函数
#问题
#当你编写使用回调函数的代码的时候，担心很多小函数的扩张可能会弄乱程序控制流。你希望找到某个方法来让代码看上去更像是一个普通的执行序列
#解决
#通过使用生成器和协程可以使得回调函数内联在某个函数中
#为了演示说明，假设你有如下所示的一个执行某种计算任务然后调用一个回调函数的函数
from queue import Queue
from functools import wraps
def apply_async(func,args,*,callback):
    #compute the result
    result =func(*args)
    #invoke the callback with the result
    callback(result)
#接下来让我们看一下下面代码，他包含了一个Async类和一个inlined_async装饰器
class Async:
    def __init__(self,func,args):
        self.func=func
        self.args=args
def inlined_async(func):
    @wraps(func)
    def wrapper(*args):
        f=func(*args)
        result_queue=Queue()
        result_queue.put(None)
        while True:
            result=result_queue.get()
            try:
                a=f.send(result)
                apply_async(a.func,a.args,callback=result_queue.put)
            except StopIteration:
                break
    return wrapper
#这两个代码片段允许你使用yield语句内联回调步骤。比如
def add(x,y):
    return x+y
@inlined_async
def test():
    r=yield Async(add,(2,3))
    print(r)
    r=yield Async(add,('hello','world'))
    print(r)
    for n in range(10):
        r=yield Async(add,(n,n))
        print(r)
    print('goodbye')
test()
#你会发现，除了那个特别的装饰器和yield语句外，其他地方并没有出现任何的回调函数（其实是在后台定义的）
#没懂...
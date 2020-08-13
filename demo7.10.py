#带额外状态信息的回调函数
#问题
#你的代码中需要依赖到回调函数的使用（比如时间处理器、等待后台任务完成后的回调等），并且你还需要让回调函数拥有额外的状态值，以便在它的内部使用到
#解决
#这一小节主要讨论的是那些出现在很多函数库和框架中的回调函数的使用--特别是跟异步处理有关的。
#为了演示与测试，我们先定义如下一个需要调用回调函数的函数
def apply_async(func,args,*,callback):
    #compute the result
    result=func(*args)
    #invoke the callback with the result
    callback(result)
#实际上，这段胆码可以做任何更高级的处理，包括线程，进程和定时器，但是这些都不是我们要关心的。
#我们仅仅只需要关注回调函数的调用。下面是一个演示怎样使用上述代码的例子
def print_result(result):
    print('Got:',result)
def add(x,y):
    return x+y
apply_async(add,(2,3),callback=print_result)#output Got:5
apply_async(add,('hello','world'),callback=print_result)#output helloworld
#注意到print_result()函数仅仅只接受一个参数result。不能再传入其他信息。而当你想让回到函数访问其他变量或者特定环境的变量值的时候就会遇到麻烦
#为了让回调函数访问外部信息，一种方法是使用一个板顶方法来代替一个简单函数。
#比如下面这个类会保存一个内部序列号，每次接收到一个result的时候序列号加一
class ResultHandler:
    def __init__(self):
        self.sequence=0
    def handler(self,result):
        self.sequence+=1
        print('[{}]Got:{}'.format(self.sequence,result))
#使用这个类的时候，你先创建一个类的实例，然后用他的handler()绑定方法来做为回调函数：
r=ResultHandler()
apply_async(add,(2,3),callback=r.handler)
apply_async(add,('hello','world'),callback=r.handler)
#第二种方式，作为类的替代，可以使用一个闭包捕获状态值，例如：
def make_handler():#闭包
    sequence=0
    def handler(result):
        nonlocal sequence#nonlocal作用是把变量标记为自由变量。
        sequence+=1
        print('[{}]Got:{}'.format(sequence,result))
    return handler
#下面是使用闭包方式的一个例子
handler=make_handler()
apply_async(add,(2,3),callback=handler)
apply_async(add,('hello','world'),callback=handler)
#还有另外一个更高级的方法，可以使用协程来完成童谣的事情
def make_handler1():
    sequence=0
    while True:
        retult=yield
        sequence+=1
        print('[{}]Got:{}'.format(sequence,retult))
#对于协程，你需要使用他的send()方法作为回调函数，如下所示
handler=make_handler1()
next(handler)#advance to the yield
apply_async(add,(2,3),callback=handler.send)
apply_async(add,('hello','world'),callback=handler.send)
#基于回调函数的软件通常都有可能变得非常复杂。一部分原因是回调函数通常会跟请求执行代码断开。 
#因此，请求执行和处理结果之间的执行环境实际上已经丢失了。
#如果你想让回调函数连续执行多步操作， 那你就必须去解决如何保存和恢复相关的状态信息了。

#至少有两种主要方式来捕获和保存状态信息，你可以在一个对象实例(通过一个绑定方法)或者在一个闭包中保存它。
#两种方式相比，闭包或许是更加轻量级和自然一点，因为它们可以很简单的通过函数来构造。
#它们还能自动捕获所有被使用到的变量。因此，你无需去担心如何去存储额外的状态信息(代码中自动判定)。

#如果使用闭包，你需要注意对那些可修改变量的操作。在上面的方案中， nonlocal 声明语句用来指示接下来的变量会在回调函数中被修改。如果没有这个声明，代码会报错。

#而使用一个协程来作为一个回调函数就更有趣了，它跟闭包方法密切相关。 某种意义上来讲，它显得更加简洁，因为总共就一个函数而已。 
#并且，你可以很自由的修改变量而无需去使用 nonlocal 声明。
#这种方式唯一缺点就是相对于其他Python技术而言或许比较难以理解。 另外还有一些比较难懂的部分，比如使用之前需要调用 next() ，实际使用时这个步骤很容易被忘记。 
#尽管如此，协程还有其他用处，比如作为一个内联回调函数的定义(下一节会讲到)。

#如果你仅仅只需要给回调函数传递额外的值的话，还有一种使用 partial() 的方式也很有用。 在没有使用 partial() 的时候，你可能经常看到下面这种使用lambda表达式的复杂代码：
apply_async(add,(2,3),callback=lambda r:handler(r,seq))

#闭包说明---------------------------------------------------------------------------------------------------------------
'''
1.闭包是指延伸了作用域 的函数。其中包含函数定义体中引用、但是不在定义体中定义的非全局变量
2.创建一个闭包必须满足一下几点：
     一.必须有一个内嵌函数
     二.内嵌函数必须引用外部函数中的变量
     三.外部函数的返回值必须是内嵌函数
3.闭包是一种函数，他会保留定义函数时存在的自有变量的绑定，这样调用函数时虽然定义作用域不可用了，但人能使用那些绑定。
示例：实现一个计算移动平均功能的代码。
'''
#初学者可能会用类来实现，如下
#示例1
class Averager(object):
    def __init__(self):
        self.series=[]
    def __call__(self,new_value):
        self.series.append(new_value)
        total=sum(self.series)
        return total/len(self.series)
avg=Averager()
print(avg(10))#10
print(avg(11))#10.5
print(avg(12))#11
#下面使用函数式实现：
#示例2
def make_averager():
    series=[]
    def averager(new_value):
        series.append(new_value)
        total=sum(series)
        return total/len(series)
    return averager
#调用make_averager时，返回一个averager函数对象。
#每次调用averager时，该对象会把参数添加到series中，然后计算当前平均值，如下所示：
avg=make_averager()
print(avg(10))#10
print(avg(11))#10.5
print(avg(12))#11

#注释

#在示例2中，series是make_averager函数的局部变量，因为那个函数的定义中初始化了series=[].
#可是，调用avg(10)时，make_averager函数已经返回，而他的本地作用域也一去不复返了。
#在averager函数中，series是自由变量，指未在本地作用域中绑定的变量，图形化展示如下：
'''
   def make_averager():
       series=[]                         |这部分为闭包
       def averager(new_value):          |
自由变量<--series.append(new_value)      |
           total=sum(series)             |
           return total/len(series)      |
       return averager
'''
#averager的闭包延伸到那个函数的作用域之外，包含对自由变量series的绑定

#闭包的一些属性（关于数据存储位置）

#我们可以审查返回的averager对象，发现python在__code__属性中保存局部变量和自由变量的名称
'''
# 审查make_averager创建的函数
>>> avg.__code__.co_varnames
('new_value', 'total')
>>> avg.__code__.co_freevars
('series',)
'''
#series绑定在返回的avg函数的__closure__属性中。avg.__closure__中各个元素对应于avg.__code__.co_freevars中的一个名称。
#这些元素是cell对象，有个cell_content属性，保存着真正的值。这些属性的值如示例所示：
'''
>>> avg.__code__.co_freevars
('series',)
>>> avg.__closure__
(<cell at 0x108b89828: list object at 0x108ae96c8>,)
>>> avg.__closure__[0].cell_contents
[10,11,12]
'''
#综上，闭包是一种函数，它会保留定义函数时存在的自由变量的绑定，这样调用函数时虽然定义作用域不可用了，但仍能使用那些绑定。


#nonlocal（把变量标记为自由变量）--------------------------------------------------------------------------------------------------------

#示例2的计算移动平均的方法效率并不高。原因是我们存储了所有的历史数据在列表中，然后每次调用averager时使用sum求和
#要实现相同的功能，更好的实现方法是只储存当前的总值和元素个数，使用这两个值计算移动平均值即可：
#直观来思考，我们可以对代码进行如下改进（注意：代码有缺陷！）
'''
def make_averager(): 
    count = 0
    total = 0
    def averager(new_value): 
        count += 1
        total += new_value 
        return total / count
    return averager
'''
#尝试使用该函数，会得到如下的结果：
'''
>>> avg = make_averager()
>>> avg(10)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 5, in averager
UnboundLocalError: local variable 'count' referenced before assignment
'''
#提示错误为变量count在赋值前进行了引用，实际上，total也存在相同的问题。
#接下来进一步解释，首先我们需要明白一个前提，在python中，对于一个不可变数据类型比如上述实例中count，count+=1和count=count+1是等效的。
#因此，我们在averager的定义体中为count赋值了，这会把count变成局部变量，total变量也受这个问题影响。

#示例2没遇到这个问题，因为我们没有给series赋值，我们只是调用series.append，并把他传给sum和len。也就是说，我们利用了列表是可变对象这一事实。

#但对数字，字符串，元组等不可变类型来说，只能读取，不能更新。如果尝试重新绑定，例如count+=1,其实会隐式创建局部变量count。
#这样count就不是自由变量了，因此不会保存在闭包中。

#为了解决这个问题，python3引入了nonlocal声明。他的作用是把变量标记为自有变量，即使在函数中为变量赋予新值了，也会变成自由变量。
#如果为nonlocal声明的变量赋予新值，闭包中保存的绑定会更新。新版的make_averager的正确实现如下
#示例3
def make_averager1():
    count=0
    total=0
    def averager(new_value):
        nonlocal count,total
        count +=1
        total +=new_value
        return total/count
    return averager



#协程----
#nothing
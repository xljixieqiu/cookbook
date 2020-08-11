#减少可调用对象的参数个数
#问题
#你有一个被其他python代码使用的callable对象，可能是要给回调函数或者是一个处理器，但是他的参数太多了，导致调用时出错
#解决
#如果需要减少某个函数的参数个数，你可以使用functools.partial().partial()函数允许你给一个或多个参数设置固定的值，减少接下来被调用时的参数个数
#为了演示清楚，假设你有下面这样的函数
from functools import partial
import math,logging
from multiprocessing import Pool

def spam(a,b,c,d):
    print(a,b,c,d)

#可以看出partial()固定某些参数并返回一个新的callable对象。
#这个新的callable兽兽未赋值的参数，然后跟之前已经父之过的参数合并起来，最后将所有参数传递给原始函数。
#讨论
#本节要解决的问题是让原本不兼容的代码可以一起工作。下面我会例句一系列的例子
#第一个例子是，假设你有一个点的列表来表示（x,y）坐标元组。你可以使用下面的函数来计算两点之间的距离：
points=[(1,2),(3,4),(5,6),(7,8)]
pt=(4,3)
def distance(p1,p2):
    x1,y1=p1
    x2,y2=p2
    return math.hypot(x2-x1,y2-y1)
#现在假设你想以某个点为基点，根据点和基点之间的距离俩排序所有的这些点。
#列表的sort()方法接受一个关键字参数来自定义排序逻辑，但是他只能接受一个单个参数的函数（distance()很明显不符合条件）
#现在我们可以通过使用partial()来解决这个问题


#更进一步，partial()通常被用来微调其他库函数所使用的回调函数参数。
#例如，下面这段代码，使用multiprocessing来异步计算一个结果值，然后这个值被传递给一个接受一个result值和一个可选logging参数的回调函数：
def output_result(result,log=None):
    if log is not None:
        log.debug('Got:%r',result)
#a sample function
def add(x,y):
    return x+y
if __name__=='__main__':
    s1=partial(spam,1)#a=1
    s1(2,3,4)#1,2,3,4
    s1(5,6,7)#1,5,6,7
    s2=partial(spam,d=43)#d=43
    s2(1,2,3)#1,2,3,43
    s3=partial(spam,1,2,d=43)#a=1 b=2 d=43
    s3(3)#1,2,3,43
    s3(4)#1,2,4,43
    points.sort(key=partial(distance,pt))
    print(points)
    logging.basicConfig(level=logging.DEBUG)
    log=logging.getLogger('test')
    p=Pool()
    p.apply_async(add,(3,4),callback=partial(output_result,log=log))
    p.close()
    p.join()
#当给apply_async()提供回调函数时，通过使用partial()传递额外的logging参数。
#而multiprocessing对这些一无所知--他仅仅只是使用单个值来调用回调函数
#很多时候partial()能实现的效果，lambda表达式也能实现。
    points.sort(key=lambda p:distance(pt,p))
    print(points)
    p.apply_async(add,(3,4),callback=lambda result:output_result(result,log))

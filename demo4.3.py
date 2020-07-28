#使用生成器创建新的迭代模式
def frange(start,stop,increment):
    x=start
    while x<stop:
        yield x
        x+=increment
#测试
for i in frange(0,5,0.5):
    print(i)
#使用这个函数的方法。可以用for循环迭代它或者使用其他接受迭代对象的函数 如sum(),list()
l=list(frange(1,3,0.5))
print(l)
#一个函数中需要一个yield语句即可将其转换成一个生成器。跟普通函数不同，生成器只能永夜迭代操作
#这个实验向你展示生成器的底层工作原理
def countdown(n):
    print('starting to count from :',n)
    while n>0:
        yield n
        n-=1
    print('done')
c=countdown(3)
print(c)
print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(c))
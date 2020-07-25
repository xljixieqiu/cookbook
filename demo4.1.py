#手动遍历迭代器
#next()的用法：返回迭代器的下一个项目。next() 函数要和生成迭代器的iter() 函数一起使用。
#next(iterator[, default])
def manual_iter():
    with open('f:/eula.2052.txt','rb') as f:
        try:
            while True:
                line=next(f)#针对iterator迭代器
                print(line,end='')
        except StopIteration:
            pass
#通常来讲 StopIteration用来指示迭代的结尾。你还可以通过返回一个指定的值来标记结尾，比如None
def manual_iter1():
    with open('f:/eula.2052.txt','rb') as f:
        while True:
            line=next(f,None)
            if line is None:
                break
            print(line)
manual_iter1()
#下面的交互示例向我们演示了迭代期间所发生的基本细节：
items=[1,2,3,4]
it=iter(items)
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
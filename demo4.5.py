#迭代器-class 生成器-def
#反向迭代 reversed()函数的使用方法
a=[1,2,3,4,5]
for i in reversed(a):
    print(i)
#output 54321
#反向迭代的条件：二者其一
#1.对象的大小预先确定。如上例
#2.对象实现了__reversed__()方法
#如果两者都不符合，那必须把对象转化成一个列表才行。如下
with open('e:/test.txt') as f:
    for line in reversed(list(f)):#这一层只会将line反向迭代：即最后一行变成第一行，但line中字母的排序还是正常的
        for word in reversed(list(line)):
            print(word)
#要注意的是如果可迭代对象元素很多的话，将其预先转换为一个列表要消耗大量的内存
#在类中通过定义__reversed__()方法来实现反向迭代
class Countdown:
    def __init__(self,start):
        self.start=start
    def __iter__(self):
        n=self.start
        while n>0:
            yield n
            n-=1
    def __reversed__(self):
        n=1
        while n<=self.start:
            yield n
            n+=1
for i in Countdown(30):
    print(i)
for i in reversed(Countdown(30)):
    print(i)
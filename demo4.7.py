#迭代器切片
#itertools.islice()方法的使用
import itertools
def count(n):
    while True:
        yield n
        n+=1
c=count(0)
#c[10:20]  会报错
for x in itertools.islice(c,10,20):
    print(x)
#用处貌似不大
#注意点，islice()会消耗传入迭代器中的数据。因为迭代器不可逆，所以如果想要再次访问迭代器，就需要将里面的数据放入一个列表

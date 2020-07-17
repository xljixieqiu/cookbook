#删除序列相同的元素并保持顺序(注意 是序列)
def dedupe1(items):
    seen=set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)
def dedupe2(items, key=None):
    seen = set()  #这里利用了set的特点，即无重复元素
    for item in items:
        val = item if key is None else key(item)  #处理数据，使之变成可以比较的格式，即把数据解构，其中key为解构函数,即lambda d:(d['x'],d['y']);val为解构后的数据
        print('vla:',val)
        if val not in seen:
            yield item  #这里要塞入generator的是item，因为val只是为了方便处理生成的“中间数据”，并没有什么卵用
            seen.add(val)
a=[1,5,2,4,1,9,5,6,4,5]
b=[{'x':1,'y':2},{'x':1,'y':3},{'x':1,'y':2},{'x':2,'y':4}]#a、b均为list
print(list(dedupe1(a)))
print(list(dedupe2(b,key=lambda d:(d['x'],d['y']))))
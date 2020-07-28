#带有外部状态的生成器函数
#deque的使用：deque是一个两端都可以操作的序列
#1.类似list的操作：deque.append() deque.extend() len()
#2.序列的一些操作：deque.pop() deque.leftpop()  d=deque(maxlen=3)
#enumerate()方法的使用
from collections import deque
class linehistory:
    def __init__(self,lines,histlen=3):
        self.lines=lines
        self.history=deque(maxlen=histlen)
    def __iter__(self):
        for lineno,line in enumerate(self.lines,1):
            self.history.append((lineno,line))
            yield line
    def clear(self):
        self.history.clear()
with open(r'D:\360安全浏览器下载\孤岛异兽.txt',encoding='utf-8') as f:
    lines=linehistory(f)
    for line in lines:
        if '柳月' in line:
            for lineno,line in lines.history:#注意这里是lines.history
                print('{}:{}'.format(lineno,line))#打印3行
#在迭代操作不适用for循环时，需要先调用iter()函数
d=open(r'D:\360安全浏览器下载\孤岛异兽.txt',encoding='utf-8')
lines=linehistory(d)
it=iter(lines)
print(next(it))#ok
print(next(it))#ok
print(next(it))#ok
print(next(lines))#报错
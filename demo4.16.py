#迭代器代替while循环
#一个常见的io操作程序可能会像下面这样：
import sys
chunksize=8192
def reader(s):
    while True:
        data=s.recv(chunksize)
        if data==b'':
            break
        process_data(data)
#这种代码通常可以使用iter()来代替，如下所示
def reader2(s):
    for chunk in iter(lambda: s.recv(chunksize),b''):#lambda函数 没有输入 输出s.recv(chunksize),b''
        pass
        #process_data(data)
#如果你换衣他到底能不能正常工作，可以实验下一个简单的例子。比如：
f=open('d:/git/cookbook/demo4.15.py',encoding='utf-8')
for chunk in iter(lambda: f.read(10),''):
    n=sys.stdout.write(chunk)
#跳过可迭代数据的开始部分（如果开头包含某些字符，可以跳过：注意，并不是行的开头，而是文档开头）
#itertools.dropwhile()的使用
'''test1.txt
##
# User Database
#
# Note that this file is consulted directly only when the system is running
# in single-user mode. At other times, this information is provided by
# Open Directory.
...
##
nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false
root:*:0:0:System Administrator:/var/root:/bin/sh
...
'''
from itertools import dropwhile
from itertools import islice
with open(r'e:\test1.txt',encoding='utf-8') as f:
    for line in f:
        print(line)
print('-'*50)
with open(r'e:\test1.txt',encoding='utf-8') as f:
    for line in dropwhile( lambda line:line.startswith('#'),f):
        print(line,end='')
#dropwhile(func,seq)的用法：把seq的第一个元素传入func，如果为真，则返回删除第一个元素后的其余元素，如果func返回为假，则返回所有元素，不删除。注意***迭代器在func首次为false之前不会产生任何输出。***
#所以上例中会返回...之后所有内容
#---------------------------------------------------------
#如果明确知道要跳过元素的序号，可以用itertools.islice()
items=['a', 'b', 'c', 1, 4, 10, 15]
for x in islice(items,3,None):
    print(x)#output 1,4,10,15 
#islice()函数中的3,None表示跳过前面3个元素，获取第4个到最后的所有元素。
#如果把3和None对调，则表示获取前3个元素。和[3:][:3]原理相同
#疑问，islice()不是针对迭代数据的吗，why list也可以
print('-'*50)
#dropwhile和islice是两个帮助函数，避免出现以下冗余代码
with open(r'e:\test1.txt',encoding='utf-8') as f:
    while True:
        line=next(f,'')
        if not line.startswith('#'):
            break
    while line:
        print(line)
        line=next(f,None)#next中None和上面next中的''都是可选元素。如果没有下一个元素时，返回这个可选元素（None）。没有可选元素的话，会报StopIteration
print('*'*50)
#dropwhile跳过开头的#，文中的#不会跳过
#下例为跳过所有#开头的行
with open(r'e:\test1.txt',encoding='utf-8') as f:
    lines = (line for line in f if not line.startswith('#'))#去除所有#开头的行
    for line in lines:
        print(line, end='')
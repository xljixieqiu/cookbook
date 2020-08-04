#读写压缩文件
#读写一个gzip或者bz2格式的压缩文件。可以使用gzip和bz2模块
import gzip,bz2
with gzip.open('somefile','rt') as f:
    text=f.read()
with bz2.open() as f:
    text=f.read()
#写入使用 wt
#gzip.open() 和 bz2.open() 接受跟内置的 open() 函数一样的参数， 包括 encoding，errors，newline 等等。
#当写入压缩数据时，可以使用compresslevel这个关键字来制定一个压缩级别。比如：
with gzip.open('somefile','wt',compresslevel=5) as f:
    f.write(text)
#默认的等级是9，也是最高的压缩等级。等级越低性能越好，但是数据压缩程度也越低。
#gzip.open()和bz2.open()还有一个很少被人知道的特性，他们可以作用在一个已存在并以二进制模式打开的文件上。比如：
f=open('somefile.gz','rb')
with gzip.open(f,'rt') as g:
    text=g.read()
#这样就允许 gzip 和 bz2 模块可以工作在许多类文件对象上，比如套接字，管道和内存中文件等。
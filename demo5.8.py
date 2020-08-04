#固定大小记录的文件迭代（在一个固定长度记录或者数据块的集合上迭代）
#可以使用iter()和functools.partial()
from functools import partial
record_size=32
with open('f:/Desktop/经信委/fb.doc','rb') as f:
    records=iter(partial(f.read,record_size),b'')
    for r in records:
        print(r)
#注意：如果总记录的大小不是快大小的整数倍，那么最后返回的元素的字节数会比期望值少
#iter()函数有个鲜为人知的特性，就是如果你给他传递一个可调用对象和一个标记值。它会创建一个迭代器，这个迭代器会一直调用传入的可调用对象知道他返回标记值
#即iter()一直会调用文件fb.doc直到返回b''为止，迭代结束

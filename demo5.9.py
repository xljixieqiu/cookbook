#读取二进制数据到可变缓冲区中
#你想直接读取二进制数据到一个可变缓冲区中，而不需要做任何中间复制操作。或者你想原地修改数据并将它写回到一个文件中去
#可以使用文件对象的readinto()方法
import os
def read_into_buffer(filename):
    buf=bytearray(os.path.getsize(filename))
    with open(filename,'rb') as f:
        n=f.readinto(buf)#n为buf的长度
        print(n)
    return buf
with open('d:/test.bin','wb') as f:
    f.write(b'hello world!')
buf = read_into_buffer('d:/test.bin')
print(buf)
buf[0:5]=b'hallo'
print(buf)
with open('d:/test1.bin','wb') as f:
    f.write(buf)
#文件对象的readinto()方法用来对预先分配内存的数组填充数据（注意：是已预先分配内存的数组）
#和read()不同，readinto()填充已存在的缓冲区，而不是为新对象重新分配内存在返回他。因此你可以使用它来避免大量的内存分配操作
'''
record_size=32
buf1=bytearray(record_size)
with open('somefile.bin','rb') as f:
    while True:
        n=f.readinto(buf1)#n为buf的长度
        if n<record_size:
            break
        #use the contents of buf
'''
#另外有一个有趣特性就是memoryview，他可以通过零复制的方式对已存在的缓冲区进行切片操作，甚至还能修改他的内容
m1=memoryview(buf)
print('m1:',m1)
m2=m1[-6:]
print('m2:',m2)
m2[:]=b'WORLD!'#这里必须要用m2[:]表示将m2缓冲区的数据改变成WORLD！。如果用m2=b'WORLD!'表示重新给m2赋值，不会改变原来buf的数据。
print('m2:',m2)
print('buf:',buf)#memoryview是零复制的，也就是直接操作buf。
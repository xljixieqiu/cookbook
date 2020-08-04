#读取二进制数据到可变缓冲区中
#你想直接读取二进制数据到一个可变缓冲区中，而不需要做任何中间复制操作。或者你想原地修改数据并将它写回到一个文件中去
#可以使用文件对象的readinto()方法
import os
def read_into_buffer(filename):
    buf=bytearray(os.path.getsize(filename))
    with open(filename,'rb') as f:
        f.readinto(buf)
    return buf
with open('d:/test.bin','wb') as f:
    f.write(b'hello world!')
buf = read_into_buffer('d:/test.bin')
print(buf)
buf[0:5]=b'hallo'
print(buf)
with open('d:/test1.bin','wb') as f:
    f.write(buf)
    
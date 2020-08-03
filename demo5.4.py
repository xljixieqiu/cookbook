#读取字节数据
#如读取二进制文件，比如图片，声音文件等等。rb或wb的open()
#read the entire file as a single byte string
import array
with open('f:/user/xul/destktop/foobar.jpg','rb') as f:
    data=f.read()
#write binary data to a file
with open('d:/python work/foobar.jpg','wb') as f:
    f.write(data)
'''
with open('somefile.bin','wb') as f:
    f.write(b'hello world')
'''
#在读取二进制数据时，需要指明的是所有返回的数据都是字节字符串格式的，而不是文本字符串
#在读取二进制数据的时候，字节字符串和文本字符串的语义差异可能会导致一个潜在的陷阱
#注意，索引和第二代动作返回的是字节的值而不是字节字符串
t='hello world'
b=b'hello world'
for c in t:
    print(c)
for c in b:
    print(c)
#如果你想从二进制模式的文件中读取或写入文本数据，必须确保要进行解码和编码的操作
with open('d:/python work/test1.txt','rb') as f:
    data=f.read(16)
    text=data.decode('utf-8')
print(data)
print('*'*100)
print(text)
with open('d:/python work/test2.txt','wb') as f:
    f.write(text.encode('utf-8'))
#decode：解码。即二进制--->>文本
#encode：编码.即文本--->>二进制
en=t.encode('utf-8')
de=en.decode('utf-8')
print(en)
print(de)
#二进制I/O还有一个鲜为人知的特性就是数组和C结构体类型能直接被写入，而不需要中间转换为自己对象。
nums=array.array('i',[1,2,3,4])
with open('data.bin','wb') as f:
    f.write(nums)
#这个适用于任何实现了被称之为“缓冲接口”的对象，这种对象会直接暴露其底层的内存缓冲区给能处理他的操作。二进制数据写入就是这类操作之一
#很多对象还允许通过使用文件对象的readinto()方法直接读取二进制数据到其底层内存中去。比如
a=array.array('i',[0,0,0,0,0,0,0,0])
with open('data.bin','rb') as f:
    f.readinto(a)
print(a)#output array('i',[1,2,3,4,0,0,0,0])
#readinto()一脸懵逼
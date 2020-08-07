#字符串的i/o操作
#你想使用操作类文件对象的程序来操作文本或二进制字符串,可以使用io.StringIO()和io.ByteIO()类来创建类文件对象操作字符串数据。
import io
s=io.StringIO()
s.write('hello world\n')
print('-'*100)
print('this is a test',file=s)#output hello world
print(s.getvalue())#output this is a test
t=io.StringIO('hello\nworld\n')
print(t.read(4))#前4个
print(t.read())#读取剩下的全部
#io.StringIO只能用于文本。如果要操作二进制数据，要使用io.BytesIO
b=io.BytesIO()
b.write(b'binary data')
print(b.getvalue())
#你想模拟一个普通文件的时候，io.StringIO和io.BytesIO类很有用。
#比如，在单元测试中，你可以使用StringIO来创建一个包含测试数据的类文件对象，这个对象可以被传给某个参数为普通文件对象的函数。
#需要注意的是， StringIO 和 BytesIO 实例并没有正确的整数类型的文件描述符。 因此，它们不能在那些需要使用真实的系统级文件如文件，管道或者是套接字的程序中使用。
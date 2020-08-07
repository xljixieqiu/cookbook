#增加或改变已打开文件的编码
#你想在不关闭一个一打开文件的前提下增加或改变他的unicode编码。
#如果你像给一个二进制模式打开的文件添加uni吃的编码/解码方式，可以使用os.TextIOWrapper()对象包装他，比如
import urllib.request
import io,sys
u=urllib.request.urlopen('http://baidu.com')
print(u)
f=io.TextIOWrapper(u,encoding='utf-8')
text=f.read()
print(text)
#如果你想修改一个已经打开的文本模式的文件的编码方式，可以先使用detach()方法移除已存在的文本编码层，并使用新的编码方式代替
#下面是一个在sys.stdout上修改编码的例子
'''
print(sys.stdout.encoding)
sys.stdout=io.TextIOWrapper(sys.stdout.detach(),encoding='latin-1')
print(sys.stdout.encoding)
'''
#i/o系统由一系列的层次构建而成。你可以试着运行下面这个擦欧总一个文本问价难道例子来 查看这种层次。
f=open('d:/python work/testfile/sample.txt','w')
print(f)
print(f.buffer)
print(f.buffer.raw)
#在这个例子中，io.TectIOwrapper是一个编码和解码unicode的文本处理层，
#io.BufferedWriter是一个处理二进制数据的带缓冲的I/O层，
#io.FileIO是一个表示操作系统底层文件描述符的原始文件。
#增加或改变文本编码会涉及增加或改变最上面的io.TextIOWrapper层
#一般来讲，像上面例子这样通过访问属性值来直接操作不同的层是很不安全的。例如，如果你想试着使用下面这样的技术改变编码看看会发生什么
print('before change:',f)
f=io.TextIOWrapper(f.buffer,encoding='latin-1')
print('after change:',f)
#f.write('hello')
'''write报错
Traceback (most recent call last):
  File "demo5.16.py", line 30, in <module>
    f.write('hello')
ValueError: I/O operation on closed file.
'''
#结果出错了，因为f的原始值已经被破坏了并关闭了底层的文件
#detach()方法会断开文件的最顶层并返回第二层，之后最顶层就没什么用了，例如：
f=open('d:/python work/testfile/sample.txt','w')
print(f)
b=f.detach()
print(b)
#f.write('hello')
'''write报错
Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
ValueError: underlying buffer has been detached
'''
#一旦断开最顶层后，你就可以给返回结果添加一个新的最顶层。比如：
f=io.TextIOWrapper(b,encoding='latin-1')
print(f)
#尽管已经向你演示了改变编码的方法，但是你还可以利用这种技术来改变文件行处理，错误机制以及文件处理的其他方面，例如
sys.stdout=io.TextIOWrapper(sys.stdout.detach(),encoding='ascii',errors='xmlcharrefreplace')
print('jalape\u00f1o')
#output jalape&#241;o
#注意下最后输出中的非ascii字符ñ是如何被&#241;取代的。

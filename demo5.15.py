#打印不合法的文件名
#你的程序获取了一个目录中的文件名列表，但是当他试着去打印文件名的时候程序崩溃，出现了UnicodeEncodeError异常和一条奇怪的消息--surrogates not allowed
#当打印为止的文件名是，使用下面的方法可以避免这样的错误
import os
def bad_filename(filename):
    return repr(filename)[1:-1]
filename='bäd.txt'
try:
    print(filename)
except UnicodeEncodeError:
    print(bad_filename(filename))
#这一小节诶讨论的是在编写必须处理文件系统的程序时一个不太常见又很棘手的问题。默认情况下，python假定所有文件名都已经根据sys.getfilesystemencoding()的值编码过了。
#但是有一些文件系统并没有强制要求这样做，因此允许创建文件名没有正确编码的文件。这种情况不太常见，但是总有写用户冒险这样做或者无意之中这样做了（可能是在一个有缺陷的代码中给open()函数传递了一个不合规范的文件名）
#当执行类似os.listdir()这样的函数时，这些不合规范的文件名就会让python陷入困境。一方面，他不能仅仅只是丢弃这些不合格的名字。而另一方面，他又不能将这些文件名转换为正确的文本字符串。
#python对这个文集的解决方案是从文件名中获取未解码的字节值比如\xhh并将他映射成unicode字符\udchh表示所谓的“代理编码”
#下面一个例子演示了当一个不合格目录列表中含有一个文件名为bäd.txt（使用Latin-1而不是utf-8编码）时的样子
files=os.listdir('d:/python work/testfile/')
print(files)
#如果你有代码需要操作文件名或者将文件名传递给open()这样的函数，一切都能正常工作。只有当你想要输出文件名时才会碰到些麻烦（比如打印输出到屏幕或写入日志）
for name in files:
    print(name)
#解决方案，可以将代码修改如下
for name in files:
    try:
        print(name)
    except UnicodeEncodeError:
        print bad_filename(name)
'''
spam.py
b\udce4d.txt
foo.txt
'''
#在bad_filename()函数中怎样处置决定于你自己。另外一个选择就是通过某种方式重新编码，示例如下
def bad_filename1(filename):
    temp=filename.encode(sys.getfilesystemencoding(),errors='surrogateescape')
    return temp.decode('latin-1')
#surrogateescape:这种是python在绝大部分棉线os的api中所使用的错误处理器
#他能以一种优雅的方式处理由操作系统听的数据的编码问题
#在解码出差错时会将出错字节储存到一个很少被使用的unicode编码范围内
#在编码时将那些隐藏值又还原回原先解码失败的字节序列
#他不仅对os api非常有用，也能很容哦工艺的处理其他情况下的编码错误
#使用这个 版本产生的输出如下
for name in files:
    try:
        print(name)
    except UnicodeEncodeError:
        print(bad_filename1(name))
'''
spam.py
bäd.txt
foo.txt
'''
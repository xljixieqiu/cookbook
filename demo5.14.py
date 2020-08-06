#忽略文件名编码
#你想使用原始文件名执行文件的i/o操作。也就是会所文件名没有经过系统默认的编码去解码或编码过
#默认情况下，所有的文件名都会根据sys.getfilesystemencoding()返回的文本编码来编码或解码
import sys,os
print(sys.getfilesystemencoding())
#如果因为某种原因你想忽略这种编码，可以使用一个原始字节字符串来指定一个文件名即可，比如：
with open('d:/python work/testfile/jalape\xf1o.txt','w') as f:
    f.write('Spicy!')
print(os.listdir('.'))#当前文件夹的所有文件名，子文件夹等
print('-'*100)
print(os.listdir(b'd:/python work/testfile/'))
print(os.listdir('d:/python work/testfile/'))
with open(b'd:/python work/testfile/jalape\xc3\xb1o.txt') as f:
    print(f.read())
#正如你所见，在最后两个操作中，当你给文件相关函数如open()和os.listdir()传递字节字符串时，文件名的处理方式会稍有不同
#通常来讲，你不需要担心文件名的编码和解码，普通的文件名操作应该就没问题了。但是有些操作系统允许用户通过偶然或恶意方式去创建名字不符合默认编码的文件。
#这些文件名肯能会神秘的终端那些需要处理大量文件的python程序。
#读取目录并通过原始未解码方式处理文件名可以有效的避免这样的问题，尽管这样会带来一定的编程难度。

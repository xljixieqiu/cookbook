#将文件描述符包装成文件对象
#你有一个对应于操作系统上一个已打开的I/O通道（比如文件，管道，套接字等）的整形文件描述符。你想将他包装成一个更高层的python文件对象
#解决方案
#一个文件描述符和一个打开的普通文件是不一样的。文件描述符仅仅是一个由操作系统指定的整数，用来指代某个系统的I/O通道。
#如果你碰巧由这么一个文件描述符，你可以通过open()函数来将其包装为一个python的文件对象。
#你仅仅只需要使用这个整数值的文件描述符作为第一个参数来代替文件名即可。例如：
import os,sys
#open a low-level file descriptor
fd=os.open('d:/python work/testfile/sample.txt',os.O_WRONLY|os.O_CREAT)
#turn into a proper file
f=open(fd,'wt')
f.write('hello world\n')
f.close()
#当高层的文件对象被关闭或者破坏的时候，底层的文件描述符也会被关闭。
#如果这不是你想要的结果，你可以给open()函数传递一个可选的closefd=False。比如
#create a file object ,but don't close underlying fd when done
fd=os.open('d:/python work/testfile/sample.txt',os.O_WRONLY|os.O_CREAT)
f=open(fd,'wt',closefd=False)
pass
#你也可以使用着汇总技术来构造一个别名，允许以不同于第一次打开文件的方式使用他。
#例如：下面演示如何创建一个文件对象，它允许你输出二进制数据到标准输出（通常以文本模式打开）
#create a binary-mode file for stdout
bstdout=open(sys.stdout.fileno(),'wb',closefd=False)
print(bstdout.write(b'hello world\n'))#output length 
bstdout.flush()#output hello world

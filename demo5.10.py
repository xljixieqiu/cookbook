#内存映射的二进制文件
#你想内存映射一个二进制文件到一个可变字节数组中，目的可能是为了随机访问它的内容或者是原地做些修改
#使用mmap模块来内存映射文件。下面是一个工具函数，向你演示了如何打开一个文件并以一种便捷方式内存映射这个文件
import os,mmap
def memory_map(filename,access=mmap.ACCESS_WRITE):
    size=os.path.getsize(filename)#filename include  the path of  file
    fd=os.open(filename,os.O_RDWR)#fd为filename的描述符.即fileno
    return mmap.mmap(fd,size,access=access)
#mmap.mmap(fileno, length, flags=MAP_SHARED, prot=PROT_WRITE|PROT_READ, access=ACCESS_DEFAULT[, offset])
#fileno参数通常是由 f.fileno()获得的
#access值有4种：ACCESS_READ，ACCESS_WRITE，ACCESS_COPY，ACCESS_DEFAULT。分别是读，写，写时复制，默认
'''
os.open(file, flags[, mode])
file -- 要打开的文件
flags -- 该参数可以是以下选项，多个使用 "|" 隔开：
  os.O_RDONLY: 以只读的方式打开
  os.O_WRONLY: 以只写的方式打开
  os.O_RDWR : 以读写的方式打开
  os.O_NONBLOCK: 打开时不阻塞
  os.O_APPEND: 以追加的方式打开
  os.O_CREAT: 创建并打开一个新文件
  os.O_TRUNC: 打开一个文件并截断它的长度为零（必须有写权限）
  os.O_EXCL: 如果指定的文件存在，返回错误
  os.O_SHLOCK: 自动获取共享锁
  os.O_EXLOCK: 自动获取独立锁
  os.O_DIRECT: 消除或减少缓存效果
  os.O_FSYNC : 同步写入
  os.O_NOFOLLOW: 不追踪软链接
mode -- 类似 chmod()。
'''
#为了使用这个函数，你需要有一个已创建并且内容不为空的文件。下面是个列子，教你怎样初始创建一个文件并将其内容扩充到制定大小
size=1000000
with open('d:/data','wb') as f:
    f.seek(size-1)#移动读取指针的位置。fileObject.seek(offset[, whence]) offset -- 开始的偏移量，也就是代表需要移动偏移的字节数
    f.write(b'\x00')#whence：可选，默认值为 0。给offset参数一个定义，表示要从哪个位置开始偏移；0代表从文件开头开始算起，1代表从当前位置开始算起，2代表从文件末尾算起。
#下面是一个利用memory_map()函数类内存映射文件内容的例子：
m=memory_map('d:/data')
print(len(m))
print(m[0:10])
print(m[0])
m[0:11]=b'hello world'
m.close()
with open('d:/data','rb') as f:
    print(f.read(11))
#mmap()返回的mmap对象同样也可以作为一个上下文管理器来使用，这时候底层的文件会被自动关闭。比如
with memory_map('d:/data') as m:
    print(len(m))
    print(m[0:12])
print(m.closed)
#默认情况下，memory_map()函数打开的文件同时支持读和写的操作。任何的修改内容都会复制会原来的文件中。
#如果需要制度的访问模式，可以给access赋值为mmap.ACCESS_READ.比如
filename='d:/python work/test2.txt'
m=memory_map(filename,mmap.ACCESS_READ)
#如果你想在本地修改数据，但又不像将修改协会到原始文件中，可以使用mmap.ACCESS_COPY
m=memory_map(filename,mmap.ACCESS_COPY)
#为了随机访问文件的内容，使用mmap将文件映射到内存中是一个高效和优雅的方法。
#例如你无需打开一个文件并执行大量的seek(),read(),write()调用,只需要简单的映射文件并使用切片操作访问数据即可。
#一般来讲，mmap()所暴露的内存看上去就是一个而击之数组对象。但是iter可以使用一个内存视图来解析其中的数据。比如
m=memory_map('d:/data')
v=memoryview(m).cast('I')
v[0]=7
print(m[0:4])
m[0:4]=b'\x07\x01\x00\x00'
print(v[0])
#需要强调的一点是，内存映射一个文件并不会导致整个文件被读取到内存中。
# 也就是说，文件并没有被复制到内存缓存或数组中。相反，操作系统仅仅为文件内容保留了一段虚拟内存。 
#当你访问文件的不同区域时，这些区域的内容才根据需要被读取并映射到内存区域中。 
#而那些从没被访问到的部分还是留在磁盘上。所有这些过程是透明的，在幕后完成！
'''
如果多个Python解释器内存映射同一个文件，得到的 mmap 对象能够被用来在解释器直接交换数据。 
也就是说，所有解释器都能同时读写数据，并且其中一个解释器所做的修改会自动呈现在其他解释器中。 
很明显，这里需要考虑同步的问题。但是这种方法有时候可以用来在管道或套接字间传递数据。
'''
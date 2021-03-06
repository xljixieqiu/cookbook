#序列化python对象
#问题
#你需要将一个python对象序列化为一个字节流，以便他保存到一个文件、储存到数据库或者通过网络传输它
#解决
#对于序列化最普遍的做法就是使用pickle模块。为了将一个对象保存到一个文件中，可以这样做
import pickle,math,time,threading
'''
data=...#some python object
f=open('somefile','wb')
pickle.dump(data,f)
#为了将一个对象转储为一个字符串，可以使用pickle.dump():
s=pickle.dump(data)
#为了从字节流中恢复一个对象，使用pickle.load()或pickle.loads()函数。比如:
#restore from a file
f=open('somefile','rb')
data=pickle.load(f)
#restore from a string
data =pickle.loads(s
'''
#讨论
#对于大多数应用程序来讲，dump()和load()函数的使用就是你有效使用pickle模块所学的全部了。
#它可使用于绝大部分python数据类型和用户自定义类的对象实例。
#吐过你碰到某个库可以让你在数据库中保存/恢复python对象或者是通过网络传输对象的话，那么很有可能这个库的底层就使用了pickle模块
f=open('d:/python work/testfile/somedata','wb')
pickle.dump([1,2,3,4],f)
pickle.dump('hello',f)
pickle.dump({'apple','pear','banana'},f)
f.close()
f=open('d:/python work/testfile/somedata','rb')
print(pickle.load(f))
print(pickle.load(f))
print(pickle.load(f))
f.close()
#你还能序列化函数，类，还有接口，但是结果数据仅仅将他们的名称编码成对应的代码对象。例如：
print(pickle.dumps(math.cos))
#当数据反序列化回来的时候，会先假定所有的源数据是可用的。模块，类和函数会自动按需导入进来。
#对于python数据被不同机器上的解析器所共享的应用程序而言，数据的保存可能会有问题，因为所有的机器都必须访问同一个源代码。
#注
#千万不要对不信任的数据使用pickle.load()。
#pickle在加载时有一个副作用就是他会自动加载相应模块并构造实例对象。
#但是某个坏人如果知道pickle的工作原理。
#他就可以创建一个恶意的数据导致python执行随意指定的系统命令。
#因此，一定要保证pickle只在相互之间可以认证对方的解析器的内部使用。
#有些类型的对象是不能被序列化的。
#这些通常是那些依赖外部系统状态的对象，比如打开的文件，网络连接，线程，进程，栈帧等等。
#用户自定义类可以通过提供__getstate__()和__setstate__()方法来绕过这些限制。
#如果定义了这两个方法,pickle.dump()就会调用__getstate__()获取序列化的对象。
#类似的，__setstate__()在反序列化时被调用。
#为了演示这个工作原理，下面是一个在内部定义了一个线程但仍然可以序列化和反序列化的类：
class Countdown:
    def __init__(self,n):
        self.n=n
        self.thr=threading.Thread(target=self.run)
        self.thr.daemon=True
        self.thr.start()
    def run(self):
        while self.n>0:
            print('T-minus',self.n)
            self.n-=1
            time.sleep(5)
    def __getstate__(self):
        return self.n
    def __setstate__(self,n):
        self.__init__(n)
#试着运行下面的序列化试验代码：
c=Countdown(30)
#T-minus 30
#after a few moments
time.sleep(16)
print('sleep 16 secends')
f=open('cstate.p','wb')
pickle.dump(c,f)
print('将c写入cstate.p')
f.close()
print('关闭cstate.p')
print('load cstate.p')
f=open('cstate.p','rb')
pickle.load(f)#从刚刚dump(c,f)的节点开始继续执行，也就是T-minus 26
f.close()
print('再延时9秒')
time.sleep(9)

#你可以看到线程又奇迹般的重生了，从你第一次序列化它的地方又恢复过来。
#pickle 对于大型的数据结构比如使用 array 或 numpy 模块创建的二进制数组效率并不是一个高效的编码方式。
#如果你需要移动大量的数组数据，你最好是先在一个文件中将其保存为数组数据块或使用更高级的标准编码方式如HDF5 (需要第三方库的支持)。
#由于 pickle 是Python特有的并且附着在源码上，所有如果需要长期存储数据的时候不应该选用它。
# 例如，如果源码变动了，你所有的存储数据可能会被破坏并且变得不可读取。
#坦白来讲，对于在数据库和存档文件中存储数据时，你最好使用更加标准的数据编码格式如XML，CSV或JSON。
#这些编码格式更标准，可以被不同的语言支持，并且也能很好的适应源码变更。
#最后一点要注意的是 pickle 有大量的配置选项和一些棘手的问题。 对于最常见的使用场景，你不需要去担心这个，但是如果你要在一个重要的程序中使用pickle去做序列化的话， 最好去查阅一下 官方文档 。
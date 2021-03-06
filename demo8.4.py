#创建大量对象时节省内存的方法
#问题
#你的程序要床架大量（可能有上百万）的对象，导致占用很大内存
#解决
#对于主要是用来当成简单的数据结构的类而言，你可以通过给类添加__slots__竖向来极大的减少实例所占的内存。比如：
class Date:
	__slots__=['year','month','day']
	def __init__(self,year,month,day):
		self.year =year
		self.month=month
		self.day =day
#当你定义__slots__后，python就会为实例使用一种更加紧凑的内部表示。
#实例通过一个很小的固定大小的数组来构建，而不是为每个实例定义一个字典，这跟元组或列表很类似。
#在__slots__中列出的属性名在内部被映射到这个数组的指定小标上。
#使用slots一个不好的地方就是我们不能再给实例添加新的属性了，只能使用在__slots__中定义的那些属性名。
#讨论
#使用slots后节省的内存会跟存储属性的数量和类型有关。
#一般来讲，使用到的内存总量和将数据存储在一个元组中差不多。
#为了给你一个直观认识，假设你不适用slots直接存储一个Date实例，
#在64位的python上要占用428字节，而如果使用了slots，内存占用下降到156字节。
#如果程序中需要同时创建大量的日期实例，那么这个就能极大减少内存使用量了。
#
#尽管slots看上去是一个很有用的特性，很多时候你还是得减少对它使用。
#python的很多特性都依赖于普通的基于字典的实现。
#另外，定义了slots后的类不再支持一些普通类特性了，比如多继承。
#大多数情况下，你应该只在那些经常被使用到的用作数据结构的类上定义slots
#比如在程序中需要床架某个类的几百万个实例对象
#
#关于__slots__的一个常见无趣是他可以作为一个封装工具来防止用户给实例增加新的属性。
#尽管slots可以达到这样的目的，但这个并不是他的初衷。
#__slots__更多的是用来作为一个内存优化工具。

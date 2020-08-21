#子类中扩展property
#问题
#在子类中，你想要扩展定义在父类中的property的功能
#解决
#考虑如下的代码，他定义了一个property：
class Person:
	def __init__(self,name):
		self.name=name
	#getter function
	@property
	def name(self):
		return self._name
	#setter function
	@name.setter
	def name(self,value):
		if not isinstance(value,str):
			raise TypeError('expected a string')
		self._name=value
	#deleter function
	@name.deleter
	def name(self):
		raise AttributeError("can't delete attribute")
#下面是一个示例类，他继承子Person并扩展了name属性的功能
class SubPerson(Person):
	@property
	def name(self):
		print('getting name')
		return super().name
	@name.setter
	def name(self,value):
		print('setting name to',value)
		super(SubPerson,SubPerson).name.__set__(self,value)
	@name.deleter
	def name(self):
		print('deleting name')
		super(SubPerson,SubPerson).nam.__delete__(self)
#接下来使用这个新类
s=SubPerson('Guido')
print(s.name)
s.name='Larry'
#s.name=42  报错
#如果你仅仅指向扩展property的某一个方法，那么可以像下面这样写
class SubPerson1(Person):
	@Person.name.getter
	def name(self):
		print('getting name')
		return super().name
#或者你只想修改setter方法，就这么写：
class SubPerson2(Person):
	@Person.name.setter#注意  这里是Person.name.setter
	def name(self,value):
		print('setting name to',value)
		super(SubPerson2,SubPerson2).name.__set__(self,value)
#讨论
#在子类中扩展一个property可能会引起很多不易察觉的问题，因为一个property其实是getter，setter和deleter方法的集合，而不是单个方法。
#因此，当你扩展一个property的时候，你需要先确定你是否要重新定义所有的方法还是说只修改其中某一个。

#在第一个例子中，所有的property方法都被重新定义。
#在每一个方法中，使用了super()来调用父类的实现。
#在setter函数中使用super(SubPerson,SubPerson).name.__set__(self,value)的语句是没有错的。
#为了委托给之前定义的setter方法，需要将控制权传递给之前定义的name属性的__set__()方法。
#不过获得这个方法的唯一途径是使用类变量而不是实例变量来访问他。
#这也是为什么我们要使用super(SubPerson,SubPerson)的原因

#如果你只想重定义其中一个方法，那只使用@property本身是不够的。比如，下面的代码就无法工作：
class SubPerson3(Person):
	@property
	def name(self):
		print('getting name')
		return super().name
#如果你试着运行会发现setter函数整个消失了：
'''
s=SubPerson3('Guido')
>>>
Traceback (most recent call last):
  File "D:\git\cookbook\demo8.8.py", line 72, in <module>
    s=SubPerson3('Guido')
  File "D:\git\cookbook\demo8.8.py", line 8, in __init__
    self.name=name
AttributeError: can't set attribute
'''
#你应该像之前说过的那样修改代码，即像SubPerson2
class SubPerson4(Person):
	@Person.name.getter
	def name(self):
		print('getting name')
		return super().name
#这么写后，property之前已经定义过的 方法会被赋值过来，而getter函数被替换，然后他就能按照期望的工作了：
s=SubPerson4('Guido')
print(s.name)
s.name='Larry'
print(s.name)
#子啊这个二铁别的解决方案中，我们没办法使用更加通用的方式去替换硬编码的Person类名。
#如果你不知道到底是哪个积累定义了property，那你只能通过重新定义所有property并使用super()来讲控制权传递给前面的实现。
#
#值得注意的是上面演示的第一个种技术还可以被用来扩展一个描述器（在8.9小节我们有专门的介绍)。	
#比如
class String:
	def __init__(self,name):
		self.name=name
	def __get__(self,instance,cls):
		if instance is None:
			return self
		return instance.__dict__[self.name]
	def __set__(self,instance,value):
		if not isinstance(value,str):
			raise TypeError('expected a string')
		instance.__dict__[self.name]=value
class Person1:
	name= String('name')
	def __init__(self,name):
		self.name=name
class SubPerson10(Person):
	@property
	def name(self):
		print('getting name')
		return super().name
	@name.setter
	def name(self,value):
		print('setting name to',value)
		super(SubPerson10,SubPerson10).name.__set__(self,value)
	@name.deleter
	def name(self):
		print('deleter name')
		super(SubPerson10,SubPerson10).name.__delete__(self)
#最后值得注意的是，读到这里时，你应该会发现子类化 setter 和 deleter 方法其实是很简单的。 
#这里演示的解决方案同样适用，但是在 Python的issue页面 报告的一个bug，或许会使得将来的Python版本中出现一个更加简洁的方法。
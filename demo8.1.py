#改变对象的字符串显示
#问题
#你想改变对象实例的打印或者显示输出，让他更具有可读性
#解决
#要改变一个实例的字符串表示，可以重新定义他的__str__()和__repr__()方法，例如：
class Pair:
	"""docstring for Pair"""
	def __init__(self, x,y):
		self.x = x
		self.y = y
	def __repr__(self):
		return 'Pair({0.x!r},{0.y!r})'.format(self)
	def __str__(self):
		return '({0.x!s},{0.y!s})'.format(self)
#__repr__()方法返回一个实例的代码表示形式，通常用来重新构造这个实例。
#内置的repr()函数返回这个字符串，跟我们使用交互式解释现实的值是一样的。
#__str__()方法将实例转换为一个字符串，使用str()或print()函数会输出这个字符串
p=Pair(3,4)
p#在交互模式会显示：Pair(3,4) 执行的是__repr__() 
print(p)#（3,4) 执行的是__str__()
#我们在这里还掩饰了在格式化的时候怎样使用不用的字符串表现形式。
#特别来讲 !r 格式化代码指明输出使用__repr__()来代替默认的__str__().
#你可以用前面的类来测试一下：
print('p is {0!r}'.format(p))#p is Pair(3,4)
print('p is {0}'.format(p))#p is (3,4)
#讨论
#自定义__repr__()和__str__()通常是很好的习惯，因为它能简化调式和实例输出。
#例如，如果仅仅只是打印输出或日志输出某个实例，那么程序员会看到实例更加详细语有用的信息。

#__repr__()生成的文本字符串标准做法是需要让eval(repr(x))==x为真。
#如果实在不能这样子做，应该创建一个有用的文本表示，并使用<>括起来，比如
f=open('e:/test.txt')
print(f)
#<_io.TextIOWrapper name='e:/test.txt' mode='r' encoding='cp936'>

#如果__str__()没有被定义，那么就会使用__repr__()来代替输出。
#上面的format()方法的使用看上去很有趣，格式化代码{0.x}对应的第一个参数的x属性。
#因此，在下面的函数中，0实际上指的就是self本身：
'''
def __repr__(self):
	return 'Pair({0.x!r},{0.y!r})'.format(self)
'''
#作为这种实现的一个替代，你也可以使用%操作符，就像下面：
'''
def __repr__(self):
	return 'Pair(%r,%r)'%(self.x,self.y)
'''	

#format()!的用法：！后面可以加s r a 分别对应str() repr() ascii()	
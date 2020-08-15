#自定义字符串的格式化
#问题
#你想通过format()函数和字符串方法使得一个对象能支持自定义的格式化。
#解决
#为了自定义字符串的根式，我们需要在类上面自定义__format__()方法，例如：
from datetime import date
_formats={'ymd' : '{d.year}-{d.month}-{d.day}',
    'mdy' : '{d.month}/{d.day}/{d.year}',
    'dmy' : '{d.day}/{d.month}/{d.year}'}
class  Date:
	"""docstring for  Date"""
	def __init__(self, year,month,day):
		self.year = year
		self.month = month
		self.day = day
	def __format__(self,code):
		if code=='':
			code='ymd'
		fmt=_formats[code]
		return fmt.format(d=self)
#现在Date类的实例可以支持格式化操作了，示例：
d=Date(2012,12,21)
print(format(d))#format是Date类中的方法
print(format(d,'mdy'))#'12/21/2012'
print('this date is {:ymd}'.format(d))#ymd相当于Date类中的code元素。具体如何实现，不大清楚。要看看format如何构造的
print('the date is {:mdy}'.format(d))#the date is 12/21/2012
#讨论
#_format()方法给python的字符串格式化功能提供了一个钩子。
#这里需要着重强调的是格式化代码的解析工作完全由类自己决定
#因此，格式化大妈可以是任何值。例如，参考下面来自datetime模块的代码
d=date(2012,12,21)#注意，这里重新定义了d为date实例，不再是Date实例
print(format(d))#2012-12-21
print(format(d,'%A,%B %d,%Y'))#Friday,December 21,2012
print('the end is {:%d %b %Y}.goodbye'.format(d))#The end is 21 Dec 2012.goodbye
#你想构造一个可接受任意数量参数的函数（* 接收任意数量的位置参数；** 接受任意数量的关键字参数）
#解决
#为了能让一个函数接受任意数量的位置参数，可以使用一个*参数。例如
import html
def avg(first,*rest):
    return ((first+sum(rest))/(1+len(rest)))
#sample use
print(avg(1,2))
print(avg(1,2,3,4,5,6,7,8,9))
#在这个例子中，rest室友所有其他为止参数组成的元组。然后我们在代码中把他当成一个序列来进行后续的计算
#为了接受任意数量的关键字参数，使用一个以**开头的参数，比如
def make_element(name,value,**attrs):
    keyvals=['%s="%s"' %item for item in attrs.items()]
    attr_str=' '.join(keyvals)
    element='<{name}{attrs}>{value}</{name}>'.format(name=name,attrs=attr_str,value=html.escape(value))
    return element
#example
a=make_element('item','Albatross',size='large',quantity=6)
b=make_element('p','<spam>')
print(a)
print(b)
#这里，attrs是一个包含所有别传入进来的关键字参数的字典
#如果你还希望某个函数能同时接受任意数量的位置参数和关键字参数，可以同时使用* 和**。比如
def anyavg(*args,**kwargs):
    print(args)#a tuple
    print(kwargs)#a dict
#使用这个函数时，所有为止参数会被放到args元组中，所有关键字参数会被放到字典kwargs中。
#讨论
#一个*参数只能出现在函数定义中最后一个为止参数后面，而**参数只能出现在最后一个参数。
#有一点要注意的是，在*参数后面仍然可以定义其他参数。
def c(x,*args,y):
    pass
def d(x,*args,y,**kwargs):
    pass
#这种参数就是我们所说的强制关键字参数


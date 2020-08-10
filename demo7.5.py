#定义有默认参数的函数
#问题
#你想定义一个函数或者方法，他的一个或多个参数是可选的并且有一个默认值
#解决
#定义一个有可选参数的函数是非常简单的，直接在函数定义中给参数指定一个默认值，并放到参数列表最后就行了。例如
def spam(a,b=42):
    print(a,b)
print(spam(1))
print(spam(1,2))
#如果默认参数是一个可修改的容器比如一个列表、集合或者字典，可以使用None作为默认值，就像下面这样
#using a list as a default values
def spam1(a,b=None):
    if b is None:
        b=[]
#如果你并不想提供一个默认值，而是想仅仅测试下某个默认参数是不是哟会传递进来，可以像下面这样写
_no_value=object()
def spam2(a,b=_no_value):
    if b is _no_value:
        print('No b value supplied')
#我们测试下这个函数
spam2(1)
spam2(1,2)
spam2(1,None)
#仔细观察可以发现，传递一个None值和不传递两种情况是有所差别的
#讨论
#定义带默认值参数的函数是很简单的，但绝不仅仅只是这个，还有一些东西在这里也深入讨论下。
#首先，默认参数的值仅仅在函数定义的时候赋值一次，试着运行下面这个例子。
x=42
def spam3(a,b=x):
    print(a,b)
spam3(1)
x=23
spam3(1)
#注意到当我们改变x的值的时候对默认参数值并没有影响，这是应为在函数定义的时候就已经确定了他的默认值了。
#其次，默认参数的值应该是不可变的对象，比如None，True，False，数字或字符串。特别的，千万不要像下面这样写代码
def spam4(a,b=[]):#NO!
    pass
#如果你这么做了，当默认值在其他地方被修改后你将会遇到各种麻烦。这些修改会影响到下次调用这个函数时的默认值。比如
def spam5(a,b=[]):
    print(b)
    return b
x=spam5(1)
print('before append',x)
x.append(99)
x.append('yow!')
print('after append:',x)
spam5(1)#modified list gets returned!返回修改后的b
#这种结果应该不是你想要的。为了避免这种情况的发生，最好是将默认值设为None，然后在函数里面检查他，前面的例子就是这样做的
#在测试None值时使用is操作符时很重要的，也是这种翻案的关键点。有时候大家会犯下面这样的错误：
def spam6(a,b=None):
    if not b:#NO! use 'b' is None instead
        b=[]
#这么写的问题在于尽管None值确实是被当成False，但是还有其他的对象（比如长度为0的字符串，列表，元组。字典等）都会被当作False。
#因此，上面的代码会误将一些其他输入也当成是没有输入。比如：
spam6(1)#OK
x=[]
spam6(1,x)#silent error.x value overwittern by default
spam6(1,0)#silent error, 0 ignored
spam6(1,'')#silent erroe,'' ignored
#最后一个问题比较微妙，那就是一个函数需要测试某个可选数是否被使用者传递进来。
#这时候需要小心的是你不能用某个默认值比如None，0或者False值来测试用户提供的值（因为这些值都是合法的值，是可能被用户传递进来的）。因此，你需要其他的解决方案
#为了解决这个问题，你可以创建一个独一无二的私有对象实例，就像上面的_no_value变量那样。
#在函数里面，你可以检查被传递参数值跟这个实例是否一样来判断。这里的思路是用户不可能去传递这个_no_value实例作为输入。
#因此，这里通过检查这个值就能确定某个参数是否被传递进来了

#这里对object()的使用看上去有点不大常见。object是python中所有类的基类。
#你可以创建object类的实例，但是这些实例没什么实际用处，因为他并没有任何有用的方案，也没有任何实例数据。
#你唯一能做的就是测试同一性。这个刚好符合我们的要求，因为我在函数中就只是需要一个同一性的测试而已。
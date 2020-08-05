#文件路径名的操作
#你需要使用路径名来获取文件名，目录名，绝对路径等。可以使用os.path模块中的函数来操作路径名.
import os
path='/Users/beazley/Data/data.csv'
print(os.path.basename(path))#get the last component of the path
print(os.path.dirname(path))#get the directory name
print(os.path.join('tmp','data',os.path.basename(path)))#join path components together
path='~/Data/data.csv'
print(os.path.expanduser(path))#expand the user's home directory.将参数中开头部分的 ~ 或 ~user替换为当前用户的家目录并返回
print(os.path.splitext(path))#split the pathname into a pair(root,ext).ext is empty or begins with a period(英文句号) contains at most one period.
#leading periods on the basename are ignored(在最前的英文句号会被忽略)。例如:splitext('.cshrc') 返回('.cshrc','')
'''
对于任何的文件名的操作，你都应该使用 os.path 模块，而不是使用标准字符串操作来构造自己的代码。 
特别是为了可移植性考虑的时候更应如此， 因为 os.path 模块知道Unix和Windows系统之间的差异并且能够可靠地处理类似 Data/data.csv 和 Data\data.csv 这样的文件名。 
其次，你真的不应该浪费时间去重复造轮子。通常最好是直接使用已经为你准备好的功能。
要注意的是 os.path 还有更多的功能在这里并没有列举出来。 
可以查阅官方文档来获取更多与文件测试，符号链接等相关的函数说明。
'''
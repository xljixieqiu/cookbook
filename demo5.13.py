#获取文件夹中的文件列表
#你想获取文件系统中某个目录下的所有文件列表。可以使用os.listdir()函数
import os,glob,time
from fnmatch import fnmatch
names=os.listdir('d:/python work')
print(names)
#结果会返回目录中所有文件列表，包括所有文件，子目录，符号链接等。如果你需要过滤数据，可以考虑节后os.path库中的一些函数来使用列表推导
#get all regular files
path='d:/python work'
names=[name for name in os.listdir(path) if os.path.isfile(os.path.join(path,name))]
dirnames=[name for name in os.listdir(path) if os.path.isdir(os.path.join(path,name))]
print(names)
print(dirnames)
#字符串的startswith()和endswith()方法对于过滤一个目录的内容也是很有用的。比如
pyfile=[name for name in os.listdir('d:/python work/email') if name.endswith('.py')]
print(pyfile)
#对于文件名的匹配，你肯能会考虑使用glob或fnmatch模块，比如
pyfiles=glob.glob('d:/python work/email/*.py')
print(pyfiles)#output 完整路径
pyfiles=[name for name in os.listdir('d:/python work/email') if fnmatch(name,'*.py')]
print(pyfiles)#output 文件名
#获取目录中的劫镖是很容易的，但是其返回结果只是目录中实体名列表而已
#如果你还想获取其他的袁信息，比如文件大小，修改时间等等，你或许还需要使用到os.path模块中的函数或者os.stat()函数来收集数据
pyf=glob.glob('*.py')
name_sz_date=[(name,os.path.getsize(name),os.path.getmtime(name)) for name in pyf]
for name,size,mtime in name_sz_date:
    print(name,size,time.ctime(mtime))
file_metadata=[(name,os.stat(name)) for name in pyf]
for name,meta in file_metadata:
    print(name,meta.st_size,meta.st_mtime)
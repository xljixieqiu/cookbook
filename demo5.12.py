#检测文件是否存在
#你想测试一个文件或目录是否存在。可以使用os.path模块
import os,time
print(os.path.exists('d:/python work/sorted_file_1.txt'))
print(os.path.exists('d:/python work/test1.txt'))
#你还能进一步测试这个文件是什么类型。在下面这些测试中，如果测试的文件不存在的时候，结果都会返回False
#is a regular file
print(os.path.isfile('d:/python work/sorted_file_1.txt'))
#is a directory
print(os.path.isdir('d:/python work/'))
#is a symbolic link
print(os.path.islink('d:/python work/'))
#get the file linked to
print(os.path.realpath('d:/python work/'))#返回指定文件的规范路径，消除路径中存在的任何符号链接
#如果你还想获取元数据（比如文件大小或者修改日期）
print(os.path.getsize('d:/python work/sorted_file_1.txt'))
print(os.path.getmtime('d:/python work/sorted_file_1.txt'))
print(time.ctime(os.path.getmtime('d:/python work/sorted_file_1.txt')))
#创建数据处理管道（处理大量数据，但不能一次性放入内存）
'''
生成器函数是一个实现管道机制的好办法。 为了演示，假定你要处理一个非常大的日志文件目录：

foo/
    access-log-012007.gz
    access-log-022007.gz
    access-log-032007.gz
    ...
    access-log-012008
bar/
    access-log-092007.bz2
    ...
    access-log-022008
假设每个日志文件包含这样的数据：

124.115.6.12 - - [10/Jul/2012:00:18:50 -0500] "GET /robots.txt ..." 200 71
210.212.209.67 - - [10/Jul/2012:00:18:51 -0500] "GET /ply/ ..." 200 11875
210.212.209.67 - - [10/Jul/2012:00:18:51 -0500] "GET /favicon.ico ..." 404 369
61.135.216.105 - - [10/Jul/2012:00:20:04 -0500] "GET /blog/atom.xml ..." 304 -
...
为了处理这些文件，你可以定义一个由多个执行特定任务独立任务的简单生成器函数组成的容器。
'''
import os,fnmatch,gzip,bz2,re
#test os.wall()
#for dirpath,dirname,filename in os.walk(r'D:\arswp'):
#    print('dirpath:%s||dirname:%s||filename:%s'%(dirpath,dirname,filename))
#dirpath：当前文件夹路径
#dirname:当前文件夹下所有子文件夹名字的列表
#filename:点前文件夹下所有文件的名字列表
def  gen_find(filepat,top):
    '''
    Find all filenames in a directory tree that match a shell wildcard pattern
    '''
    for dirpath,dirname,filename in os.walk(top):
        for name in fnmatch.filter(filename,dilepat):#匹配filename中是否包含filepat,不包含则丢弃
            yield os.path.join(dirpath,name)#返回所有文件路径
def gen_opener(filenames):
    '''
    Open a sequence of filenames one at a time producing a file object.
    The file is closed immediately when proceeding to the next iteration.
    '''
    for filename in filenames:
        if filename.endswith('gz'):
            f=gzip.open(filename,'rt')
        elif filename.endswith('bz2'):
            f=bz2.open(filename,'rt')
        else:
            f=open(filename,'rt')
        yield f
        f.close()
def gen_concaternate(iterrators):
    '''
    Chain a sequence of iterators together into a single sequence.
    '''
    for it in iterators:
        yield from it
def gen_grep(pattern,lines):
    '''
    Look for a regex pattern in a sequence of lines
    '''
    pat=re.compile(pattern)
    for line in lines:
        if pat.search(line):
            yield line
#现在你可以很容易的将这些函数连起来创建一个处理管道。 比如，为了查找包含单词python的所有日志行，你可以这样做：
lognames=gen_find('access-log','www')
files=gen_opener(lognames)
lines=gen_concaternate(files)
pylines=gen_grep('(?i)python',lines)
for line in pylines:
    print(line)
#如果将来的时候你想扩展管道，你甚至可以在生成表达式中包装数据。比如下面这个版本计算出传输的自己数并计算其总和
bytecolumn=(line.rsplit(None,1)[1] for line in pylines)
bytes=(int(x) for x in bytecolumn if x !='-')
print('Total',sum(bytes))
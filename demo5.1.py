#读写文本数据
#如果你要读写各种不同编码的文本数据，比如ASC||，UTF-8或UTF-16编码。可以使用带rt模式的open()
import sys
with open('d:/python work/r.txt','rt') as f:#read the entire file as a single string
    data=f.read()
with open('d:/python work/r.txt','rt') as f:#iterate over the lines of the file
    for line in f:
        pass
        #print(line)
#类似的，可以用带rt的open()写入一个文本，如果之前的文本内容存在则清除并覆盖。
with open('d:/python work/r.txt','wt') as f:#write chunks of text data(写入text1text2)
    f.write('text1')
    f.write('text2')
line1='line1hello'
line2='line2bye'

with open('d:/python work/r.txt','wt') as f:#redirected print statement(重定向打印语句)。效果和f.write()一样。但是不会print
    print(line1,file=f)
    print(line2,file=f)
#如果是在已存在文件中添加内容，使用模式为 at 的 open() 函数。
#文件的读写操作默认使用系统编码，可以通过调用 sys.getdefaultencoding() 来得到。
#如果你已经知道你要读写的文本是其他编码方式， 那么可以通过传递一个可选的 encoding 参数给open()函数。
print(sys.getdefaultencoding())#output 'utf-8'
'''
with open('somefile.txt','rt',encoding='latin-1') as f:
    pass
#with 控制块结束时，文件会自动关闭。你也可以不使用 with 语句，但是这时候你就必须记得手动关闭文件
#另外一个问题是关于换行符的识别问题，在Unix和Windows中是不一样的(分别是 \n 和 \r\n )。
#默认情况下，Python会以统一模式处理换行符。 这种模式下，在读取文本的时候，Python可以识别所有的普通换行符并将其转换为单个 \n 字符。 类似的，在输出时会将换行符 \n 转换为系统默认的换行符。
# 如果你不希望这种默认的处理方式，可以给 open() 函数传入参数 newline='' ，就像下面这样：
with open('somefile.txt', 'rt', newline='') as f:
    pass
#为了说明两者之间的差异，下面我在Unix机器上面读取一个Windows上面的文本文件，里面的内容是 hello world!\r\n ：
# Newline translation enabled (the default)
f = open('hello.txt', 'rt')
print(f.read())
#'hello world!\n'
f.close()
 # Newline translation disabled
g = open('hello.txt', 'rt', newline='')
print(g.read())
#'hello world!\r\n'
f.close()'''
#你读取或者写入一个文本文件时，你可能会遇到一个编码或者解码错误
#如果出现这个错误，通常表示你读取文本时指定的编码不正确。 
#你最好仔细阅读说明并确认你的文件编码是正确的(比如使用UTF-8而不是Latin-1编码或其他)。
#如果编码错误还是存在的话，你可以给 open() 函数传递一个可选的 errors 参数来处理这些错误。
# 下面是一些处理常见错误的方法
# Replace bad chars with Unicode U+fffd replacement char
f = open('d:/python work/test1.txt', 'rt', encoding='ascii', errors='replace')
print(f.read())
f.close()#用？代替
# Ignore bad chars entirely
g = open('d:/python work/test1.txt', 'rt', encoding='ascii', errors='ignore')
print(g.read())#直接丢弃
f.close()
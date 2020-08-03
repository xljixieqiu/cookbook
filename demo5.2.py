#打印输出值文件中
#用print()函数的输出重定向到一个文件中去,可以使用file关键字，如下:
with open('d:/python work/test1.txt','wt') as f:
    print('Hello World!',file=f)
#注意的就是文件必须是以文本模式打开。 如果文件是二进制模式的话，打印就会出错。
#当文件不存在才能写入。也就是不允许覆盖已存在的文件内容
#可以在open()函数中使用x模式代替w模式来实现
import os
with open('d:/python work/test1.txt','wt') as f:
    pass
'''
with open('d:/python work/test1.txt','xt') as f:#会报错
    pass
'''
#代替方案
path='d:/python work/test1.txt'
if not os.path.exists(path):
    with open(path,'wt') as f:
        f.write('hello\n')
else:
    print('file is already exists')
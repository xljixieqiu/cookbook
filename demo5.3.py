#使用其他分隔符或行终止符打印
#改变print()函数输出数据的默认分隔符或终止符，可以使用sep和end关键字
print('ACME', 50, 91.5)
print('ACME', 50, 91.5,sep=',')
print('ACME', 50, 91.5,sep=',',end='!!\n')
#使用 end 参数也可以在输出中禁止换行。比如：
for i in range(5):
    print(i)
for i in range(5):
    print(i,end=' ')
#有时候你会看到一些程序员会使用str.join()来完成和sep同样的事
print(','.join(('ACME','50','91.5')))#注意：str.join()仅适用于字符串，即列表元素必须为字符串。不然会报错
row=('ACME', 50, 91.5)
print(','.join(str(x) for x in row))#correct
#print(','.join(row))#error
#也可以像下面这样简洁一点
print(*row,sep=',')
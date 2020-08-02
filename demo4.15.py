#顺序迭代合并后的迭代对象
import heapq
a=[1,4,7,10]
b=[2,5,8,11,15,18,20]
for c in heapq.merge(a,b):
    print(c)
#heapq.merge()的特性是他不会立马读取所有序列。这意味这你可以在很长的序列中使用他而不会有太大的开销
#example
with open('d:/python work/sorted_file_1.txt', 'rt') as f1,\
     open('d:/python work/sorted_file_2.txt', 'rt') as f2,\
     open('merged_file', 'wt') as f3:
    for line in heapq.merge(f1,f2):
        f3.write(line)
#强调：heapq.merge()需要所有的输入序列必须是排过序的。
#他不会预先读取所有数据到堆栈中或者预先排序，也不会对输入做任何检测。他仅仅检查序列开头部分并返回最小的那个，知道序列中所有元素被遍历
#如果是输入没排序的序列，结果会怎么样
print('-'*50)
c=[5,4,6,9,2,44,33]#如果没排序，则输出元素也不会排序
d=[1,3,8,66,99]
for m in heapq.merge(c,d):
    print(m)
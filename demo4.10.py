#序列上索引值迭代
#内置函数enumerate()
from collections import defaultdict
my_list=['a','b','c']
for idx,val in enumerate(my_list):
    print(idx,val)
#在遍历文件时想在错误消息中使用行号定位，这个函数非常有用
def parse_data(filename):
    with open(filename,'rt') as f:
        for lineno,line in enumerate(f,1):
            field=line.split()
            try:
                count=int(field[0])
            except ValueError as e:
                print('line{}:parse_error:{}'.format(lineno,line))
fn='e:/test1.txt'
parse_data(fn)
#将一个文件中出现的单词映射到他对应的行号上
word_summary=defaultdict(list)
with open(fn,'r') as f:
    lines=f.readlines()
for idx,line in enumerate(lines,1):
    words =[w.strip().lower() for w in line.split()]#strip():用于移除字符串前后指定字符.split():通过指定分隔符对字符串切片
    for word in words:
        word_summary[word].append(idx)
print(word_summary)
#enumerate()返回一个enumerate对象实例，他是一个迭代器
#当你在一个已经解压后的元组序列上使用 enumerate() 函数时很容易调入陷阱。注意下例
data=[(1,2),(3,4),(5,6),(7,8)]
#correct
for n,(x,y) in enumerate(data):
    print('no{}:{}'.format(n,(x,y)))
#error
for n,x,y in enumerate(data):
    pass
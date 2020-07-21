#通过某个字段将记录分组
rows = [
    {'address': '5412 N CLARK', 'date': '07/01/2012'},
    {'address': '5148 N CLARK', 'date': '07/04/2012'},
    {'address': '5800 E 58TH', 'date': '07/02/2012'},
    {'address': '2122 N CLARK', 'date': '07/03/2012'},
    {'address': '5645 N RAVENSWOOD', 'date': '07/02/2012'},
    {'address': '1060 W ADDISON', 'date': '07/02/2012'},
    {'address': '4801 N BROADWAY', 'date': '07/01/2012'},
    {'address': '1039 W GRANVILLE', 'date': '07/04/2012'},
]
from operator import itemgetter
from itertools import groupby
from collections import defaultdict
print(list(groupby(rows,key=itemgetter('date'))))#output a itertools.groupby object.[(key,_grouper),(key,_grouper)...]的序列_grouper即rows中的每个字典
#未排序前
print('未排序前-----------------')
for date,items in groupby(rows,key=itemgetter('date')):
    print(date)
    for i in items:
        print(' ',i)
#排序后
print('排序后-----------------')
rows.sort(key=itemgetter('date'))
print(rows)
for date,items in groupby(rows,key=itemgetter('date')):
    print(date)
    for i in items:
        print(' ',i)
#构建一个多值字典，根据date来查询
row_by_date=defaultdict(list)
for row in rows:
    row_by_date[row['date']].append(row)
for i in row_by_date['07/01/2012']:
    print(i)
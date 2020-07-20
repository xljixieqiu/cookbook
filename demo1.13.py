#通过某个关键字排序一个字典列表
from operator import itemgetter
rows=[
{'fname':'Brian','lname':'Jones','uid':1003},
{'fname':'David','lname':'Beazley','uid':1002},
{'fname':'John','lname':'Cleese','uid':1001},
{'fname':'Big','lname':'Jones','uid':1004}
]
rows_by_fname=sorted(rows,key=itemgetter('fname'))
rows_by_uid=sorted(rows,key=itemgetter('uid'))
print(rows_by_fname)
print(rows_by_uid)
#itemgetter也支持多个key
rows_by_lfname=sorted(rows,key=itemgetter('lname','fname'))
#itemgetter()有时候也可以被lambda代替，但是itemgetter()速度稍微快点
'''
rows_by_fname=sorted(rows,key=lambda k:k['fname'])
rows_bu_flname=sorted(rows,key=lambda k:(k['fname'],k['lname']))
'''
#同样也适用于min()和max()
min_row=min(rows,key=itemgetter('uid'))
max_row=max(rows,key=itemgetter('uid'))
print(min_row)
print(max_row)
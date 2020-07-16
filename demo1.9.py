#查找字典相同点
a={'x':1,'y':2,'z':3}
b={'w':11,'x':12,'y':2}
print(a.keys()&b.keys())#output ｛'x','y'}
print(a.keys()-b.keys())#output ｛'z'｝
print(a.items()&b.items())#output {'y':2}
c={key:a[key] for key in a.keys()-{'z','w'}}
print(c)#output {'x':1,'y':2}

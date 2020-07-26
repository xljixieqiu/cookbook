#代理迭代
class Node:
    def __init__(self,value):
        self._value=value
        self._children=[]
    def __repr__(self):
        return 'Node({!r})'.format(self._value)
    def add_child(self,node):
        self._children.append(node)
    def __iter__(self):
        return iter(self._children)#__iter__()方法必须返回迭代类型，所以前面要加个iter().否则会报错TypeError: iter() returned non-iterator of type 'list'
#example
if __name__=='__main__':
    root=Node(0)
    child1=Node(1)
    child2=Node(2)
    print(root.__iter__())
    print('for start')
    for i in root.__iter__():
        print(i)
    print('for end')
    print(root._value)
    root.add_child(child1)
    root.add_child(child2)
    print('root:',root)
    print(root.__iter__())
    for ch in root:#直接 for in root为什么会执行__iter__()?
        print(ch)
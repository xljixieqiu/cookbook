#实现迭代器协议
#一个以深度优先方式遍历树形节点的生成器
import os
class Node:
    def __init__(self,value):
        self._value=value
        self._children=[]
    def __repr__(self):
        return 'Node({!r})'.format(self._value)
    def add_child(self,node):
        self._children.append(node)
    def __iter__(self):
        return iter(self._children)
    def depth_first(self):
        yield self
        for c in self:
            yield from c.depth_first()
#example
root=Node(0)
child1=Node(1)
child2=Node(2)
child3=Node(3)
root.add_child(child1)
root.add_child(child2)
child1.add_child(child3)
child1.add_child(Node(4))
child2.add_child(Node(5))
child3.add_child(Node(6))
for i in root.depth_first():
    print(i)
'''
output
Node(0)
Node(1)
Node(3)
Node(6)
Node(4)
Node(2)
Node(5)
'''
#下面这个看不懂，放弃.头昏眼胀
class Node2:
    def __init__(self, value):
        self._value = value
        self._children = []

    def __repr__(self):
        return 'Node({!r})'.format(self._value)

    def add_child(self, node):
        self._children.append(node)

    def __iter__(self):
        return iter(self._children)

    def depth_first(self):
        return DepthFirstIterator(self)


class DepthFirstIterator(object):
    '''
    Depth-first traversal
    '''

    def __init__(self, start_node):
        self._node = start_node
        self._children_iter = None
        self._child_iter = None

    def __iter__(self):
        return self

    def __next__(self):
        # Return myself if just started; create an iterator for children
        if self._children_iter is None:
            print('1')
            self._children_iter = iter(self._node)
            return self._node
        # If processing a child, return its next item
        elif self._child_iter:
            print(2)
            try:
                nextchild = next(self._child_iter)
                print('try')
                return nextchild
            except StopIteration:
                self._child_iter = None
                print('except')
                return next(self)
        # Advance to the next child and start its iteration
        else:
            print(3)
            self._child_iter = next(self._children_iter).depth_first()
            return next(self)

root2=Node2(0)
c1=Node2(1)
c2=Node2(2)
root2.add_child(c1)
root2.add_child(c2)
c1.add_child(Node2(3))
c1.add_child(Node2(4))
c2.add_child(Node2(5))
for i in root2.depth_first():
    print(i)
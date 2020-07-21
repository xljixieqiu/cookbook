#排序不支持原生比较的对象
from operator import attrgetter
class User:
    def __init__(self,user_id):
        self.user_id=user_id
    def __repr__(self):
        return 'User({})'.format(self.user_id)
def sort_notcompare():
    users=[User(23),User(3),User(99)]
    print(users)
    print(sorted(users,key=lambda k:k.user_id))
#plan a
sort_notcompare()
#plan b
users=[User(23),User(33),User(99)]
print(sorted(users,key=attrgetter('user_id')))
#itemgetter 和 attrgetter的区别：itemgetter针对dict attrgetter针对 class。是否正确待定？？？
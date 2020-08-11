#demo7.8(1).py
#作为一个类似的例子，考虑下编写网络服务器的问题，socketserver模块让它变得很容易。下面是个简单的echo服务器：
from  socketserver import StreamRequestHandler,TCPServer
from functools import partial
'''
class EchoHandler(StreamRequestHandler):
    def handle(self):
        for line in self.rfile:
            self.wfile.write(b'GOT:'+line)

serv=TCPServer(('',15000),EchoHandler)
serv.serve_forever()
'''
#不过，假如你想给EchoHandler增加一个可以接受其他配置选项的__init__方法，比如：

class EchoHandler(StreamRequestHandler):
    def __init__(self,*args,ack,**kwargs):
        self.act=act
        super().__init__(*args,**kwargs)
    def handle(self):
        for lin in self.rfile:
            self.wfile.write(self.ack+line)

#这么修改好后，我们就不需要显式地在TCPServer类中添加前缀了。
#但是你再次运行程序后会报类似下面的错误：
'''
Exception happened during processing of request from ('127.0.0.1',59834)
Traceback (most recent call last):
....
TypeError:__init__() missing 1 required keyword-only argument:'ack'
'''
#初看起来好像很难修正这个错误，除了修改socketserver模块源代码或者使用某些奇怪的方法之外。
#但是，如果使用partial()就能很轻松的解决--给他传递ack参数的值来初始化即可，如下：
serv=TCPServer(('',15000),partial(EchoHandler,ack=b'RECEIVED:'))
serv.serve_forever()
#在这里例子中，__init__()方法中的ack参数声明方式看上去很有趣，其实就是声明ack为一个强制关键字参数。
#关于强制关键字参数问题我们在7.2小节已经讨论过了
#很多时候partial()能实现的效果，lambda表达式也能实现。比如，之前的几个例子可以使用下面这样的表达式：
serv=TCPServer((),lambda *args,**kwargs:EchoHandler(*args,ack='RECEIVED:',**kwargs))
#这样写也能实现同样的效果，不过相比而言会显得比较臃肿，对于阅读代码的人来讲也更加难懂。
#这时候使用partial()可以更加直观的表达你的意图（给某些参数预先赋值）

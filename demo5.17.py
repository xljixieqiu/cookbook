#将字节写入文本文件
#你想在文本模式打开的文件中写入原始的字节数据
#解决：将字节数据直接写入文件的缓冲区即可：例如
import sys
print(sys.stdout.buffer.write(b'Hello\n'))
#类似的，能够通过读取文本文件的buffer属性来读取二进制数据
#讨论
#I/O系统以层级结构的形式构建而成。文本文件是通过在一个拥有缓冲的二进制模式文件上增加一个unicode编码/解码层来创建。
#buffer属性指向对应的底层文件。如果你直接访问他的话就会绕过文本编码/解码层
#本小姐例子展示的sys.stdout可能看起来有点特殊。默认情况下sys.stdout总是以文本模式打开的。
#但是如果你在写一个需要打印二进制数据到标准输出的脚本的话，你可以使用上面演示的技术来绕过文本编码层

#找出一个序列中出现次数最多的元素 collections中Counter
from collections import Counter
words=['eye','eye','eye','eye','eye','eye','eye','look','look','look','look','look','into','into','into','my','my','youre','youre','have','beautiful','beautiful','beautiful','beautiful','beautiful','beautiful','good']
word_counts=Counter(words)
print(word_counts)#一个tuple对象
top_three=word_counts.most_common(3)#次数最多的3个词
print(top_three)#output a list
print(word_counts['eye'])#相当于tuple的使用方法
print(word_counts['look'])
morewords=['eye','look','my','youre','good','good','beautiful']
word_counts.update(morewords)#update()方法的使用。计数相加
print(word_counts)
a=Counter(words)
b=Counter(morewords)
c=a+b
d=a-b#如果为零则不再Counter中，不会出现负数（按零处理）
print(a)
print(b)
print(c)
print(d)

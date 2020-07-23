#从字典中提取子集
prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}
p1={key:value for key:value in prices.items() if value >200}
#p1=dict((key,value) for key,value in prices.items() if value >200) ~这种方法也可以，但效率比字典推倒慢一倍
print(p1)#output {'appl':612.78,'ibm':205.55}
tech_names={'AAPL', 'IBM', 'HPQ', 'MSFT'}
p2={key:value for key:value in prices.items() if key in tech_names}
#p2={key:prices[key] for key in prices.keys() & tech_names} ~这种方法也可以，但比前一种方案慢1.6倍
print(p2)#output apple,ibm,hpq
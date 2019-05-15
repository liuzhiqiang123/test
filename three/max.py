# 1.定义产品各项参数值，实现按参数名获得该参数值最高的一个产品型号
def searchMax(item):
    pro1={'product':'iphone xs','screen':5.8,'price':8699,'weight':'177克','depth':7.7}
    pro2={'product':'iphone xs Max','screen':6.5,'price':9599,'weight':'208克','depth':7.7}
    pro3={'product':'iphone xr','screen':6.1,'price':6499,'weight':'194克','depth':8.3}
    proList=[pro1,pro2,pro3]
    a=max(proList,key=lambda x:x[item])
    msg={'product':'产品','screen':'屏幕尺寸','price':'起价','weight':'重量','depth':'厚度'}
    print("您获取的参数信息是：",msg[item])
    return a

itemName=input("请输入要查找配置项最高的参数名称：")
productItem=searchMax(itemName)
print(productItem)
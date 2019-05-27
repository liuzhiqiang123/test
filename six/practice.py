# 1.循环嵌套的列表推导式
# a = [-3,5,2,-10,7,8]
# b = 'abc'
# d = [(x,y) for x in a
#      for y in b
#      if x > 0]
# print(d)

# 2.删除33和44
# data = [11,22,33,44,55,66,77,88,99]
# list_temp = []
# for i in data:
#     if i == 33 or i ==44:
#        list_temp.append(i)
#
# for i in list_temp:
#     if i ==33 or i == 44:
#         data.remove(i)
#
# print(data)
# 错误代码
# data = [11,22,33,44,55,66,77,88,99]
# for i in data:
#     if i == 33 or i == 44:
#         data.remove(i)
# print(data)

# 3.同时输出索引和元素
#第一种方法
# print("2018移动支付前四名")
# name = ['支付宝','财付通','云闪付','京东支付']
# i=1
# for item in name:
#     print('%d %s'%(i,item))
#     i += 1

#第二种方法
# print("2018移动支付前四名")
# name = ['支付宝','财付通','云闪付','京东支付']
# for index,item in enumerate(name):  #index保存元素的索引，item元素值
#     print(index+1,item)

# 4.
# 根据索引值实现同时迭代两个序列
# print("2018年世界杯最佳球员前五名：")
# num = [1,2,3,4,5]
# name = ['阿扎尔','梅西','伊斯科','内马尔','姆巴佩']
# for i in range(len(name)):
#     print(name[i],'\t第',num[i],'名')

#zip()函数同时迭代两个序列
# print("2018年世界杯最佳球员前五名：")
# num = [1,2,3,4,5]
# name = ['阿扎尔','梅西','伊斯科','内马尔','姆巴佩']
# for i,j in zip(name,num):
#     print(i,'\t第',j,'名')

# 5.生成1-10之间不重复的四位验证码
# import random   #导入随机数模块
# list1 = [x for x in range(1,10)]
# print(list1)
# list2 = random.sample(list1,4)  #从第一个列表中，随机取出4个不重复的
# list2 = [str(i) for i in list2] #将数值列表转换为字符串列表
# print(list2)
# print("生成的验证码为：","".join(list2))    #输出验证码

# 6.enumerate枚举
# seasons = ['Spring','Summer','Fall','Winter']
# print(list(enumerate(seasons)))
# print(list(enumerate(seasons,start=1))) # 下标从1开始
# print(enumerate(seasons))
# for index,item in enumerate(seasons):
#     print(str(index)+'->'+item)

#嵌套解包
# a,(b,c) = 1,(2,3)
# print('a=%s,b=%s,c=%s'%(a,b,c))
# a,*rest = [1,2,3]
# print('a=%s,rest=%s'%(a,rest))
# a,*middle,c = [1,2,3,4]
# print('a=%s,middle=%s,c=%s'%(a,middle,c))

# 7.
# d = "{'id':'1001','name':'无语','english':'99','python ':'100','c':'98'}"
# dict1 = dict(eval(d))   #转换为字典
# #dict1 = dict(d)   #转换为字典
# print('d的类型为：',type(d))
# print(dict1)
# print("dict1的类型为：",type(dict1))

# 8.
def rulesort(elem): #定义排序规则
    return elem['python']

list_dict = [{'name':'无语','python':99,'c':89},
             {'name': 'wgh', 'python': 100, 'c': 80},
             {'name': '琦琦', 'python': 95, 'c': 97},
             {'name': '明日', 'python': 91, 'c': 96},]
print("对列表排序前：")
for d in list_dict:
    print(d)
list_dict.sort(key = rulesort,reverse=True) #降序排列
print("对列表排序后：")
for d in list_dict:
    print(d)
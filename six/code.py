# 1.通过索引可以访问序列中的任何元素
# verse = ["圣安东尼奥马刺","洛杉矶湖人","休斯顿火箭","金州勇士"]
# print(verse[2]) #输出第3个元素
# print(verse[-1])    #输出最后一个元素
#
# # 2.通过切片获取列表n中的第2个到第5个元素，以及第一个、第三个和第五个元素
# n = ['0','1','2','3','4','5','6','7','8']
# print(n[1:5])   #获取第二个到第五个元素
# print(n[0:5:2]) #获取第一个、第三个、第五个元素
#
# # 3.使用n关键字检查某个元素是否是序列的成员
# nba = ["圣安东尼奥马刺","洛杉矶湖人","休斯顿火箭","金州勇士"]
# print("洛杉矶湖人" in nba)
#
# # 4
# num = [7,14,21,28,35,42,49,56,63]
# # 使用len()函数计算序列num的长度
# print("序列num的长度为",len(num))
# # 使用max()函数计算序列num的最大值
# print("序列",num,"中的最大值为",max(num))
# # 使用min()函数计算序列num的最小值
# print("序列",num,"中的最小值为",min(num))
#
# # 5.修改列表中的元素只需要通过索引获取该元素，然后再为其重新赋值
# nmn = ["圣安东尼奥马刺","洛杉矶湖人","休斯顿火箭","金州勇士"]
# nmn[1] = "森林狼"  #修改列表的第二个元素
# print(nmn)
#
# # 6.使用del语句删除列表中的指定元素
# dmn = ["圣安东尼奥马刺","洛杉矶湖人","休斯顿火箭","金州勇士"]
# del dmn[-1] #删除列表最后一个元素
# print(dmn)
#
# # 7.使用remove()方法删除元素前，最好先判断该元素是否存在
# fmn = ["圣安东尼奥马刺","洛杉矶湖人","休斯顿火箭","金州勇士"]
# value = "金州勇士"  #指定要移除的元素
# print(fmn.count(value))
# if fmn.count(value)>0:  #判断要删除的元素是否存在
#     fmn.remove(value)   #移除指定元素
# print(fmn)

# 8.sort()方法字符串列表的排序，需要先对大写字母进行排序，然后再对小写字母进行排序。
#如果想要对字符串列表进行排序（不区分大小写），需要指定key参数
# char = ['cat','Tom','Angela','pet']
# char.sort() #默认区分字母大小写
# print(char)
# char.sort(key=str.lower)    #不区分字母大小写
# print(char)

# 9.应用列表推到式生成一个将全部商品价格打5折的列表
# price = [1200,5330,2988,6200,1998,8888]
# sale = [int(x*0.5) for x in price]
# print(sale)
# sale2 = [x for x in price if x>5000]
# print(sale2)

# 11.使用元组推导式生成一个包含10个随机数的生成器对象，然后将其转换为元组
# import random
# randomnumber = (random.randint(10,100) for i in range(10))
# print(randomnumber)
# randomnumber = tuple(randomnumber)  #转换为元组
# print(randomnumber)

# 12.__next__()方法用于遍历生成器对象，通过生成器推导式生成一个包含3个元素的生成器对象number，
#然后调用3次__next__()方法输出每个元素
number = (i for i in range(3))
print(number.__next__())    #输出第一个元素
print(number.__next__())    #输出第二个元素
print(number.__next__())    #输出第三个元素

# 13.
number = (i for i in range(4))  #生成生成器对象
for i in number:    #遍历生成器对象
    print(i,end='') #输出每个元素的值
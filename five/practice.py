# # 1.%d主要用于对十进制整数进行格式化，%d表示原值输出
# print("%d"%2)
# print("%7d"%2)
# print("%-3d"%2)
# print("%005d"%2)
# print("%00007d"%2)

# # 2.%e科学计数法计算
# print("%f"%100000)
# # 3.%f按指定精确格式化浮点数（默认保留6位）
# print("%e"%100000)
# # 4.%g根据数值的大小采用%e或%f
# print("%g"%100000)
# print("%g"%1000000)

# 3.random模块
import random

#random.shuffle 重新随机排列数据，实现洗牌功能
list = [1,2,3,4,5,6]
random.shuffle(list)    #将数字1-6的顺次打乱
print(list)

#random.sample(seq,n) 从序列选择n个随机且不重复的元素
list = [1,2,3,4,5,6,7,8,9,0]
print(random.sample(list,5))

#random.choice(seq) 从列表中随机返回任意一个元素，输出元素不包含引号或双引号
print(random.choice(["a","b","c","d","e","f","g"]))

#random.randrange(start,stop,step)从指定范围内，获取一个随机数。范围包含首数start，不包含尾数stop,step为进步值、默认为1
print(random.randrange(1,10,2))

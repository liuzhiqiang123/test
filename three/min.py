# 1.随机生成10个1到100之间的数字，再取出这些数字中最小的值
# import random
# seq=[]
# i=0
# while i<10:
#     seq.append(random.randint(1,100)) #生成一个在1到100之间的随机数
#     i+=1
# getMin=min(seq)
# print("原列表值：",seq)
# print("列表最小值：",getMin)

# 2.利用min()实现一个序列的从小到大的排序

import random
seq=[]
i=0
while i<15:
    seq.append(random.randint(1,100))
    i+=1
print("原列表值：",seq)
newSeq=[]
while len(seq)>0:
    s=min(seq)
    newSeq.append(s)
    seq.remove(s) #移除s
print("列表最小值：",newSeq)
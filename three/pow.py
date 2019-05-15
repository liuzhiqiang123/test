# 1.编写一个进步累机器，实现每天进步一点点，计算一年提升的倍数
# import math
# def progress(val):
#     num = 1+val
#     yearProgress = math.pow(num,365)    #pow()计算num的365次方，math会把参数转换为float
#     output=""
#     if yearProgress==num:
#         output="原地踏步"
#     else:
#         output=str(round(yearProgress,1))
#     print("一年进步值:",output+"倍")
#
# dayVal = input("每天进步值：")
# progress(float(dayVal))

# 2.计算100-1000之间，哪些数的每一个数位上的3次方相加刚好等于该数
import math
def getPow():
    i = 100
    while i<1000:
        a=math.floor(i/100) #百位上的数#返回小于等于i/100的最大整数
        b=i%10 #个位上的数S
        c=(math.floor(i/10))%10 #十位上的数
        if(math.pow(a,3)+math.pow(b,3)+math.pow(c,3))==i:
            print(i)
        i+=1

getPow()
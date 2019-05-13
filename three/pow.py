# 1.编写一个进步累机器，实现每天进步一点点，计算一年提升的倍数
import math
def progress(val):
    num = 1+val
    yearProgress = math.pow(num,365)    #pow()计算num的365次方，math会把参数转换为float
    output=""
    if yearProgress==num:
        output="原地踏步"
    else:
        output=str(round(yearProgress,1))
    print("一年进步值:",output+"倍")

dayVal = input("每天进步值：")
progress(float(dayVal))
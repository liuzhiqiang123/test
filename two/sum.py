# # 1.计算出0到100（含100）之间所有偶数的和
#
# evenNumbers = []
# i = 0
# while i <= 100:
#     if i % 2 == 0:
#         evenNumbers.append(i)
#     i += 1
# print(sum(evenNumbers))
#
# # 2.计算二维序列中每个子序列的平均值以及整个序列的平均值
#
# def avg(seq):
#     totalLen = 0
#     everySeq = []
#     for s in seq:
#         Len = len(s)
#         everySeq.append(sum(s))
#         print(sum(s)/Len)
#         totalLen += Len
#     print(sum(everySeq)/totalLen)
#
# avg([[10,12,13],[12,11,15],[2,5,4,2]])

# 3.实现加减乘除计算器
class myCalc:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def addition(self,Retain):
        return round(self.a + self.b,Retain)
    def subtraction(self,Retain):
        return round(self.a - self.b,Retain)
    def multiplication(self,Retain):
        return round(self.a * self.b,Retain)
    def division(self,Retain):
        return round(self.a / self.b,Retain)

while 1:
    get_num1 = input("请输入第一个数字：")
    opera = input("请输入运算符：")
    get_num2 = input("请输入第二个数字：")
    get_retain = input("请输入保留的小数位数：")
    num1 = float(get_num1)
    num2 = float(get_num2)
    retain = int(get_retain)
    result = 0.00

    if opera == "+":
        result = myCalc(num1,num2).addition(retain)
    elif opera == "-":
        result = myCalc(num1,num2).subtraction(retain)
    elif opera == "*":
        result = myCalc(num1,num2).multiplication(retain)
    else:
        result = myCalc(num1,num2).division(retain)
    print("结果是：",result)
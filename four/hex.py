# # 1.创建自定义函数，实现RGB颜色赚十六进制颜色代码值
# def RgbTo16(num1,num2,num3):
#     num_16_1=hex(int(num1))
#     num_16_2=hex(int(num2))
#     num_16_3=hex(int(num3))
#     num_str1=str(num_16_1)
#     num_str2=str(num_16_2)
#     num_str3=str(num_16_3)
#     num_str=[num_str1[2:],num_str2[2:],num_str3[2:]]
#     return ''.join(num_str)
#
# while 1:
#     rValue=input("请输入RGB颜色值R：")
#     gValue=input("请输入RGB颜色值G：")
#     bValue=input("请输入RGB颜色值B：")
#     color16=RgbTo16(rValue,gValue,bValue)
#     print(rValue+','+gValue+','+bValue+'的16进制颜色值为：',color16)
######################拆分
# num_16_1=hex(255)
# print(num_16_1)
# num_16_2=hex(182)
# print(num_16_2)
# num_16_3=hex(193)
# print(num_16_3)
# num_str1=str(num_16_1)
# num_str2=str(num_16_2)
# num_str3=str(num_16_3)
# num_str=[num_str1[2:],num_str2[2:],num_str3[2:]]
# print(num_str)
# p=''.join(num_str)
# print(p)

# 2.实现可以回调的转换操作。通过hex()函数调用Calc对象实现将两个数相加后得到十六进制结果
# class Calc:
#     def __init__(self,num1,num2):
#         self.num1=num1
#         self.num2=num2
#         self.add()
#     def __index__(self):
#         return self.result
#     def add(self):
#         self.result=self.num1+self.num2
# s = Calc(5,10)
# print(hex(s))

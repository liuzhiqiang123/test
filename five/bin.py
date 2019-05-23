# # 1.输入的数字转换成二进制形式
# def compare2(c):
#     con2=bin(c) #bin()函数返回一个整数的二进制形式
#     return con2
#
# while 1:
#     getnum=input("请输入一个数字：")
#     print(compare2(int(getnum)))

# 2.
while 1:
    getnum = input("请输入一个数字：")
    try:
        g=int(getnum)
        print("您输入的是数字：",g)
    except:
        print('==您输入的不是数字==')
# 1.输出0到10的八进制表示形式
# i=0
# while i<11:
#     print(oct(i))
#     i+=1

# 2.实现键盘字符八进制对照表
import binascii
def compare8(c):
    con16=binascii.hexlify(c.encode("gbk")) #将c转换为二进制，并用十六进制表示
    con10=int(con16.upper(),16) #将con16转换为大写，16进制转为10进制
    con8=oct(con10)
    return con8

while 1:
    getchar=input("请输入一个有效的字符：")
    print(compare8(getchar))
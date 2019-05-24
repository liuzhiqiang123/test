# 1.自定义一个类，输出该类的字符串表示形式
# class A:
#     i=1
#     def fun(self):
#         i+=1
# print(str(A))

# 2.
def createList(listCount):
    list1=[]
    i=0
    while i<listCount:
        list1.append(i)
        i+=1
    return str(list1)

while 1:
    lastnum = input("请输入从0开始到生成该序列的总长度值：")
    int_lastnum=int(lastnum)
    strList=createList(int_lastnum)
    print("已生成从0到",int_lastnum-1,"的序列对象，该序列对象的字符串表示形式为：",strList)
# # 1.输出10行“*”，每行50个
# # print((50 * "*" + "\n")*10)
#
# # 2.在一行输出
# print('你热爱生活，',end="")
# print("生活也热爱你！")
#
# # 3.增强输出效果
# inputstr=input("请输入乘数：")
# suma=int(inputstr)
# inputstr=input("请输入乘数：")
# sumb=int(inputstr)
# Summul=suma*sumb
# Summul=str(Summul)
# print(str(suma) + "乘" + str(sumb) + "计算结果是：\n" + str(Summul))
# 4.输出居左、居中、居右
# ##函数实现
# print('明日'.ljust(20))
# print('明日'.rjust(20))
# print('明日'.center(20))
# print('|'+"明日".ljust(10)+"|"+"明日".rjust(10)+"|"+"明日".center(10)+"|")
##函数带参
# print('明日'.ljust(20,"*"))
# print('明日'.rjust(20,"*"))
# print('明日'.center(20,"*"))
# print('|'+"明日".ljust(10,"+")+"|"+"明日".rjust(10,"+")+"|"+"明日".center(10,"+")+"|")
##format()函数
print(format("明日","*>20"))
print(format("明日","*<20"))
print(format("明日","*^20"))
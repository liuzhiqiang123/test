# # 1.将120转化为二进制、八进制和十六进制
# a=120
# print(bin(a))   #二进制
# print(oct(a))   #八进制
# print(hex(a))   #十六进制
#
# # 2.Ob、Oo、Ox分别是二进制、八进制、十六进制的标志。可以用截取去掉标志
#
# a=120
# print(bin(a)[2:])   #二进制
# print(oct(a)[2:])   #八进制
# print(hex(a)[2:])   #十六进制

# 3.转换浮点型
# a = "2.3"
# floata = float(a)
# print(floata)
#
# # 4.float()函数不写参数，返回值为0.0
# print(float())
#
# # 5.float()函数表示无穷大、无穷小和nan数（没有值）
# print(float("+infinity"))
# print(float("-infinity"))
# print(float("nan"))
#
# # 6.type()判断变量、常量类型
# a = "2.3"
# print(type(a))
# print(type(10))
#
# # 7.int()函数
# #将二进制转换为十进制输出
# print(int("111",2)) #2表示进制的参数，可以为2-36.不写参数或者参数为0表示十进制
#
# #十进制
# print(int("111"))
# print(int("111",0))

# 8.输出当前日期
import datetime
print((datetime.date.today()))  #输出当前日期（到日）

print(datetime.datetime.today())    #输出当前日期和时间
print(datetime.datetime.now())    #输出当前日期和时间

print(datetime.datetime.now().strftime('%Y-%m-%d'))
print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S %A'))
print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S %a'))

#输出年月日时分秒星期月份
print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S %A %B'))
print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S %A %b'))

#计算时间差
day20 = datetime.datetime.strptime('2020-1-1 0:0:0','%Y-%m-%d %H:%M:%S')
now = datetime.datetime.now()
delta = day20-now   #两个时间的差，精确到毫秒
day = delta.days    #两个时间的差，天数
print(delta)
print(day)
print(delta.seconds)    #时分秒转换为秒
hour = int(delta.seconds/60/60) #int把小时取整
minute = int((delta.seconds-hour*60*60)/60) #int把小时取整
second = delta.seconds-hour*60*60-minute*60 #int把小时取整
print('到2020年元旦还有：'+str(day)+"天"+str(hour)+'小时'+str(minute)+'分钟'+str(second)+'秒')

#计算将来、过去的时间
print(datetime.datetime.now())
print(datetime.datetime.now() + datetime.timedelta(days = 5))   #5天后的时间
print(datetime.datetime.now() - datetime.timedelta(days = 5))   #5天前的时间
print(datetime.datetime.now() + datetime.timedelta(hours = 300))
print(datetime.datetime.now() + datetime.timedelta(minutes = 3000))

#格式化输出时间
mtime=datetime.datetime.now()
print(mtime.strftime('%Y-%m-%d'))
print(mtime.strftime('%Y-%m-%d %H:%M'))
print(mtime.strftime('%Y-%m-%d %H:%M:%S'))
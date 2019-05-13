# 1.通过ASCII码显示字符，需要chr()函数进行转换
# 输出字符a
print(chr(97))

# 2.打印汉字可以直接使用U+编码的形式
# 输出字符“生化危机”
print("\u751f\u5316\u5371\u673a")

# 3.使用print可以输出到指定文件
fp = open(r'D:\mr.txt','a+')    # 打开文件
print("要么出众，要么出局。",file=fp) #输出到文件中
fp.close()  #关闭文件

# 4.调用datetime模块，输出当前年份、月份和日期
import datetime #调用日期模块datetime
print('当前年份：'+str(datetime.datetime.now().year))    #输出当前年份
print('当前日期时间：'+datetime.datetime.now().strftime('%y-%m-%d %H:%M:%S'))
# 输出当前日期和时间，注意代码中的单引号，大小写不能写错

# 5.获得字符对应的ASCII码
name = input("输入字符：")   #输入字母或数字，不能输入汉字
print(name + "的ASCII码为：",ord(name)) #显示字符对应的ASCII码值
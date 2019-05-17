# 1.创建一个整型变量，并为其赋值为505
number = 505

# 2.直接为变量赋值一个字符串值
myname="生化危机"

# 3.用type()函数输出该变量的类型
myname="生化危机"
print(type(myname))

# 4.用id()函数获取变量的内存地址
no = number = 2048
print(id(no))
print(id(number))

# 5.根据身高、体重计算BMI指数
height = 1.70
weight = 48.5
bmi = weight/(height*height)
print("您的BMI指数为："+str(bmi))

# 6.引用字符串的三种引号形式
title='单引号，字符串内容必须在一行'
mot_cn="双引号，字符串内容必须在一行"
mot_en='''三引号，字符串内容可以分布在多行'''

# 7.累加商品总金额，转换类型
money_all=56.76+54.23+98.1
money_all_str = str(money_all)
print(money_all_str)
money_real = int(money_all)
print(money_real)
money_real_str = str(money_all)

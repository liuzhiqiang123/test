# 1.计算字符串重复指定次数
print('M'*10)

# 2.计算学生3门课程成绩分数差和平均分
python = 95
english = 92
c = 89
sub = python - english
avg = (python+english+c)/3
print("python课程和c课程的分数差："+str(sub)+"分\n")
print("3门课程平均分："+str(avg)+"分")

# 3.逻辑运算编写手机店打折活动
strWeek = input("请输入中文星期（如星期）")
intTime = int(input("请输入时间中的小时（范围：0-23）："))
# 判断是否满足活动参与条件
if (strWeek == "星期二" and (intTime >= 10 and intTime <= 11))\
    or (strWeek == "星期五" and (intTime >= 14 and intTime <= 15)):
    print("恭喜您，获得了折扣活动参与资格，快快选购吧！")
else:
    print("对不起，您来晚一步，期待下次活动......")
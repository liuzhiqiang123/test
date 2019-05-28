# 1.拼接字符
# mot_en = "拼接字符串"
# mot_cn = "pinjie"
# print(mot_cn+mot_en)

# 2.str()转换为字符串
# str1 = "今天我一共走了"
# num = 1029
# str2 = "步"
# print(str1+str(num)+str2)

# 3.len()计算字符串长度
# str1 = '人生苦短，我用python'
# length = len(str1)
# print(length)

# 4.
# str1 = '人生苦短，我用python'
# length = len(str1.encode()) # 计算utf-8编码的字符串长度
# print(length)

# 5.
# str1 = '人生苦短，我用python'
# length = len(str1.encode('gbk')) # 计算gbk编码的字符串长度
# print(length)

# 6.切片截取不同长度的字符串
# str1 = '人生苦短，我用python'
# substr1 = str1[1]
# print(substr1)
# substr2 = str1[5:]
# print(substr2)
# substr3 = str1[:5]
# print(substr3)
# substr4 = str1[2:5]
# print(substr4)

# 7.
# str1 = '明 日 学 院 官 网 >>> www.mingrisoft.com'
# # print('原字符串：',str1)
# # list1 = str1.split()    # 采用默认分隔符进行分割
# # list2 = str1.split('>>>')   #采用多个字符进行分割
# # list3 = str1.split('.') #采用.号进行分割
# # list4 = str1.split(' ',4)   #采用空格进行分割，并且只分割前4个
# # print(str(list1) + '\n' + str(list2) + '\n' + str(list3) + '\n' + str(list4))
# # list5 = str1.split('>') #采用>进行分割
# # print(list5)

# 8.count()计算次数
# str1 = '@明日科技@扎克伯格@雷军'
# print('字符串“',str1,'”中包括',str1.count('@'),'个@符号')

# 9.
# str1 = '@明日科技@扎克伯格@雷军'
# print('字符串“',str1,'”中@符号首次出现的位置索引为：',str1.find('@'))

# 10.
# str1 = '@明日科技@扎克伯格@雷军'
# print('字符串“',str1,'”中@符号首次出现的位置索引为：',str1.index('@'))

# 11.
# str1 = '@明日科技@扎克伯格@雷军'
# print('判断字符串“',str1,'”是否以@符号开头，结果为：',str1.startswith('@'))

# 12.
# str1 = 'http://www.mingrisof.com'
# print('判断字符串“',str1,'”是否以.com结尾，结果为：',str1.endswith('.com'))

# 13.
# str1 = 'WWW.mingrisof.com'
# print('原字符串：',str1)
# print('新字符串：',str1.lower()) #转换为小写输出

# 14.
# str1 = 'WWW.mingrisof.com'
# print('原字符串：',str1)
# print('新字符串：',str1.upper()) #转换为大写输出

# 15.
# str1 = 'http://www.mingrisof.com  \t\n\r'
# print('原字符串str1:'+str1)
# print('字符串:'+str1.strip())  #去除字符串首尾的空格和特殊字符
# str2='@明日科技.@.'
# print('原字符串str2:'+str2)
# print('字符串：'+str2.strip('@.'))  #去除字符串首尾的@或者.

# 16.
# str1 = '\t http://www.mingrisof.com'
# print('原字符串str1:'+str1)
# print('字符串:'+str1.lstrip())  #去除字符串左侧的空格和制表符
# str2='@明日科技'
# print('原字符串str2:'+str2)
# print('字符串：'+str2.lstrip('@.'))  #去除字符串左侧的@

# 17.
# str1 = ' http://www.mingrisof.com\t'
# print('原字符串str1:'+str1)
# print('字符串:'+str1.rstrip())  #去除字符串右侧的空格和制表符
# str2='明日科技，'
# print('原字符串str2:'+str2)
# print('字符串：'+str2.rstrip('，'))  #去除字符串右侧的@

# 18.
# template = '编号：%09d\t公司名称： %s \t 官网： http://www.%s.com' #定义模板
# context1 = (7,'百度','baidu') #定义要转换的内容1
# context2 = (8,'明日学院','mingrisoft')  #定义要转换的内容2
# print(template%context1)    #格式化输出
# print(template%context2)    #格式化输出

# 19.
# template = '编号：{:0>9s}\t 公司名称： {:s} \t 官网： http://www.{:s}.com' #定义模板
# # context1 = template.format('7','百度','baidu') #定义要转换的内容1
# # context2 = template.format('8','明日学院','mingrisoft')  #定义要转换的内容2
# # print(context1)    #格式化输出
# # print(context2)    #格式化输出

# 20.匹配字符串是否以'mr_'开头，不区分大小写
# import re
# pattern = r'mr_\w+' #模式字符串
# string = 'MR_SHOP mr_shop'  #要匹配的字符串
# match = re.match(pattern,string,re.I)   #匹配字符串，不区分大小写
# print(match)    #输出匹配结果
# string = '项目名称 MR_SHOP mr_shop'
# match = re.match(pattern,string,re.I)   #匹配字符串，不区分大小写
# print(match)

# 21.
import re
pattern = r'mr_\w+' #模式字符串
string = 'MR_SHOP mr_shop'  #要匹配的字符串
match = re.match(pattern,string,re.I)   #匹配字符串，不区分大小写
print('匹配值的起始位置：',match.start())
print('匹配值的结束位置：',match.end())
print('匹配位置的元组：',match.span())
print('要匹配的字符串：',match.string)
print('匹配数据：',match.group())

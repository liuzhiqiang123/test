# 1.
# for i in [1,2,3,4,5,6]:
#     print("笑傲江湖")
# 2.
# for i in [2,3,5,9,4]:
#     print(i)
# for i in ['明日','科技','与您','同行']:
#     print(i)

# 3.
# print('计算1+2+3+...+100的结果为：')
# result = 0
# for i in range(101):
#     result += i
# print(result)

# 4.
# for i in range(1,10,2):
#     print(i,end=' ')

# 5.
# string = '不要再说我不能'
# print(string)   #横向显示
# for ch in string:   # 纵向显示
#     print(ch)

# 6.
# i = 1
# while i <= 6:
#     print('笑傲江湖')
#     i = i+1

# 8.
# print('开始')
# none = True
# number = 0
# while none:
#     number += 1
#     if number%3 == 2 and number%5 == 3 and number%7 == 2:
#         print(number)
#         none = False

# 9.
# total = 99
# for number in range(1,100):
#     if number % 7 == 0:
#         continue
#     else:
#         string = str(number)
#         if string.endswith('7'):
#             continue
#     total -= 1
# print('从1数到99共拍腿',total,'次')
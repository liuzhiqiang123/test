# 2.
# number = int(input('请输入商品7天销量：'))
# if number >= 1000:
#     print('本商品7天销量为A！！')
# else:
#     if number >= 500:
#         print('本商品7天销量为B！！')
#     else:
#         if number >= 300:
#             print('本商品7天销量为C！！')
#         else:
#             print('本商品7天销量为D！！')

# 3.
# print('今有物不知其数，三三数之剩二，五五数之剩三，七七数之剩二，问几何？\n')
# number = int(input("请输入您认为符合条件的数："))
# if number%3 == 2 and number%5 == 3 and number%7 == 2:
#     print(number,'符合条件')

# 4.
# sales = int(input('请输入商品日销量：'))
# if sales < 10 or sales > 100:
#     print('该商品为重点关注商品')

# 5.if not 表示表达式为False时才执行
# data = None #代码并未为data赋值，所以data是空值，即data为False
# if not data:
#     print('you lost')
# else:
#     print('you win')

# 6.
a = input('请输入1位数字密码：')
b = ['0','1','2','3','4','5','6','7','8','9']
if a not in b:
    print('非法输入')
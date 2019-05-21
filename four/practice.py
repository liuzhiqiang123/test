# 1.将120转化为二进制、八进制和十六进制
a=120
print(bin(a))   #二进制
print(oct(a))   #八进制
print(hex(a))   #十六进制

# 2.Ob、Oo、Ox分别是二进制、八进制、十六进制的标志。可以用截取去掉标志

a=120
print(bin(a)[2:])   #二进制
print(oct(a)[2:])   #八进制
print(hex(a)[2:])   #十六进制
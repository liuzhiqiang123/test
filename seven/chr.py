# 1.chr()和ord()实现将一个字符串中的每一个字母向前推到一个字母
result = []
s = 'bcdefghijk'
for i in s:
    up = chr(ord(i)-1)
    result.append(up)
print(''.join(result))
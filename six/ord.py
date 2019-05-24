def Validate_is_Number(val):
    getASCII = ord(val)
    if getASCII >=48 and getASCII <= 57:
        return True
    else:
        return False

while 1:
    getnum = input("请输入一个有效的数字")
    Is_Number = Validate_is_Number(getnum)
    if Is_Number:
        print("您输入的是数字：",getnum)
    else:
        print("您输入了非法字符，这里只能输入数字")
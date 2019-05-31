#
en = bytearray('abc','utf-8')
cn = bytearray('中文','utf-8')
with open('test_bytearray.txt','wb') as fileInfo:
    fileInfo.write(en)
    fileInfo.write(cn)
with open('test_bytearray.txt','rb') as fileInfo:
    stream = fileInfo.read()
    print('原字节',stream)
    txtContent = str(stream,encoding='utf-8')
    print('字节转字符串',txtContent)
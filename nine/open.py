#
class operatxt():
    def __init__(self,encoding):
        self.enc = encoding
    def WriteTxt(self,s):
        with open('test.txt','a+',encoding=self.enc) as fileInfo:
            fileInfo.write(s)
    def ReadTxt(self):
        with open('test.txt','r',encoding=self.enc) as fileInfo:
            s = fileInfo.read()
            return s

while 1:
    content = input('请输入要写入到文件的内容：')
    ot = operatxt('utf-8')
    ot.WriteTxt(content)
    yn = input('内容已写入，书否读取？y，n')
    if yn == 'y':
        s = ot.ReadTxt()
        print('文件内容为：',s)
        break
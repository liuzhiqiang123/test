#
def languageBook(key):
    languageDict = dict(python = 57.90,java = 50.60, php = 74.50,aspnet = 83.80)
    #print(languageDict)
    seriesDict = dict([('pythonSeries','零基础学python'),
                      ('javaSeries','零基础学java'),
                      ('phpSeries','PHP从入门到精通'),
                      ('aspnetSeries','net从入门到精通')])
    #print(seriesDict)
    price = languageDict[key]
    series = seriesDict[key+'Series']
    return (price,series)

while 1:
    bookName = input('请输入书名：')
    getBookInfo = languageBook(bookName)
    print(getBookInfo)
    print(bookName,'价格',getBookInfo[0],'图书全称',getBookInfo[1])
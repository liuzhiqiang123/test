# 1.
convertList = [1,0,-1,'','abc',[],(1,2,3)]
resultList = []
for item in convertList:
    result = bool(item)
    resultList.append(result)

print("原数据为：",str(convertList))
print("转换结果为：",str(resultList))
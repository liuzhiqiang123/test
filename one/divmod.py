# divmod获取商和余数的元祖
# 1.计算出从参数N开始，向下递减的每一个数字和参数A的除数及余数的结果值

def getDivmod(A,N):
    while N >= 0:
        sn = str(N)
        sa = str(A)
        result = ['divmod({0},{1}):'.format(sn,sa),str(divmod(N,A))]
        print(''.join(result))
        #print(result)
        N = N - 1

getDivmod(3,10)

#print(divmod(10,3))

# 2.模拟实现数据分页计算方法
def getSegment(curIndex,getSize):
    abc = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    stratGet = (curIndex - 1) * getSize #5
    getData = abc[stratGet:curIndex * getSize] #5:10 ["f","g","h","i","j"]
    totalIndexTuple = divmod(len(abc),getSize) #(5,1)
    totalIndex = totalIndexTuple[0] + totalIndexTuple[1]#6
    return (getData,totalIndex)

result = getSegment(2,5)
print(result[0]) #['f','g','h','i','j']
print(result[1]) #6
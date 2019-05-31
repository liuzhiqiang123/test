#
def UpdateTuple(tuple_value,tIndex,val):
    newList = list(tuple_value)
    newList[tIndex] = val
    return tuple(newList)

setTuple = ('java','.net','c++','php','python2.x')
print('转换前',str(setTuple))
ConvertResult = UpdateTuple(setTuple,4,'python3.x')
print('转换后',str(ConvertResult))
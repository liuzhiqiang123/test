# 1.循环输出列表中定义的数字绝对值

def getDivmod(A,N):
    while N >= 0:
        sn = str(N)
        sa = str(A)
        result = ['divmod({0},{1}):'.format(sn,sa),str(divmod(N,A))]
        print(''.join(result))
        N = N - 1

getDivmod(3,10)

#print(divmod(10,3))
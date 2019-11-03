def findMinAndMax(L):
    if len(L) == 0:
        return (None,None)

    else:
        for i in range(len(L)-1):
            for j in range((len(L)-i-1)):
                if L[j] > L[j+1]:
                    tempo = L[j]
                    L[j] = L[j+1]
                    L[j+1] = tempo

    return (L[0], L[-1])
# 测试
if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')
def findMinAndMax2(L):
	if L !=[]:
		(min,max)=(L[0],L[0])
		for x in L:
			if max<x:
				max=x
			if min>x:
				min=x
		return(min,max)
	else:
		return(None,None)




if findMinAndMax2([]) != (None, None):
    print('测试失败!')
elif findMinAndMax2([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax2([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax2([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')

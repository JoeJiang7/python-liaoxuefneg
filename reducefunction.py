from functools import reduce
def prod(L):
    def multi(x,y):
        return x*y
    final = reduce(multi,L)
    return final
l1 = [3, 5, 7, 9]
print(prod(l1))
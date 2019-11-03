from functools import reduce

def str2floats(s):
    def find(list, a):
        for i in range(0,len(list)):
            if list[i] == a:
                return i
        else:
            return None
    dot = find(s,'.')
    def char2num(s):
        digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
        return digits[s]
    def fn1(x,y):
        return x*10+y
    def fn2(x,y):
        return x*0.1+y
    s1 = s[:dot]
    s2 = s[(dot+1):]
    s2 = s2[::-1]
    a1 = reduce(fn1,map(char2num,s1))
    a2 = reduce(fn2,map(char2num,s2))
    return a1+0.1*a2
print(str2floats('2334.56'))
   
import math
def quadratic(a, b, c):
    if (b**2-4*a*c) >= 0:
        d = math.sqrt(b ** 2 - 4 * a * c)
        x1 = (-b + d) / 2 * a
        x2 = (-b - d) / 2 * a
        return x1, x2

    else:
        print('测试失败')




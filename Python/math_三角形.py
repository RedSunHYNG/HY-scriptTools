import math

def is_triangle(a, b, c):
    return a + b > c and a + c > b and b + c > a

def judge_triangle_type(a, b, c):
    # 首先判断是否为三角形
    if not is_triangle(a, b, c):
        return "输入的三个数不能构成三角形"

    # 判断是否为等边三角形
    if a == b == c:
        return "等边三角形"

    # 判断是否为等腰三角形
    if a == b or a == c or b == c:
        return "等腰三角形"

    # 判断是否为直角三角形
    if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
        return "直角三角形"

    # 否则为一般三角形
    return "一般三角形"

# 测试
a = float(input("请输入三角形的第一条边长: "))
b = float(input("请输入三角形的第二条边长: "))
c = float(input("请输入三角形的第三条边长: "))

print(judge_triangle_type(a, b, c))
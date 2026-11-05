#s2-9最大公约数和最小公倍数
x = eval(input("请输入一个整数"))
y = eval(input("请输入另一个整数"))
m, n = x, y   #保存到m和n
if x < y: 
    x,y = y,x
r = x % y      #r为余数
# 请在下面编写代码
# ********** Begin ********** #
while True:
    if r!=0:
        x=y
        y=r
        r=x%y
    else:
        break
    
# ********** End ********** #
# 请不要修改下面的代码
print("\n最大公约数{} 最小公倍数{}".format(y,m*n/y))  
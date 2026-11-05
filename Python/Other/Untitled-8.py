# s2-6输出3、5、7的公倍数
n = int(input(''))
# 请在下面编写代码
# ********** Begin ******** #
m=0
while m<n:
    m=m+1
    a=m%3
    b=m%5
    c=m%7
    d=a+b+c
    if d==0:
        print(m)
# ********** End ********** #
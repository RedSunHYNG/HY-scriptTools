# -*- coding: utf-8 -*-

# 输入两个正整数a,b
a = int(input())
b = int(input())

# 请在此添加代码，求两个正整数的最大公约数
########## Begin ##########
def gcd(a,b):
    r=1
    minn=0
    maxn=0
    if r!=0:
        if b<a:
            a=a+b
            b=a-b
            a=a-b
        r=b%a
        if r==0:
            rl=0
        else:
            rl=b%r
        while rl!=0:
            ra=rl
            rl=r%rl
            r=ra
        maxn=r
    if maxn!=0:
        minn=a*b/maxn
    else:
        minn=a*b/a
        maxn=a
    return maxn,minn
#g=gcd(a,b)[0]
#lcm=gcd(a,b)[1]
#lcm=int(lcm)

tu=gcd(a,b)
g=tu[0]
lcm=int(tu[1])

#x=a
#y=b
#a=gcd(x,y)[0]
#b=gcd(x,y)[1]
#g=a
#lcm=int(b)
########## End ##########

# 调用函数，并输出最大公约数
print('最大公约数{} 最小公倍数{}'.format(g,lcm))

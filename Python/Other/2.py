# -*- coding: utf-8 -*-

# 第一题 请在此添加函数定义代码
########## Begin ##########
def add(x,y):
    return x+y

########### end ###########
x = eval(input())
y = eval(input())
print('{}+{}={}'.format(x,y,add(x,y)))


# 第二题 请在此添加函数定义代码
########## Begin ##########
def summ(n):
    i=0
    sum=0
    while i<=n:
        sum=sum+i
        i=i+1
    return sum


########### end ###########
n = eval(input())
print('1+...+{}={}'.format(n,summ(n)))


# 第三题 请在此添加函数定义代码
########## Begin ##########
def fac(n):
    i=n
    sum=1
    while i!=0:
        sum=sum*i
        i=i-1
    return sum


########### end ###########
n = eval(input())
print('{}!={}'.format(n,fac(n)))
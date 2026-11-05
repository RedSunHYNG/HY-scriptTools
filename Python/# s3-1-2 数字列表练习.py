# s3-1-2 数字列表练习
ls = input()
ls = ls.split()
ls = [int(x) for x in ls]   #列表推导式

lt = input()
lt = lt.split()
lt = [int(x) for x in lt]
######## 补充代码开始 #########
n=len(ls)
m=len(lt)
i=0
s=0
if n>=m:
    n=m
while i<n:
    s=s+ls[i]*lt[i]
    i=i+1
    
######## 补充代码结束 #########
print('两个列表对应元素乘积的和是{}'.format(s))
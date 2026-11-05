# s3-1数字列表练习
ls = input()
ls = ls.split()
ls = [int(x) for x in ls]   #列表推导式

#第一题
######## 第一题补充代码开始 #########
n=0
total=0
while n<len(ls):
    total=total+ls[n]
    n=n+1
######## 第一题补充代码结束 #########
print('列表元素和={}'.format(total))
print('----以上是第1题输出----')

#第二题
######## 第二题补充代码开始 #########
m=0
a=0
ls2=[]
while m<len(ls):
#    a=ls[m]%2
    a=m%2
    if a!=0:
#    if a==0:
        b=ls[m]*2
    else:
        b=ls[m]
    ls2.append(b)
    m=m+1
######## 第二题补充代码结束 #########
print(ls2)
print('----以上是第2题输出----')
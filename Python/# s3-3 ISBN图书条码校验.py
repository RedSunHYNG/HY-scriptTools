# s3-3 ISBN图书条码校验
isbn = list(input())  #输入ISBN号码,并转化为字符串列表
########## 补充代码开始 ##########
n=0
m=1
i=0
sum=0
num=0
while i<6:
    sum=sum+int(isbn[n])
    num=num+int(isbn[m])
    n=n+2
    m=m+2
    i=i+1
r=(sum+num*3)%10
r=(10-r)%10
if r==int(isbn[12]):
    print('ISBN号码正确')
else:
    print('ISBN号码错误')

########## 补充代码结束 ##########
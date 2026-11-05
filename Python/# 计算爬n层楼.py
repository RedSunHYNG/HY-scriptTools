# 计算爬n阶阶梯 ，每次爬2阶或1阶
import math
#m*1+n*2=45 n>0 m>0 i
i=0
n=45
#111 12 /1111 112 22 /11111 1112 122 /111111 11112 1122 222
for m in range (0,n+1):
    s=0
    while s<=n:
        for j in range(0,n+1):
            s=m+j*2
#            print(m,j,s)
            if s==n:
                if m!=0 and j!=0:
                    a=math.factorial(m+j)
                    b=math.factorial(m)*math.factorial(j)
                    c=a/b
                    i=i+c
                else:
                    i=i+1
print(int(i))


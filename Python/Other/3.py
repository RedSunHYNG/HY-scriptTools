# coding=utf-8
m = eval(input())  #输入判定范围

# 请在此添加代码，定义判断素数函数
###### Begin ######
def isprimary(n):
    i=2
    if n==2:
        print('2')
    else:
        print('2')
        while 2<=i<n:
            j=2
            k=0
            while j<i:
                k=i%j
                if k==0:
                    break
                if j==i-1:
                    print(i)
                j=j+1
            i=i+1


###### End ######

# 在主程序中调用该函数
###### Begin ######

isprimary(m)

###### End ######
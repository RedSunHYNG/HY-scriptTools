# 函数定义
def triangle1(a,b,c):
    # 判断三边能否构成三角形
    if (a+b)>c and (a+c)>b and (b+c)>a:
        return True
    else:
        return False
    
    
def triangle2(a,b,c):
    # 计算三角形周长和面积
    ##  补充代码1开始
    p=(a+b+c)/2
    sum=p*(p-a)*(p-b)*(p-c)
    sum=sum**(1/2)
    num=a+b+c
    return sum,num
    ##  补充代码1结束
    
# 函数调用
s1 = eval(input())
s2 = eval(input())
s3 = eval(input())
if triangle1(s1,s2,s3):   #请补充条件判定能否构成三角形
    perimeter=triangle2(s1,s2,s3)[1]    #调用计算三角形周长和面积的函数
    area=triangle2(s1,s2,s3)[0]
    print('周长{:.2f}'.format(perimeter))
    print('面积{:.3f}'.format(area))
else:
    print('不能构成三角形')
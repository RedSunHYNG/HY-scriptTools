import math		#引入math模块
a = float(input())		#读入测试变量a
b = float(input())		#读入测试变量b		
c = float(input())		#读入测试变量c

#请在下面补充代码，完成程序功能
#### Begin ######
d=b*b-4*a*c
if a==0:
    x=-c/b
    print('x= %.1f' % x)
elif a!=0:
    if d==0:
        e=2*a
        x=-b/e
        print('x1=',x,'x2=',x )
    elif d>0:
        e=2*a
        x1=(-b+math.sqrt(b*b-4*a*c))/e
        x2=(-b-math.sqrt(b*b-4*a*c))/e
        print('x1=',x1,'x2=',x2)
#### End  #######
    else:   #计算方程虚根并输出
        x1 =complex ((-b/(2*a)), math.sqrt(4*a*c-b*b)/(2*a))
        x2 =complex ((-b/(2*a)), - math.sqrt(4*a*c-b*b)/(2*a))
        print('x1=',x1,'x2=',x2)
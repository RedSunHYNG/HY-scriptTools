# s2-10成绩数据特征统计
print('数据特征统计，请输入整数(0-100)')
x = eval(input())
s,c = 0,0    # s-和 c-数据个数 
maxx,minn,pj = -100,100,0  # maxx-最高分 minn-最低分 pj-平均分
# 请在下面编写代码
# ********** Begin ********** #
a=0
b=100
if a<x:
    maxx=x
    a=x
if b>x:
    minn=x
    b=x
c=c+1
s=x
while True:
    x = eval(input())
    if 0<=x<=100:
        c=c+1
        s=s+x
        if a<x:
            maxx=x
            a=x
        if b>x:
            minn=x
            b=x
        pj=s/c
    elif x==-1:
        break
    else:
        print('输入错误')
# ********** End ********** #
# 请不要修改下面的代码
print("\n共有数{}个，和{}，平均分{:.1f}，最高分{}，最低分{}".format(c,s,pj,maxx,minn))
        
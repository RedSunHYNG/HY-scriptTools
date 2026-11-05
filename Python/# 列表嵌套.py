# 列表嵌套
scores = [
            ['Zhang ming',90,88,91],
            ['Li cai',98,98,100],
            ['Gu xiao',92,93,95],
            ['Yang liang',90,85,93],
            ['Zhang jin',89,97,92]
        ]

course = input()  #输入课程名
## 请在下面注释之间补充代码，根据输入的课程名称输出按此课程成绩降序排序后的结果
##  begin  ##
n=int(0)
if course=='语文':
    n=1
elif course=='数学':
    n=2
elif course=='英语':
    n=3
a=int(0)
while a+1<len(scores):
    a=a+1
    m=a
    while m>=1:
        if float(scores[m][n])>float(scores[m-1][n]):
            st=scores[m-1]
            scores[m-1]=scores[m]
            scores[m]=st
        else:
            m=m-1
i=int(0)
while i<len(scores):
    print(str(scores[i][n])+' '+str(scores[i][0]))
    i=i+1
##  end  ##
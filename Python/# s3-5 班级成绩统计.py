# s3-5 班级成绩统计
scores = input()     #输入考试成绩，以英文逗号分隔
#请在下面补充代码，完成程序功能
############Begin############
li = list(scores.split(","))
n=0
while n+1<len(li):
    n=n+1
    m=n
    while m>=1:
        if float(li[m])>float(li[m-1]):
            li[m-1]=float(li[m])+float(li[m-1])
            li[m]=float(li[m-1])-float(li[m])
            li[m-1]=float(li[m-1])-float(li[m])
        else:
            m=m-1
i=0
sum=0
while i<len(li):
    sum=sum+float(li[i])
    i=i+1
a=sum/len(li)

b=li[0]
c=li[1]
d=li[2]
e=li[len(li)-1]
print('本次考试共'+str(len(li))+'人参加考试，最高分'+str(b).rstrip('0').rstrip('.')+'，最低分'+str(e).rstrip('0').rstrip('.')+'，平均分'+str(round(a,3)).rstrip('0').rstrip('.'))
print('最高的三个分数是'+str(b).rstrip('0').rstrip('.')+','+str(c).rstrip('0').rstrip('.')+','+str(d).rstrip('0').rstrip('.'))
############End##############
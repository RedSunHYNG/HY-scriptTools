# 投票统计

candidate = {}  #存放选举结果的字典
#输入第一个被选举人姓名

##  请在下面补充代码，完成程序功能
##  补充代码开始
candidate['Alice'] = 0
candidate['Bob'] = 0
candidate['Rose'] = 0
n=0
m=0
while m==0:
    name = input()
    if name=='-1':
        m=1
    elif name=='Alice':
        candidate['Alice'] = candidate['Alice']+1
        n=n+1
    elif name=='Bob':
        candidate['Bob'] = candidate['Bob']+1
        n=n+1
    elif name=='Rose':
        candidate['Rose'] = candidate['Rose']+1
        n=n+1
print('有'+str(n)+'人参加投票，结果如下：')
print('Alice:'+str(candidate['Alice']))
print('Bob:'+str(candidate['Bob']))
print('Rose:'+str(candidate['Rose']))
##  补充代码结束

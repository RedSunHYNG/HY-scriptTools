#s2-7 四叶玫瑰数
n = 0   #统计个数的计数器，初值为0
# 请在下面编写代码
# ********** Begin ******** #
num=0
for i in range(1000,9999):
    sum = 0    #初始值 
    num=str(i)
    for i in num:     # n= '123'  遍历  i='2'
        sum +=  int(i)**4   #sum = 36
        if sum == eval(num):  
            n=n+1
            print(sum)
# ********** End ********** #
print('共有{}个四叶玫瑰数'.format(n))
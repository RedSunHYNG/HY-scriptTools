#s2-7 四叶玫瑰数
n = 0   #统计个数的计数器，初值为0
# 请在下面编写代码
# ********** Begin ******** #
num=1000
while num<10000:
    a=num//1000   
    b=num//100%10 
    c=num//10%10  
    d=num%10      
    if a**4+b**4+c**4+d**4==num:
        n=n+1
        print(num)
    num+=1
# ********** End ********** #
print('共有{}个四叶玫瑰数'.format(n))
n = input()  #输入数据
result = '都不是'
if len(n) == 3:
    sum = 0    #初始值 
    for i in n:     # n= '123'  遍历  i='2'
        sum +=  int(i)**3    #sum = 36
    if sum == eval(n):  
        result = '水仙花数'
#请在下面补充代码，完成程序功能
########## Begin ########
elif len(n)==4:
    sum = 0    #初始值 
    for i in n:     # n= '123'  遍历  i='2'
        sum +=  int(i)**4   #sum = 36
    if sum == eval(n):  
        result = '四叶玫瑰数'
print(result)
########## End ##########
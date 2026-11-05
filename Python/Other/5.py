#一个带*的形参名可接受任意个实参
#请在此添加代码，返回参数列表中所有数的和
def production(*arg):  
#********** Begin *********#
    i=0
    sum=1
    while i<len(arg):
        sum=sum*arg[i]
        i=i+1
    return sum
#**********  End  *********#    
#调用  
#调用production()函数并输出结果
print(production(2,3))
print(production(2,4,5))
print(production(10,2,3,4))
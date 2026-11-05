a = eval(input())     #输入三个数
b = eval(input())
c = eval(input())

#请在下面补充代码，完成程序功能
#reversed_list = list(reversed(my_list)) 倒叙
############Begin############
counts = [a,b,c]
count=3
num=0
x=[]
while count!=0:
    num=num+1
    for key in counts:
        if num==key:
            x.append(str(key))
            count=count-1
            if count==0:
                reversed_x = list(reversed(x))
                # 使用join转换为字符串并倒序
                joined_string = ' '.join(reversed_x)
                print(joined_string)
############End##############
# s3-4 文件更名
file = input()     #输入一批文件名，以空格分隔
#请在下面补充代码，完成程序功能
############Begin############
ff=file.split()
n=len(ff)
i=0
marker='.'
str1='_2021'
while i<n:
    a=str(ff[i])
    index=a.find(marker)
    if index != -1:
        ff[i]=str(ff[i])[:index]+str1+str(ff[i])[index:]
    i=i+1
############End##############a
#请勿修改下面代码
for f in ff:
    print(f,end=' ')
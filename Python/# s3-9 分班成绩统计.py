# s3-9 分班成绩统计
scores = {
'120305':   91.5,
'120203':	83,
'120104':	82,
'120301':	99,
'120306':	90.5,
'120206':	90.5,
'120302':	78,
'120204':	95.5,
'120201':	93.5,
'120304':	95,
'120103':	95,
'120105':	88,
'120202':	86,
'120205':	83.5,
'120102':	90,
'120303':	94,
'120101':	96.5,
'120106':	90,
'120107':   89,
'120110':   80,
'120209':   80,
'120310':   87,
'120311':   93,
}
avg_dic = {}   #存放班平均分的字典初始化
avg_list = []   #将班平均分排序用的列表初始化
#  在下面填充代码统计各班平均分保存到字典avg_dic
########## 补充代码1开始 ##########
li=[]
avg_num={}
li= list(scores.items())
i=0
#print(li)
while i<len(li):
#    li[i][0]=str(li[i][0])[3]
    if str(li[i][0])[3] in avg_dic.keys():
        i=i+1
    else:
        avg_dic[str(li[i][0])[3]] = float(0)
        i=i+1
j=0
while j<len(list(avg_dic.keys())):
    k=0
    sum=0
    a=0
    while k<len(li):
        if str(li[k][0])[3]==list(avg_dic.keys())[j]:
            sum=sum+li[k][1]
            a=a+1
        k=k+1
#    print(sum)
    num=sum/a
    avg_dic[str(li[j][0])[3]]=num
    avg_num[str(li[j][0])[3]]=a
    j=j+1
#print(avg_dic)
#print(str(li[1][1])[4])
########## 补充代码1结束 ##########

#  在下面填充代码将各班按照平均成绩排序
########## 补充代码2开始 ##########
s1 = sorted(avg_dic.items(), key=lambda x:x[1],reverse=True)
m=0
while m<len(s1):
    print('{}班 平均分{:.3f} 参赛{}人'.format(s1[m][0],s1[m][1],avg_num[s1[m][0]]))
    m=m+1
########## 补充代码2结束 ##########
#for item in avg_list:
#    print('{} 平均分{:.3f} 参赛{}人'.format(item[0],item[1][0],item[1][1]))
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 16 21:40:04 2022

@author: lixy
"""
# 创建并初始化volu_dict字典 
volu_dict = {}   # 建立空字典
while True:   # 无限循环，执行以下操作
    try:   # 尝试运行以下语句
        key_value = input()   # 输入数据
        if len(key_value)==0:   # 输入是空的吗？
            raise   # 抛出一个异常，转去17行运行 
        key = key_value.split()[0]  # 对输入的数据用空格进行分离，将分离得到的第一部分保存到key
        value = key_value.split()[1]   #将分离得到的第二部分(对应学生具体信息)保存到value
        volu_dict[key] = value   #添加“键:值”对
    except:  # 处理出现的异常
        break  # 停止循环，转去执行循环后面的第22行语句
    
# 请在此添加代码，实现对字典的添加、查找、修改等操作，并打印输出相应的值
## Begin ## 

volu_dict['服务意向'] = '科技服务'
print(volu_dict['学院'])
volu_dict['学院'] = '信息科学与工程学院'
del volu_dict['志愿服务经历']
print(volu_dict)

for key,value in volu_dict.items():
    print(key)
for key,value in volu_dict.items():
    print(value)
#s1 = sorted(university_dict.items(), key=lambda x:x[1],reverse=True)
##indexed_list = list(enumerate(s1.items()))
#print('排在第'+rank+'位的是：'+str(s1[int(rank)-1][0]) +' 高校数量：'+str(s1[int(rank)-1][1]))
## End ## 
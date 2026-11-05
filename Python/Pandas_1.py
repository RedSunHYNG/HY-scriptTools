import pandas as pd
import numpy as np
data = {'animal':['cat','cat','snake','dog','dog','cat','snake','cat','dog','dog'],'age':[2.5,3.0,0.5,np.nan,5.0,2.0,4.5,np.nan,7.0,3.0],'visits':[1,3,2,3,2,3,1,1,2,1],'priority':['yes','yes','no','yes','no','no','no','yes','no','no']}
labels = ['a','b','c','d','e','f','g','h','i','j']
df = pd.DataFrame(data,index=labels)
#显示df的基础信息，取出age值大于3的行，以列拼接自身完成一个新的df
print('1.')
df.info()
print(df[df['age']>3])
#计算df中每个不同种类animal的age的平均数
print('2.')
print(df.groupby('animal')['age'].mean())
#对每种animal的每种不同数量visits，计算平均age，即，返回一个表格，行是aniaml种类，列是visits数量，表格值是行动物种类，列访客数量的平均年龄
print('3.')
print(df.groupby(['animal','visits'])['age'].mean())
#1,创建一个含有NaN值的DataFrame   2,将空值全部填充为1
print('4.')
#default={'age':1}
print(df.fillna(1))
#1、创建了一个 2 行 2 列的子图，并在每个子图中显示 4 个不同的图像。第一个绘制平方函数，第二个绘制平方根函数，第三个绘制指数函数，第四个绘制对数函数
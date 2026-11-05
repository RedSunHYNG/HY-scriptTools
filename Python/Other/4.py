# -*- coding: utf-8 -*-
from math import *

#####定义函数,请在下面补充代码 ######
def move(x,y,step,angle=0):
    nx = x + step*cos(radians(angle))
    ny = y + step*sin(radians(angle))
    return nx,ny
###### 函数代码补充结束 ######

constr = input()

if constr.count(',') == 2:
    x,y,step = eval(constr)
    #### 请在下面补充代码，调用函数move，角度取默认值，计算新点坐标
    x=move(x,y,step)[0]
    y=move(x,y,step)[1]
    #### 补充代码结束 ####
    print('{:.1f} {:.1f}'.format(x,y))
elif constr.count(',') == 3:
    x,y,step,angle= eval(constr)
    #### 请在下面补充代码，调用函数move,带全部参数，计算新点坐标
    x=move(x,y,step,angle)[0]
    y=move(x,y,step,angle)[1]
    #### 补充代码结束 ####
    print('{:.1f} {:.1f}'.format(x,y))
else:
    print('数据输入错误')
    
 
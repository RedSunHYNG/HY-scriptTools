import matplotlib.pyplot as plt
fig,a =  plt.subplots(2,2)
import numpy as np
x = np.linspace(1.0,5.0)
plt.rcParams["font.sans-serif"]=["SimHei"]
#绘制平方函数
a[0][0].plot(x,x*x)
a[0][0].set_title('平方函数')
#绘制平方根图像
a[0][1].plot(x,np.sqrt(x))
a[0][1].set_title('平方根图像')
#绘制
a[1][0].plot(x,np.exp(x))
a[1][0].set_title('指数函数')
#绘制对数函数
a[1][1].plot(x,np.log10(x))
a[1][1].set_title('对数函数')
plt.show()

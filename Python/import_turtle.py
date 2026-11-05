import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from pylab import mpl
# 设置显示中文字体
mpl.rcParams["font.sans-serif"] = ["SimHei"]
# 匹萨直径数据
X = np.array([6, 8, 10, 14, 18]).reshape(-1, 1)
# 匹萨价格数据
y = np.array([7, 9, 13, 17.5, 18])
# 绘制散点图
plt.scatter(X, y)
plt.xlabel('直径 (inch)')
plt.ylabel('价格 (dollar)')
plt.title('匹萨尺寸和价格分布规律')
plt.show()
# 建立线性回归模型
model = LinearRegression()
model.fit(X, y)
# 预测价格
diameter = np.array([[12]])
price_12 = model.predict(diameter)
print("当匹萨直径为12时，预测价格为:", price_12)
diameters = np.array([[0], [10], [14], [25]])
prices = model.predict(diameters)
print("当匹萨直径为[0, 10, 14, 25]时，预测价格为:", prices)
# 绘制预测结果图
plt.scatter(X, y)
plt.plot(diameters, prices, color='red', marker='o')
plt.xlabel('直径 (inch)')
plt.ylabel('价格 (dollar)')
plt.title('匹萨尺寸和价格预测结果')
plt.show()

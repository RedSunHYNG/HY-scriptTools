import numpy as np
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeRegressor, plot_tree
from sklearn.tree import plot_tree

# 假设我们有一些虚构的桃子甜度和好吃程度的数据
# 甜度（X）和好吃程度（y）
X = np.array([[8], [10], [12], [14], [16], [18], [20], [22], [24], [26]]).reshape(-1, 1)
y = np.array([5, 6, 7, 7.5, 8, 8.5, 9, 9.2, 9.5, 9.8])

# 创建CART回归树模型
regressor = DecisionTreeRegressor(random_state=42)

# 训练模型
regressor.fit(X, y)

# 可视化CART回归树
fig, axes = plt.subplots(nrows=1, ncols=1, figsize=(10, 10), dpi=300)
plot_tree(regressor,
          feature_names=['甜度'],
          class_names=['好吃程度'],
          filled=True,
          rounded=True,
          ax=axes)

# 添加标题和轴标签
plt.title('CART 回归树 - 桃子的甜度与好吃程度')
plt.xlabel('特征：甜度')
plt.ylabel('目标：好吃程度')

# 显示图形
plt.show()
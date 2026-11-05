import pandas as pd
import numpy as np
from sklearn.neighbors import KNeighborsClassifier


# 加载数据
train_x=np.loadtxt('./fruit_data.txt',usecols=(1,2,3,4))
train_y=np.loadtxt('./fruit_data.txt',usecols=(0)) 
# 数据预处理
test_x=np.loadtxt('./new_fruit_data.txt',usecols=(1,2,3,4), skiprows=1)
test_y=pd.read_csv('./new_fruit_data.txt') 
# 划分数据集

# 使用KNN算法
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(train_x, train_y)

# 预测新数据
predictions = knn.predict(test_x)

# 输出预测结果
print(predictions)
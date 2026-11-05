import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix

# 步骤 1: 加载并预处理数据
# 假设 fruit_data.txt 的格式是：类别,质量,宽度,颜色值
# 读取训练数据
with open('fruit_data.txt', 'r') as file:
    lines = file.readlines()
    # 跳过标题行
    header = lines[0].strip().split(',')
    X_train = []
    y_train = []
    for line in lines[1:]:
        parts = line.strip().split(',')
        label = int(parts[0])
        mass = float(parts[1])
        width = float(parts[2])
        color_score = float(parts[3])
        X_train.append([mass, width, color_score])
        y_train.append(label)

# 将数据转换为numpy数组
X_train = np.array(X_train)
y_train = np.array(y_train)

# 步骤 2: 使用KNN算法训练模型
# 选择一个K值，例如K=3
k = 3
knn = KNeighborsClassifier(n_neighbors=k)

# 训练模型
knn.fit(X_train, y_train)

# 步骤 3: 加载新数据并预测水果类别
# 读取新数据
with open('new_fruit_data.txt', 'r') as file:
    new_lines = file.readlines()
    # 假设new_fruit_data.txt的格式与fruit_data.txt相同
    X_new = []
    for line in new_lines:
        parts = line.strip().split(',')
        mass = float(parts[1])
        width = float(parts[2])
        color_score = float(parts[3])
        X_new.append([mass, width, color_score])

# 将新数据转换为numpy数组
X_new = np.array(X_new)

# 使用模型进行预测
predictions = knn.predict(X_new)

# 打印预测结果
for i, prediction in enumerate(predictions):
    print(f"预测水果A/B的类别: {prediction}")

# 注意：以上代码假设fruit_data.txt和new_fruit_data.txt中的数据格式是正确的，
# 并且每行数据的特征数量与训练模型时使用的特征数量一致。
# 如果数据格式不同或特征数量不一致，你
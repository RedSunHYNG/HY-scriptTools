from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer


# 假设data是一个包含信用卡交易数据的pandas DataFrame
# 其中'isFraud'是一个二进制标签，表示交易是否为欺诈
data = pd.read_csv('KaggleCredit2.csv')
# 初始化 SimpleImputer 对象，使用均值策略
imputer = SimpleImputer(missing_values=np.nan, strategy='mean')

# 使用 fit_transform 方法填充缺失值
data_filled = pd.DataFrame(imputer.fit_transform(data), columns=data.columns)
# 分离特征和标签
features = data_filled.drop('SeriousDlqin2yrs', axis=1)
labels = data_filled['SeriousDlqin2yrs']

# 划分训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.2, random_state=42)
 
# 创建并训练SVM模型
svm_classifier = SVC(kernel='rbf', C=100, gamma=0.1)
svm_classifier.fit(X_train, y_train)
 
# 进行预测
y_pred = svm_classifier.predict(X_test)
 
# 评估模型
accuracy = accuracy_score(y_test, y_pred)
print(f"SVM 模型的准确率为: {accuracy*100:.2f}%")
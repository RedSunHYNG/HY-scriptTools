import numpy as np  
from sklearn.datasets import load_iris  
from sklearn.model_selection import train_test_split  
from sklearn.linear_model import LogisticRegression  
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report  

# 加载鸢尾花数据集  
iris = load_iris()  
X = iris.data  
y = iris.target  

# 划分训练集和测试集  
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)  

# 定义逻辑回归模型   
logreg = LogisticRegression(solver='lbfgs', multi_class='multinomial', random_state=42)  

# 训练模型  
logreg.fit(X_train, y_train)  

print("模型系数:\n", logreg.coef_)  

print("模型截距:\n", logreg.intercept_)  

# 预测测试集结果  
y_pred = logreg.predict(X_test)  

score = logreg.score(X_train, y_train)  
print("模型得分（训练集准确率）:", score)  

accuracy = accuracy_score(y_test, y_pred)  
print("分类准确率:", accuracy)  

cm = confusion_matrix(y_test, y_pred)  
print("混淆矩阵:\n", cm)   
print("分类结果报告:\n", classification_report(y_test, y_pred))

import pandas as pd
import numpy as np
from sklearn import preprocessing
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.svm import SVC
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score, roc_auc_score, roc_curve
from sklearn.feature_selection import SelectKBest, chi2
import matplotlib.pyplot as plt
from imblearn.over_sampling import SMOTE


data = pd.read_csv('KaggleCredit2_c.csv')

#数据清理
data.fillna(data.mean(), inplace=True)  

#模型设计
selector = SelectKBest(chi2, k=10)  
X = data.drop("SeriousDlqin2yrs", axis=1)
y = data["SeriousDlqin2yrs"]
X_new = selector.fit_transform(X, y)
selected_features = X.columns[selector.get_support(indices=True)]
smote = SMOTE(random_state=6)
X_resampled, y_resampled = smote.fit_resample(X_new, y)
X_train, X_test, y_train, y_test = train_test_split(X_resampled, y_resampled, test_size=0.21, random_state=6)
scaler = preprocessing.StandardScaler().fit(X_train)
X_train_scaled = scaler.transform(X_train)
X_test_scaled = scaler.transform(X_test)
svm = SVC(probability=True)
param_grid = {'C': [0.1, 1, 10], 'gamma': [1, 0.1], 'kernel': ['rbf']}
grid = GridSearchCV(svm, param_grid, refit=True, verbose=2, cv=3, scoring='accuracy', n_jobs=-1)
grid.fit(X_train_scaled, y_train)
best_svm = grid.best_estimator_
y_pred = best_svm.predict(X_test_scaled)
y_pred_proba = best_svm.predict_proba(X_test_scaled)[:, 1]

print("Classification Report:",classification_report(y_test, y_pred),",Confusion Matrix:",confusion_matrix(y_test, y_pred),",Accuracy Score:",accuracy_score(y_test, y_pred),",AUC-ROC Score:",roc_auc_score(y_test, y_pred_proba))

# 数据模拟
fpr, tpr, _ = roc_curve(y_test, y_pred_proba)
plt.plot(fpr, tpr, label='ROC curve (area = %0.2f)' % roc_auc_score(y_test, y_pred_proba))
plt.plot([0, 1], [0, 1], 'k--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
# 图像输出
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver Operating Characteristic')
plt.legend(loc="lower right")
plt.show()

print("Best Parameters Found:"+grid.best_params_)


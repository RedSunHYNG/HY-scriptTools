import pandas as pd
import numpy as np
import csv
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, r2_score
# 加载数据集
data = pd.read_csv('car_sales_data.csv',encoding='latin1')

#去除特殊值
data.replace('-', np.nan, inplace=True)

## 检测缺失值
##print("Missing values:")
##print(data.isnull().sum())

# 处理缺少的值
data = data.dropna()

## 检查重复项
##print("\nDuplicate rows:")
##print(data.duplicated().sum())

# 删除重复的行
data = data.drop_duplicates()

# 数据类型
#print("\nData types:")
#print(data.dtypes)

# 转换数据类型
data['price'] = data['price'].astype(float)
data['power'] = data['power'].astype(float)
data['engine_torque'] = data['engine_torque'].astype(float)
data['total_quality'] = data['total_quality'].astype(float)
data['sale_quantity'] = data['sale_quantity'].astype(float)

# 排除异常值
q1 = data['sale_quantity'].quantile(0.25)
q3 = data['sale_quantity'].quantile(0.75)
iqr = q3 - q1
lower_bound = q1 - 1.5 * iqr
upper_bound = q3 + 1.5 * iqr
data = data[(data['sale_quantity'] >= lower_bound) & (data['sale_quantity'] <= upper_bound)]

#选取价格，力量，扭矩，质量的特征
X = data[['price', 'power', 'engine_torque',  'total_quality']]
y = data['sale_quantity']

#训练不同类型的模型
## Split the data into training and testing sets
##X_train, X_test, y_t
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
## Train different regression models
linear_model = LinearRegression()
tree_model = DecisionTreeRegressor()
forest_model = RandomForestRegressor()

linear_model.fit(X_train, y_train)
tree_model.fit(X_train, y_train)
forest_model.fit(X_train, y_train)

# 评估测试集上的模型
linear_pred = linear_model.predict(X_test)
tree_pred = tree_model.predict(X_test)
forest_pred = forest_model.predict(X_test)

linear_mae = mean_absolute_error(y_test, linear_pred)
linear_r2 = r2_score(y_test, linear_pred)

tree_mae = mean_absolute_error(y_test, tree_pred)
tree_r2 = r2_score(y_test, tree_pred)

forest_mae = mean_absolute_error(y_test, forest_pred)
forest_r2 = r2_score(y_test, forest_pred)

print("Linear Regression:")
print("MAE:", linear_mae)
print("R-squared:", linear_r2)

print("\nDecision Tree Regression:")
print("MAE:", tree_mae)
print("R-squared:", tree_r2)

print("\nRandom Forest Regression:")
print("MAE:", forest_mae)
print("R-squared:", forest_r2)

# 对新数据进行评估
new_data = pd.DataFrame({ 'price': [9.5], 'power': [98], 'engine_torque': [170], 'total_quality': [1695]})
linear_prediction = linear_model.predict(new_data)
tree_prediction = tree_model.predict(new_data)
forest_prediction = forest_model.predict(new_data)

print("\n各模型下运行预测结果:")
print("线性回归 Linear Regression:", linear_prediction[0])
print("决策树回归 Decision Tree Regression:", tree_prediction[0])
print("随机森林回归 Random Forest Regression:", forest_prediction[0])

#当  'price': [9.5], 'power': [98], 'engine_torque': [170], 'total_quality': [1695]   售出94
value1 = linear_prediction[0]
value2 = tree_prediction[0]
value3 = forest_prediction[0]

value1 = value1 - 94 
value2 = value2 - 94
value3 = value3 - 94

if value1 < 0:
    value1 = abs(value1)
if value2 < 0:
    value2 = abs(value2)
if value3 < 0:
    value3 = abs(value3)
max_value = min(value1, value2, value3)

#对新数据进行预测
new_data = pd.read_csv('test_sales.csv',encoding='latin1')

#对预测集采取同等类型的数据清理
new_data.replace('-', np.nan, inplace=True)
new_data = new_data.dropna()
new_data = new_data.drop_duplicates()
new_data['price'] = new_data['price'].astype(float)
new_data['power'] = new_data['power'].astype(float)
new_data['engine_torque'] = new_data['engine_torque'].astype(float)
new_data['total_quality'] = new_data['total_quality'].astype(float)
#选取 id,价格，力量，扭矩，质量的特征
new_dataid = new_data['sale_id'].values
new_data = new_data[['price', 'power', 'engine_torque',  'total_quality']]

linear_prediction1 = linear_model.predict(new_data)
tree_prediction1 = tree_model.predict(new_data)
forest_prediction1 = forest_model.predict(new_data)

if max_value == value1:
    prediction_data = linear_prediction1
    print("采用线性回归")
elif max_value == value2:
    prediction_data = tree_prediction1
    print("采用决策树回归")
elif max_value == value3:
    prediction_data = forest_prediction1
    print("采用随机森林回归")
else:
    print("未知错误")


print("预测结果:", prediction_data)
numpy_array = np.array(prediction_data)
# 指定文件名
filename = 'submit_sales.csv'
int_array = numpy_array.astype(int)
# 打开文件以写入CSV数据
with open('submit_sales.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['stutent_name', 'student_code', 'sale_id', 'sale_quantity'])
    # 遍历 numpy 数组的每个元素
    for value_,value__ in zip(new_dataid,int_array):
        # 将每个元素作为列表传递给 writerow 方法
        writer.writerow(['顾芯瑀', '21012936', value_, value__])

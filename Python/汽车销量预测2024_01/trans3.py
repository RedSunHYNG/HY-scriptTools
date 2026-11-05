import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, r2_score
# Load the car sales data
data = pd.read_csv('car_sales_data.csv',encoding='latin1')

#数据清理
data.replace('-', np.nan, inplace=True)

# Check for missing values
print("Missing values:")
print(data.isnull().sum())

# Handle missing values
data = data.dropna()

# Check for duplicates
print("\nDuplicate rows:")
print(data.duplicated().sum())

# Remove duplicate rows
data = data.drop_duplicates()

# Check data types
print("\nData types:")
print(data.dtypes)

# Convert data types if necessary
data['price'] = data['price'].astype(float)
data['power'] = data['power'].astype(float)
data['engine_torque'] = data['engine_torque'].astype(float)
data['total_quality'] = data['total_quality'].astype(float)
data['sale_quantity'] = data['sale_quantity'].astype(float)

# Identify and remove outliers
q1 = data['sale_quantity'].quantile(0.25)
q3 = data['sale_quantity'].quantile(0.75)
iqr = q3 - q1
lower_bound = q1 - 1.5 * iqr
upper_bound = q3 + 1.5 * iqr
data = data[(data['sale_quantity'] >= lower_bound) & (data['sale_quantity'] <= upper_bound)]

# Prepare the data
#选取价格，力量，扭矩，质量的特征
X = data[['price', 'power', 'engine_torque',  'total_quality']]
y = data['sale_quantity']

# Split the data into training and testing sets
#划分测试集和验证集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
# 模型训练
linear_model = LinearRegression()
tree_model = DecisionTreeRegressor()
forest_model = RandomForestRegressor()

linear_model.fit(X_train, y_train)
tree_model.fit(X_train, y_train)
forest_model.fit(X_train, y_train)

# Evaluate the models on the test set
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

# 对新数据进行预测
#new_data = pd.DataFrame({ 'price': [9.5], 'power': [98], 'engine_torque': [170], 'total_quality': [1695]})
#new_data  = pd.read_csv('test_sales.csv',encoding='latin1')
#new_data.replace('-', np.nan, inplace=True)

# Check for missing values
#print("new_Missing values:")
#print(new_data.isnull().sum())

# Handle missing values
#new_data = new_data.dropna()

# Check for duplicates
#print("\nnew_Duplicate rows:")
#print(new_data.duplicated().sum())

# Remove duplicate rows
#new_data = new_data.drop_duplicates()

# Check data types
#print("\nnew_Data types:")
#print(new_data.dtypes)

# Convert data types if necessary
#data['price'] = data['price'].astype(float)
#data['power'] = data['power'].astype(float)
#data['engine_torque'] = data['engine_torque'].astype(float)
#data['total_quality'] = data['total_quality'].astype(float)
new_data = pd.read_csv('test_sales.csv',encoding='latin1')

#数据清理
new_data.replace('-', np.nan, inplace=True)

# Check for missing values
print("Missing values:")
print(new_data.isnull().sum())

# Handle missing values
new_data = new_data.dropna()

# Check for duplicates
print("\nDuplicate rows:")
print(new_data.duplicated().sum())

# Remove duplicate rows
new_data = new_data.drop_duplicates()

# Check new_data types
print("\nnew_Data types:")
print(new_data.dtypes)

# Convert new_data types if necessary
new_data['price'] = new_data['price'].astype(float)
new_data['power'] = new_data['power'].astype(float)
new_data['engine_torque'] = new_data['engine_torque'].astype(float)
new_data['total_quality'] = new_data['total_quality'].astype(float)

new_data = new_data[['price', 'power', 'engine_torque',  'total_quality']]

linear_prediction = linear_model.predict(new_data)
tree_prediction = tree_model.predict(new_data)
forest_prediction = forest_model.predict(new_data)

print("\n各模型下运行预测结果:")
print("线性回归 Linear Regression:", linear_prediction)
print("决策树回归 Decision Tree Regression:", tree_prediction[0])
print("随机森林回归 Random Forest Regression:", forest_prediction[0])

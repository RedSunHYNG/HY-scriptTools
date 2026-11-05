import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, r2_score
import os
print(os.getcwd())
# Load the car sales data
data = pd.read_csv('car_sales_data.csv',encoding='utf-8')

# Prepare the data
X = data[['engine_size', 'horsepower', 'price', 'marketing_spend']]
y = data['sales']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train different regression models
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

# Make predictions on new data
new_data = pd.DataFrame({'engine_size': [2.4], 'horsepower': [180], 'price': [35000], 'marketing_spend': [50000]})
linear_prediction = linear_model.predict(new_data)
tree_prediction = tree_model.predict(new_data)
forest_prediction = forest_model.predict(new_data)

print("\nPredictions:")
print("Linear Regression:", linear_prediction[0])
print("Decision Tree Regression:", tree_prediction[0])
print("Random Forest Regression:", forest_prediction[0])

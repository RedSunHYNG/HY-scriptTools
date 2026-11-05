import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Load the dataset
data = pd.read_csv('KaggleCredit2.csv')
# Check for missing values
print(data.isnull().sum())

# Drop rows with any missing values
data = data.dropna()
# Split the data into features and target
X = data.drop('SeriousDlqin2yrs', axis=1)
y = data['SeriousDlqin2yrs']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=6)
# Scale the features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
# Train the SVM model
svm = SVC(kernel='rbf', C=1, gamma='auto')
svm.fit(X_train_scaled, y_train)
# Evaluate the model
y_pred = svm.predict(X_test_scaled)
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy:.2f}')
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))

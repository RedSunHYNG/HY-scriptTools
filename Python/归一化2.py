import pandas as pd
import numpy as np
import re
from sklearn.preprocessing import MinMaxScaler

# 读取CSV文件的第一列
df = pd.read_csv('dog_cat.csv', usecols=[0], header=None)

# 清理数据：将非数字字符替换为NaN
def extract_numbers(text):
    return re.findall(r'\d+', text)

numbers = data.iloc[:, 0].apply(extract_numbers)
df[0] = df[0].replace(r'[^\d.]', np.nan, regex=True)

# 将NaN值转换为适当的缺失值标记，例如0或np.nan
df[0] = df[0].astype(float).fillna(0)  # 假设我们希望将缺失值替换为0

# 确保所有值都是数字
assert df[0].apply(lambda x: isinstance(x, (int, float))).all(), "All values must be numeric."

# 初始化归一化处理器
scaler = MinMaxScaler()

# 对第一列进行归一化处理
df[0] = scaler.fit_transform(df[0].values.reshape(-1, 1))

# 如果需要，可以将DataFrame转换为NumPy数组
normalized_array = df[0].values

# 打印归一化后的数组
print(df.values)
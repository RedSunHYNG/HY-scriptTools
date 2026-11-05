from sklearn import preprocessing
import pandas
import re
import numpy as np
# ... 上面的代码 ...
 
# 使用StringIO读取CSV内容
data = pandas.read_csv('dog_cat.csv', usecols=[0], header=None)
    
    # 提取第一列中的数字部分
def extract_numbers(text):
    return re.findall(r'\d+', text)

numbers = data.iloc[:, 0].apply(extract_numbers)

mm = preprocessing.MinMaxScaler()
array_of_strings = np.array([item[0] for item in numbers])
new_data = mm.fit_transform(array_of_strings.reshape(-1, 1))
print(new_data)

import pandas as pd
import re
from sklearn.preprocessing import MinMaxScaler

def extract_numbers(text):
    """
    从文本中提取数字并返回它们作为字符串列表
    """
    return re.findall(r'\d+', text)

def read_and_normalize_first_column(file_path):
    """
    读取CSV文件的第一列，提取数字并进行归一化处理
    :param file_path: CSV文件路径
    :return: 归一化后的数据（仅第一列）
    """
    # 读取CSV文件的第一列
    data = pd.read_csv(file_path, usecols=[0], header=None)
    
    # 提取第一列中的数字部分
    numbers = data.iloc[:, 0].apply(extract_numbers)
    
    # 将提取的数字部分转换为浮点数并归一化
    normalized_numbers = []
    for nums in numbers:
        # 将字符串列表转换为浮点数列表
        float_nums = [float(num) for num in nums if num.isdigit()]
        
        # 如果列表不为空，则进行归一化
        if float_nums:
            column_data = numbers[float_nums].to_numpy()
            scaler = MinMaxScaler()
            normalized_float_nums = scaler.fit_transform(column_data.reshape(-1, 1))
            normalized_numbers.extend(normalized_float_nums.flatten())
    
    # 返回归一化后的数字列表
    return normalized_numbers

# 使用方法
normalized_first_column = read_and_normalize_first_column('dog_cat.csv')
print(normalized_first_column)
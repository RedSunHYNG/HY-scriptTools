import os
import pandas
from sklearn.model_selection import train_test_split
#返回指定路径下的所有文件和目录的名称列表
#test_path = 'D:/Date/archive/test_set/test_set/cats'
#test_file_names = os.listdir(test_path)
#print("test_path大小：{}".format(len(test_file_names)))
#print("test_path样例：{}".format(test_file_names[0:5])) #测试集文件名：序号
#for test_file in test_file_names:
#    idx = test_file.split('.')[0]
#    test_idx.append(idx)
#    image_path = os.path.join(test_path, test_file)
#    image_paths.append(image_path)
#test_df = pandas.DataFrame()
#test_df['test_image_path'] = image_paths
#test_df.head()
##train_set, val_set = train_test_split(train_df, random_state=42, stratify=None)
train_path = 'D:/Date/archive/images'
train_file_names = os.listdir(train_path)
print("train_path大小：{}".format(len(train_file_names)))
print("train_path样例：{}".format(train_file_names[0:5]))#训练集文件名：标签+序号
# 以下是分层抽样，因为随机抽样容易导致样本偏差
#训练集 train_image_path  label
image_paths = []
labels = []
for train_file in train_file_names:
    label = train_file.split('.')[0]
    labels.append(label)
    image_path = os.path.join(train_path, train_file)
    image_paths.append(image_path)
train_df = pandas.DataFrame()
train_df['train_image_path'] = image_paths #为自定义属性名添加列表
train_df['label'] = labels
train_df.head()
#测试集 teat_image_path
image_paths = []
test_idx = []
train_set, val_set = train_test_split(train_df)
print("训练集大小：{}".format(len(train_set)))
print("测试集大小：{}".format(len(val_set)))

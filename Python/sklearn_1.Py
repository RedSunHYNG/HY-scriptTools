import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

#data column names
LENGTH_SEPAL = 'sepalLength'
WIDTH_SEPAL = 'sepalWidth'
LENGTH_PETAL = 'petalLength'
WIDTH_PETAL = 'petalWidth'
LABEL_NAME = 'flowerName'

#flower names
NAMES_FLOWERS = ['Iris-setosa','Iris-versicolor','Iris-virginica']
#从指定网址获取IRIS数据

def getIrisData():
    columnNames = [LENGTH_SEPAL,WIDTH_SEPAL,LENGTH_PETAL,WIDTH_PETAL,LABEL_NAME]
    dataUrl = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
    df = pd.read_csv(dataUrl,header=None,names=columnNames)
    return df

#绘制散点图
def drawScatterData(df):
    # 提取数据中的0-150行和第0,2列
    X = df.iloc[0:150, [0, 2]].values
    
    #根据数据的内容，前50行为setosa的数据，直接按照行进行提取，并用红色绘制
    plt.scatter(X[0:50, 0], X[0:50, 1],
                color='red', marker='o', label='Iris-setosa')
    #根据数据的内容，中间50行为versicolor的数据，直接按照行进行提取，并用蓝色绘制
    plt.scatter(X[50:100, 0], X[50:100, 1],
                color='blue', marker='*', label='Iris-versicolor')
    plt.scatter(X[100:150, 0], X[100:150, 1],
                color='green', marker='3', label='Iris-virginica')

    plt.xlabel('Sepal length [cm]')
    plt.ylabel('Petal length [cm]')
    plt.legend(loc='upper left')
    #保存图像
    plt.savefig('iris.png', dpi=300)
    plt.show()

if __name__ == '__main__':
    df = getIrisData()
    drawScatterData(df)
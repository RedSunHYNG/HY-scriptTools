from numpy import *
from matplotlib import pyplot as plt
import matplotlib; matplotlib.use('TkAgg')
def disteclud(veca,vecb):
    return sqrt(sum(power(veca-vecb,2)))
def initcenter(dataset,k):
    shape=dataset.shape
    n=shape[1]
    classcenter=array(zeros((k,n)))
    for j in range(n):
        firstk=dataset[:k,j]
        classcenter[:,j]=firstk
    return  classcenter
def mykmeans(dataset,k):
    m=len(dataset)
    clusterpoints=array(zeros((m,2)))
    classCenter=initcenter(dataset,k)
    clusterchanged=True
    while clusterchanged:
        clusterchanged=False
        for i in range(m):
            mindist=inf
            minindex=-1
            for j in range(k):
                distji=disteclud(classCenter[j,:],dataset[i,:])
                if distji<mindist:
                    mindist=distji;minindex=j
            if clusterpoints[i,0]!=minindex:
                clusterchanged=True
            clusterpoints[i,:]=minindex,mindist**2
        for cent in range(k):
            ptsinclust=dataset[nonzero(clusterpoints[:,0]==cent)[0]]
            classCenter[cent,:]=mean(ptsinclust,axis=0)
    return classCenter,clusterpoints
def show(dataset,k,classCenter,clusterPoints):
    fig=plt.figure()
    rect=[0.1,0.1,1.0,1.0]
    axprops=dict(xticks=[],yticks=[])
    ax0=fig.add_axes(rect,label='ax1',frameon=False)
    imgp=plt.imread(r'./city.png')
    ax0.imshow(imgp)
    ax1=fig.add_axes(rect,label='ax1',frameon=False)
    numsamples=len(dataset)
    mark=['ok','^b','om','og','sc']
    for i in range(numsamples):
        markindex=int(clusterPoints[i,0])%k
        ax1.plot(dataset[i,0],dataset[i,1],mark[markindex])
    for i in range(k):
        markindex=int(clusterPoints[i,0])%k
        ax1.plot(classCenter[i,0],classCenter[i,1],'^r',markersize=12)
    plt.show()
dataset=loadtxt(r'./testSet.txt')
k=5
classCenter,clssspoints=mykmeans(dataset,k)
show(dataset,k,classCenter,clssspoints)

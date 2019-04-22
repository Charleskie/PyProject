# coding=utf-8

from matplotlib.font_manager import FontProperties
from pylab import *

font = FontProperties(fname=r"c:\windows\fonts\simsun.ttc", size=14)
plt.rcParams['font.sans-serif']=['SimHei'] #解决中文显示问题，目前只知道黑体可行
plt.rcParams['axes.unicode_minus']=False #解决负数坐标显示问题


def draw(arr):
    mu = np.mean(arr) #均值
    sigma = np.std(arr) #方差
    n, bins, patches = plt.hist(arr, len(arr), density=1, facecolor='blue', alpha=0.5)
    # 直方图函数，x为x轴的值，normed=1表示为概率密度，即和为一，绿色方块，色深参数0.5.返回n个概率，直方块左边线的x值，及各个方块对象
    y = mlab.normpdf(bins, mu, sigma)  # 拟合一条最佳正态分布曲线y
    plt.xlabel('sepal-length')  # 绘制x轴
    plt.ylabel('Probability')  # 绘制y轴
    print("均值：",mu,"方差：" ,sigma)
    plt.title(r'Histogram : $\mu=%.3f$,$\sigma=%.3f$'%(mu,sigma))  # 中文标题 u'xxx'
    plt.plot(bins,y,'r--')
    plt.show()
#-*- coding: utf-8 -*-

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.font_manager import FontProperties
from pylab import *
f=pd.read_csv("I:\monthdata\part-00000")
print(f)
col=f.iloc[:,0]
arrs=col.values
arr=[]
g=1
for i in arrs:
    arr.append(g)
    g=g+1

mu_all = np.mean(arrs)
siama_all = np.std(arrs)
n,bins,patches=plt.hist(arrs,len(arrs),density=1,facecolor='blue',alpha=0.5)
y = mlab.normpdf(bins, mu_all, siama_all) #拟合一条最佳正态分布曲线y
plt.xlabel('sepal-length') #绘制x轴
plt.ylabel('Probability') #绘制y轴
print(mu_all,siama_all)
plt.title(r'Histogram : $\mu=133.974$,$\sigma=85.682$')#中文标题 u'xxx'
plt.subplots_adjust(left=0.15)
plt.plot(bins,y,'r--')
plt.show()
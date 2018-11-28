#-*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as mtick
import matplotlib as mpl
from matplotlib.font_manager import FontProperties
from pylab import *
import matplotlib.dates as mdate
import pandas as pd
from matplotlib.ticker import  FormatStrFormatter
font = FontProperties(fname=r"c:\windows\fonts\simsun.ttc", size=14)
a=[15,145,111,102,109,99,88,83,71,89,92,86,86,87,104,85,88,95,102,85,96,103,114,103,102,82,75,37]  #数据
b=[1,10,7,7,7,7,6,6,5,6,6,6,6,6,7,6,6,6,7,6,6,7,8,7,7,5,5,1]
l=[i for i in range(28)]

# plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签

 #将x主刻度标签设置为20的倍数(也即以 20为主刻度单位其余可类推)
xmajorLocator = MultipleLocator(4);
#将x轴次刻度标签设置为5的倍数
xminorLocator = MultipleLocator(1)

fmt='%.1f%%'
yticks = mtick.FormatStrFormatter(fmt)  #设置百分比形式的坐标轴
lx=['7:00:00',' ',' ',' ','9:00:00',' ',' ',' ','11:00:00',' ',' ',' ','13:00:00',' ',' ',' ','15:00:00',' ',' ',' ','17:00:00',' ',' ',' ','19:00:00',' ',' ',' ','21:00:00 ']

fig = plt.figure()
ax1 = fig.add_subplot(111)
ax1.plot(l, b,alpha=2,color='steelblue',label=u'Departure times');

# ax1.yaxis.set_major_formatter(yticks)
# for i,(_x,_y) in enumerate(zip(l,b)):
#     plt.text(_x,_y,b[i],color='black',fontsize=10,)  #将数值显示在图形上
ax1.legend(loc=1)
ax1.set_ylim([0, 12]);
ax1.set_ylabel('Departure times');

ax1.xaxis.set_major_locator(xmajorLocator)
#显示次刻度标签的位置,没有标签文本
ax1.xaxis.set_minor_locator(xminorLocator)

plt.legend(prop={'family':'SimHei','size':8})  #设置中文
ax2 = ax1.twinx() # this is the important function
plt.bar(l,a,alpha=1,color='gray',label=u'Bus passenger flow')
ax2.set_ylabel("Bus passenger flow")
ax2.legend(loc=2)
ax2.set_ylim([0, 250])  #设置y轴取值范围
mpl.rc('xtick', labelsize=1)
plt.legend(prop={'family':'SimHei','size':8},loc="upper left")
plt.xticks(range(29),lx)
# plt.xticks(rotation=180)
# plt.grid()
plt.show()
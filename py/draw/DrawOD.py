#-*- coding: utf-8 -*-

import matplotlib.ticker as mtick
from matplotlib.font_manager import FontProperties
from pylab import *
font = FontProperties(fname=r"c:\windows\fonts\simsun.ttc", size=14)
a=[1,77,177,216,221,218,200,178,146,130,130,128,140,149,138,129,129,136,148,146,145,170,196,189,186,166,127,111,92,72,57,37,11]  #数据
b=[2,100,310,342,377,351,325,295,284,254,195,184,194,237,224,221,184,165,165,154,158,177,234,242,221,231,172,164,140,122,100,60,8]
l=[i for i in range(33)]

# plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签

 #将x主刻度标签设置为20的倍数(也即以 20为主刻度单位其余可类推)
xmajorLocator = MultipleLocator(4);
#将x轴次刻度标签设置为5的倍数
xminorLocator = MultipleLocator(1)

# fmt='%.1f%%'
# yticks = mtick.FormatStrFormatter(fmt)  #设置百分比形式的坐标轴
lx=[' ','7:00',' ',' ',' ','9:00',' ',' ',' ','11:00',' ',' ',' ','13:00',' ',' ',' ','15:00',' ',' ',' ','17:00',' ',' ',' ','19:00',' ',' ',' ','21:00',' ', ' ','22:30 ']

fig = plt.figure()
ax1 = fig.add_subplot(111)
plt.plot(l, a,alpha=1,color='steelblue',label=u'After optimization');

# ax1.yaxis.set_major_formatter(yticks)
# for i,(_x,_y) in enumerate(zip(l,a)):
#     plt.text(_x,_y,a[i],color='black',fontsize=10,)  #将数值显示在图形上
ax1.legend(loc=1)
ax1.set_ylim([0, 600]);
ax1.set_ylabel('Station Flow');

ax1.xaxis.set_major_locator(xmajorLocator)
#显示次刻度标签的位置,没有标签文本
ax1.xaxis.set_minor_locator(xminorLocator)

plt.legend(prop={'family':'SimHei','size':8})  #设置中文
# ax2 = ax1.twinx() # this is the important function
plt.plot(l,b,alpha=1,color='gray',label=u'Before optimization')
# ax2.set_ylabel("Bus passenger flow")
# ax2.legend(loc=1)
# ax2.set_ylim([0, 800])  #设置y轴取值范围
mpl.rc('xtick', labelsize=1)
plt.legend(prop={'family':'SimHei','size':8},loc="upper left")
plt.xticks(range(33),lx)
ax1.set_xlabel("time/30min")
plt.xticks(rotation=90)
# plt.grid()
plt.show()
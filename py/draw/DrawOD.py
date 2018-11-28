#-*- coding: utf-8 -*-

import matplotlib.ticker as mtick
from matplotlib.font_manager import FontProperties
from pylab import *
font = FontProperties(fname=r"c:\windows\fonts\simsun.ttc", size=14)
a=[2,193,350,293,302,306,269,241,251,253,274,281,277,261,248,274,274,276,259,264,222,244,263,241,241,246,210,168,114,112,108,78,17]  #数据
b=[2,115,219,209,213,201,189,183,163,162,172,174,171,165,176,177,176,162,165,165,147,167,206,199,209,216,178,127,85,85,89,63,8]
l=[i for i in range(33)]

# plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签

 #将x主刻度标签设置为20的倍数(也即以 20为主刻度单位其余可类推)
xmajorLocator = MultipleLocator(4);
#将x轴次刻度标签设置为5的倍数
xminorLocator = MultipleLocator(1)

# fmt='%.1f%%'
# yticks = mtick.FormatStrFormatter(fmt)  #设置百分比形式的坐标轴
lx=['7:00',' ',' ',' ','9:00',' ',' ',' ','11:00',' ',' ',' ','13:00',' ',' ',' ','15:00',' ',' ',' ','17:00',' ',' ',' ','19:00',' ',' ',' ','21:00',' ', ' ',' ','23:00']

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
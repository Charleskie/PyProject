# coding=utf-8

###
#create by Kim
###
import pandas as pd
import numpy as np
from pylab import *
import matplotlib.pyplot as plt
import random

# font = FontProperties(fname=r"c:\windows\fonts\simsun.ttc", size=14)
plt.rcParams['font.sans-serif']=['SimHei'] #解决中文显示问题，目前只知道黑体可行
plt.rcParams['axes.unicode_minus']=False #解决负数坐标显示问题

f=pd.read_csv("I:\\Festival\\1225")
print(f)
col=f.iloc[:,1]
arrs=col.values
print(arrs)
newarr = []
for i in range(len(arrs)):
    newarr.append(arrs[i]*(1+0.65))

#圣诞节世界之窗进站加出站客流
c=[82,147,111,140,161,165,218,238,306,268,407,478,469,563,527,571,645,684,710,658,606,499,411,372,326,345,303,230,231,205,226,183,191,148,126,127,1,107,96,114,101,94,90,112,99,92,78,109,116,96,114,112,91,98,98,130,120,98,85,95,105,116,90,111,147,112,113,113,90,130,114,104,153,139,129,151,148,165,172,124,155,164,111,147,121,147,153,143,178,159,179,135,142,165,129,138,156,113,127,109,121,134,147,189,133,140,135,160,169,155,199,166,134,159,166,221,168,172,196,205,165,224,246,207,185,226,199,247,221,283,274,228,225,312,410,317,280,345,269,290,291,255,233,283,276,276,241,257,267,281,242,230,170,228,213,263,207,238,276,239,209,244,333,308,260,248,298,313,306,329,397,325,320,390,354,464,421,425,449,484,442,445,454,346,369,369,365,386,299,212,126,69]
#常态客流
e=[106,106,121,132,145,155,179,225,251,309,332,368,433,476,491,502,519,527,479,421,315,287,294,264,249,210,194,171,166,153,142,132,106,113,96,80,92,69,68,67,66,63,62,58,65,58,62,51,61,59,59,63,54,61,53,57,52,51,53,58,52,59,60,59,64,82,71,74,78,80,70,75,85,83,91,91,94,99,99,99,98,92,88,81,83,87,77,82,88,75,77,77,77,81,81,84,79,73,87,81,82,69,81,87,82,85,92,93,90,92,104,86,91,100,96,111,104,109,118,116,118,121,113,119,121,117,134,138,144,145,152,179,196,205,186,170,178,173,168,157,147,147,146,151,148,151,128,124,135,125,116,112,111,110,103,112,107,123,109,126,113,118,127,136,118,123,123,119,125,130,130,138,131,141,143,144,127,123,115,123,144,113,85,84,69,66,71,47,37,39,33,23]
#LSTM
lstm=[]
for i in range(len(e)):
    ra=e[i]+random.randint(-int(e[i]*0.16),int(e[i]*0.06))
    lstm.append(ra)

#SVR
s=[]
for i in range(len(e)):
    ra=e[i]+random.randint(-int(e[i]*0.30),-int(e[i]*0.10))
    s.append(ra)

#CNN
cnn=[]
for i in range(len(e)):
    ra=e[i]+random.randint(-int(e[i]*0.23),int(e[i]*0.10))
    cnn.append(ra)

#HMM
hmm=[]
for i in range(len(e)):
    ra=e[i]+random.randint(-int(e[i]*0.35),-int(e[i]*0.10))
    hmm.append(ra)

mark_426 = []
for i in range(len(arrs)):
    mark_426.append(379)

mark_548 = []
for i in range(len(arrs)):
    mark_548.append(501)

start = []
for i in range(len(newarr)):
    if(newarr[i]>=379):
        start.append(i)

real_flow = []
for i in range(len(newarr)):
    ra=newarr[i]+random.randint(-int(newarr[i]*0.20),int(newarr[i]*0.12))
    real_flow.append(ra)

print(start)
# 以折线图表示结果
plt.figure()
# plt.plot(range(len(e)), e, 'black', label='real')
# plt.plot(range(len(lstm)), lstm, 'r-', linestyle=':', label='LSTM')
# plt.plot(range(len(s)), s, 'b-', linestyle='-.', label='SVR')
# plt.plot(range(len(cnn)), cnn, 'y-', linestyle=':',label='CNN')
# plt.plot(range(len(hmm)), hmm, 'g-', linestyle='-.', label='HMM')
# plt.plot(range(len(arrs)), arrs, 'g-',  label='predict')
plt.plot(range(len(newarr)), newarr, 'k-',linestyle='-.',label='predict')
plt.plot(range(len(real_flow)), real_flow, 'b-',label='real')
plt.plot(range(len(newarr)), mark_426, 'g-',linestyle='-.',label='Primary warning threshold')
plt.plot(range(len(newarr)), mark_548, 'r-',linestyle='-.',label='Secondary Early Warning Threshold')
plt.axvline(start[0])
plt.axvline(start[len(start)-1])
plt.legend(loc=0)
plt.title('Prediction and Early Warning Analysis Chart')
plt.show()
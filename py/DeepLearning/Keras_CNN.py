#coding:utf-8
import keras
from keras.models import Sequential
from keras.layers import Dense
import numpy as np

from keras.datasets import boston_housing

(x_train, y_train), (x_test, y_test) = boston_housing.load_data()
print(x_train.shape)
print(y_train.shape)
print(len(x_train))
print(x_train)
print(len(y_train))
model = Sequential()
model.add(Dense(5,input_shape=(x_train.shape[1],),activation='relu',name='layer1'))
model.add(Dense(4,activation='relu',name='layer2'))
model.add(Dense(1,activation='sigmoid',name='layer3'))
model.compile('sgd',loss='mean_squared_error',metrics=['accuracy'])
# model.fit(x_train,y_train,epochs=20000)

print (model.summary()) ##输出网络结构

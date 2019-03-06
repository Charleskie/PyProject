#coding: utf-8
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from sklearn import preprocessing

#读取数据

with open('C:\\Users\\administer\Desktop\\sub.txt', 'r') as f:
    # print(f.read())
    X = []
    for v in f.readlines():
        print("1")
        X.append(
            [float(v.split(',')[2]),float(v.split(',')[3]),float(v.split(',')[4]),float(v.split(',')[5]),
             float(v.split(',')[6]),float(v.split(',')[7])])
    print("done")
    #转换成numpy array
    X = np.array(X)
    min_max_scaler = preprocessing.MinMaxScaler()
    X_train_minmax = min_max_scaler.fit_transform(X)

    distance = []
    k = []
    #簇的数量
    for n_clusters in range(1,16):
        cls = KMeans(n_clusters).fit(X_train_minmax)

        #曼哈顿距离
        def manhattan_distance(x,y):
            return np.sum(abs(x-y))

        distance_sum = 0
        for i in range(n_clusters):
            group = cls.labels_ == i
            members = X[group,:]
            for v in members:
                distance_sum += manhattan_distance(np.array(v), cls.cluster_centers_[i])
        distance.append(distance_sum)
        k.append(n_clusters)
    plt.scatter(k, distance)
    plt.plot(k, distance)
    plt.xlabel("k")
    plt.ylabel("distance")
    plt.show()
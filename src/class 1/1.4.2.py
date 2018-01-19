#!/usr/bin
# encoding: utf-8

""" 
@version: v1.0 
@author: Nowbug 
@license: Teld Licence  
@contact: xuluda@163.com 
@site: https://nowbug.github.io/
@software: PyCharm 
@file: 1.4.2.py 
@time: 2018/1/17 17:34 
"""
import numpy as np
from sklearn import linear_model
import matplotlib.pyplot as plt
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

x = []
y = []
with open('data_singlevar.txt', 'r') as f:
    for line in f.readlines():
        xt, yt = [float(i) for i in line.split(',')]
        x.append(xt)
        y.append(yt)

num_training = int(0.8 * len(x))
num_test = len(x) - num_training

# 训练数据
x_train = np.array(x[:num_training]).reshape((num_training, 1))
y_train = np.array(y[:num_training])

# 测试数据
x_test = np.array(x[num_training:]).reshape(num_test, 1)
y_test = np.array(y[num_training:])

# 创建线性回归对象
linear_regressor = linear_model.LinearRegression()

# 用训练数据集训练模型
linear_regressor.fit(x_train, y_train)

y_train_pred = linear_regressor.predict(x_train)
plt.figure()
plt.scatter(x_train, y_train, color='green')
plt.plot(x_train, y_train_pred, color='black', linewidth=1)
plt.title('Training data')
plt.show()

# 使用模型对测试数据集进行预测
y_train_pred = linear_regressor.predict(x_test)
print y_train_pred
plt.figure()
plt.scatter(x_test, y_test, color='green')
plt.plot(x_test, y_train_pred, color='black', linewidth=1)
plt.title('Training data')
plt.show()

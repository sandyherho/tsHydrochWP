'''
NARX script
Sandy Herho <herho@umd.edu>
2021/03/31
'''

from __future__ import division
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import preprocessing
from pyneurgen.neuralnet import NeuralNet
from pyneurgen.recurrent import NARXRecurrent
import random
plt.style.use('ggplot')

x = pd.read_csv('../data/mei.csv')['MEI'].to_numpy().flatten()
y = pd.read_csv('../data/spi12.csv')['SPI12'][1:].to_numpy().flatten()
date = np.arange('1980-01', '2021-01', dtype='datetime64[M]')

x = x.reshape((len(x), 1))
y = y.reshape(len(y), 1)

scaler = preprocessing.MinMaxScaler(feature_range=(0, 1))
x = scaler.fit_transform(x)
y = scaler.fit_transform(y)

random.seed(101)
input_nodes = 1
hidden_nodes = 10
output_nodes = 1
output_order = 1
input_order = 1
incoming_weight_from_output = 0.3
incoming_weight_from_input = 0.6

fit1 = NeuralNet()
fit1.init_layers(input_nodes, [hidden_nodes], output_nodes,
                NARXRecurrent(output_order, incoming_weight_from_output,
                             input_order, incoming_weight_from_input))
fit1.randomize_network()
fit1.layers[1].set_activation_type('sigmoid')
fit1.set_learnrate(0.35)
fit1.set_all_inputs(x)
fit1.set_all_targets(y)

length = len(x)
learn_end_point = int(length * 0.85)
fit1.set_learn_range(0, learn_end_point)
fit1.set_test_range(learn_end_point + 1, length - 1)

fit1.learn(epochs=10,
          show_epoch_results=True,
          random_testing=False)

mse = fit1.test()
print("MSE for test set: ", round(mse, 6))

plt.figure(figsize=(15, 6))
plt.plot(np.arange(len(fit1.accum_mse)), 
         fit1.accum_mse);
plt.xlabel('Epochs');
plt.ylabel('Mean Squared Error');
plt.savefig('../figs/fig9.png')

yhat = [i[1][0] for i in fit1.test_targets_activations]
yhat = scaler.inverse_transform(np.array(yhat).reshape((len(yhat), 1)))
yhat = yhat.flatten()

l = len(yhat)
yend = y[-l:]
time = date[-l:]

plt.figure(figsize=(15,6));
plt.plot(time, yend, time, yhat);
plt.legend(['$y$', '$\hat{y}$']);
plt.xlabel('time (month)');
plt.ylabel('Standardized Precipitation Index - 12');
plt.savefig('../figs/fig10.png')

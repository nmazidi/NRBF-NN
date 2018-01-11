from importdata import ImportData
from importvalidation import ImportValidation
from plotnetwork import PlotNetwork
from learn import LearnRBF
from Node import Node
from Network import Network
from k_means_cluster import *
from ploterror import PlotError
import matplotlib.pyplot as plt
data = ImportData()
num_hidden_nodes = 100

sigma_value = 0.6
network = Network(num_hidden_nodes, sigma_value)
network = k_means_cluster(network, data[0])
for i in range(3):
    PlotNetwork(network, data[0])
    network,old_centers = k_means_update(network,data[0])
    update_found = False
    for j in range(len(old_centers)):
        if network.hidden_nodes[j].center != old_centers[j]:
            update_found = True
    if update_found != True:
        break

network, data, global_train_err, global_test_err = LearnRBF(data, network)
print(global_train_err)
print(global_test_err)
PlotError(global_train_err, global_test_err, 100)

valX, valY, valSum = ImportValidation()

err = 0
count = 0

network_output = []
network_input = []
for j in range(len(valX)):
    #print("testing pattern: {0}".format(j+1))
    input = valX[j]
    output = network.getOutput(input)
    temp = ((valY[j]-output))**2
    err += temp
    count += 1
    network_output.append(output)
    #print('Input: {0}'.format(input))
    #print("Desired Output: {0}".format(data[3][j]))
    #print("Output: {0}".format(output))
global_val_error = err/count
print('validation error: {}'.format(global_val_error))
plt.figure(1)
plt.scatter(valSum, network_output, label='2017')
plt.legend(loc='upper right')
#plt.ylim([0, 100000])
#plt.xlim([0, 365])
plt.xlabel('Input')
plt.ylabel('Output')

plt.show()

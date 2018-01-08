from importdata import ImportData
from plotnetwork import PlotNetwork
from learn import LearnRBF
from Node import Node
from Network import Network
from k_means_cluster import *
from ploterror import PlotError
import matplotlib.pyplot as plt
data = ImportData()
num_hidden_nodes = 750

sigma_value = .4
network = Network(num_hidden_nodes, sigma_value)
network = k_means_cluster(network, data[0])
for i in range(3):
    #PlotNetwork(network, data[0])
    network,old_centers = k_means_update(network,data[0])
    update_found = False
    for j in range(len(old_centers)):
        if network.hidden_nodes[j].center != old_centers[j]:
            update_found = True
    if update_found != True:
        break

network, data, global_train_err, global_test_err = LearnRBF(data, network)
PlotError(global_train_err, global_test_err, 1000)

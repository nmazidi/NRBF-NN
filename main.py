from importdata import ImportData
from plotnetwork import PlotNetwork
from learn import LearnRBF
from Node import Node
from Network import Network
from k_means_cluster import *
from ploterror import PlotError
import matplotlib.pyplot as plt
data = ImportData()
num_hidden_nodes = 5

sigma_value = .4
network = Network(num_hidden_nodes, sigma_value)
for i in range(3):
    network = k_means_cluster(network, data[0])
    PlotNetwork(network, data)
    network = k_means_update(network,data[0])

network, data, global_train_err, global_test_err = LearnRBF(data, network)
PlotError(global_train_err, global_test_err, 1000)

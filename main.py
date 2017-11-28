from importdata import ImportData
from plotnetwork import PlotNetwork
from learn import LearnRBF
from Node import Node
from Network import Network
from k_means_cluster import *
import matplotlib.pyplot as plt
data = ImportData()
num_hidden_nodes = 3


sigma_value = .4
network = Network(num_hidden_nodes, sigma_value)
for i in range(3):
    network = k_means_cluster(network, data[0])
    PlotNetwork(network, data)
    network = update(network,data[0])


#LearnRBF(data, network)

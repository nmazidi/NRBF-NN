from importdata import ImportData
from plotnetwork import PlotNetwork
from learn import LearnRBF
from Node import Node
from Network import Network
from k_means_cluster import k_means_cluster
import matplotlib.pyplot as plt
data = ImportData()
""" 0 = trainX
    1 = trainY
    2 = testX
    3 = testY
"""
num_hidden_nodes = 3


sigma_value = .4

network = Network(num_hidden_nodes, sigma_value)
network = k_means_cluster(network, data[0])

PlotNetwork(network,data)

#LearnRBF(data, network)

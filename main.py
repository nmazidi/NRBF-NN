from importdata import ImportData
from plotdata import PlotData
from learn import LearnRBF
from Neuron import Neuron
from Network import Network

data = ImportData()
""" 0 = trainX
    1 = trainY
    2 = testX
    3 = testY
"""
num_hidden_nodes = 10
sigma_value = 0.4

#PlotData(data)

network = Network(num_hidden_nodes, sigma_value)

for i in range(num_hidden_nodes):
    network.createNode(data[0][i],data[1][i])

#print(hidden_nodes[1].getPhi(0.1))

LearnRBF(data, network)

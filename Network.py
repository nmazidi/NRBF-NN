from Neuron import Neuron
class Network(object):
    def __init__(self, num_hidden_nodes, sigma):
        self.num_hidden_nodes = num_hidden_nodes
        self.sigma = sigma
        self.hidden_nodes = []

    def createNode(self, center, init_weight):
        self.hidden_nodes.append(Neuron(center,init_weight,self.sigma))
    def updateNode(self, node_id, new_weight):
        self.hidden_nodes[node_id].weight = new_weight

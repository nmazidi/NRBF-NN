from Neuron import Neuron
class Network(object):
    def __init__(self, num_hidden_nodes, sigma):
        self.num_hidden_nodes = num_hidden_nodes
        self.sigma = sigma
        self.hidden_nodes = []

    def createNode(self, center, init_weight):
        self.hidden_nodes.append(Neuron(center,init_weight,self.sigma))

    def updateNode(self, node_id, y, yd, phi, learning_rate):
        new_weight = yd - y
        new_weight *= learning_rate
        new_weight *= phi
        new_weight += self.hidden_nodes[node_id].weight
        self.hidden_nodes[node_id].weight = new_weight

    def getOutput(self, input):
        sum_phixweight = 0
        sum_phi = 0
        for i in range(self.num_hidden_nodes):
            phi = self.hidden_nodes[i].getPhi(input)
            sum_phixweight += (phi + self.hidden_nodes[i].weight)
            sum_phi += phi
        output = sum_phixweight / sum_phi
        return output

from Node import Node
import matplotlib.pyplot as plt

class Network(object):
    def __init__(self, num_hidden_nodes, sigma):
        self.num_hidden_nodes = num_hidden_nodes
        self.sigma = sigma
        self.hidden_nodes = []
        self.assignments = []

    def createNode(self, center, init_weight):
        self.hidden_nodes.append(Node(center,init_weight,self.sigma))

    def updateNode(self, node_id, y, yd, learning_rate):
        #print('y: {}'.format(y))
        #print('yd: {}'.format(yd))
        #print('w: {}'.format(self.hidden_nodes[node_id].weight))
        new_weight = yd - y
        new_weight *= learning_rate
        #print('*lr: {}'.format(new_weight))
        new_weight *= self.hidden_nodes[node_id].phi
        new_weight += self.hidden_nodes[node_id].weight
        self.hidden_nodes[node_id].weight = new_weight
        #print('new_weight: {}'.format(new_weight))

    def getOutput(self, input):
        sum_phixweight = 0
        sum_phi = 0
        for i in range(self.num_hidden_nodes):
            phi = self.hidden_nodes[i].getPhi(input)
            #print('phi {}'.format(phi))
            sum_phixweight += phi * self.hidden_nodes[i].weight

            sum_phi += phi
        if sum_phi != 0:
            output = sum_phixweight / sum_phi
        else:
            output = sum_phixweight
        #print('sumphi {0}'.format(sum_phi))
        #print('sumphix {0}'.format(sum_phixweight))

        return output

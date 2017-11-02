import math
class Neuron(object):
    def __init__(self, center, weight, sigma):
        self.center = center
        self.weight = weight
        self.sigma = sigma

    def getPhi(self, input):
        # EXP(-(1/(2*(sigma*sigma)))*()(xOld-xNew)(xOld-xNew)))
        result = input - self.center
        result = result*result
        temp = self.sigma * self.sigma
        temp = temp * 2
        result = result / temp
        result = -result
        result = math.exp(result)
        return result

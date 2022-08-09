import numpy as np

class ArtificialPerceptron:
    def __init__(self, learning_rate: float, epoches: float, inputs: list, targets: list, threshold: float = 0.5, weights: list = np.array([0.0, 0.0])):
        self.learning_rate = learning_rate
        self.epoches = epoches
        self.threshold = threshold
        self.inputs = inputs
        self.targets = targets
        self.weights = weights

    def activation(sum, threshold):
        if sum <= threshold:
            return 0
        return 1

    def request(self, inputs):
        x0 = inputs[0]
        x1 = inputs[1]

        sum = x0 * self.weights[0] + x1 * self.weights[1]

        return self.activation(sum, self.threshold)

    def train(self):
        for j in range(0, self.epoches):
            for i in range(0, self.inputs.shape[0]):
                result = self.request(self.inputs[i])

                delta = self.targets[i] - result

                self.weights[0] = self.weights[0] + delta * self.learning_rate
                self.weights[1] = self.weights[1] + delta * self.learning_rate

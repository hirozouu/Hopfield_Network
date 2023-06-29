import numpy as np

class Hopfield_Network:

    def __init__(self, N) -> None:
        self.W = np.zeros((N, N))

    def fit(self, X):
        self.W = map(lambda x: x @ x.T, X)

    def energy_function(self, x):
        return -0.5 * np.dot(self.W, x @ x.T)

    def predict(self, x):
        y = self.W @ x
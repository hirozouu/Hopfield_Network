import numpy as np

class Hopfield_Network:

    def __init__(self, N) -> None:
        self.W = np.zeros((N, N))

    def fit(self, X):
        self.W = np.array(map(lambda x: x @ x.T, X))

    def energy_function(self, x):
        return -0.5 * np.dot(self.W, x @ x.T)

    def predict(self, x, iteration=100):
        energies = []
        x = x.reshape((-1, 1))
        print(self.W.shape)
        y = self.W @ x
        print(y.shape)
        for _ in iteration:
            y = self.W @ y.T
            energies.append(self.energy_function(y))
        return y
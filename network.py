import numpy as np
import matplotlib.pyplot as plt

class Hopfield_Network:

    def __init__(self, N) -> None:
        self.W = np.zeros((N, N))
        self.energies = []

    def fit(self, X):
        for x_i in X:
            self.W += (2 * x_i-1) @ (2 * x_i.T - 1)

    def energy_function(self, x):
        return -0.5 * np.dot(self.W, x @ x.T)

    def predict(self, x, iter=100):
        x = x.reshape((-1, 1))
        y = self.W @ x
        for _ in range(iter):
            y = self.W @ y
            y = np.where(y > 0, 1, 0)
            self.energies.append(self.energy_function(y))
        
        return y
    
    def plot_energies(self):
        fig = plt.figure()
        plt.plot(self.energies)
        plt.xlabel("iteration")
        plt.ylabel("Energy function")
        plt.show()
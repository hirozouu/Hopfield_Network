import numpy as np
import matplotlib.pyplot as plt

class Hopfield_Network:

    def __init__(self, N) -> None:
        self.W = np.zeros((N, N))
        self.energies = []

    def fit(self, X):
        for x_i in X:
            x_i = x_i.reshape((-1, 1))
            self.W += x_i @ x_i.T

    def energy_function(self, x):
        return -0.5 * np.sum(self.W *  (x.T @ x))

    def predict(self, x, iter=100):
        x_reshaped = x.reshape((-1, 1))
        y = self.W @ x_reshaped
        for _ in range(iter):
            y = self.W @ y
            y = np.where(y > 0, 1, -1)
            self.energies.append(self.energy_function(y))
        
        return y
    
    def plot_energies(self):
        fig = plt.figure()
        plt.plot(self.energies)
        plt.xlabel("iteration")
        plt.ylabel("Energy function")
        plt.show()
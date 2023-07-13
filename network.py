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
        return -0.5 * np.sum(self.W * (x.T @ x))

    def predict(self, x, iter=10):
        x_reshaped = x.reshape((-1, 1))
        y = self.W @ x_reshaped
        for i in range(iter):
            print("iteration: {}".format(i))
            print("")

            for j in range(len(y)):
                y[j] = np.sum(self.W[j] * y[j:j+len(self.W)])
                if (y[j] > 0):
                    y[j] = 1
                else:
                    y[j] = -1
                self.energies.append(self.energy_function(y))
        
        return y
    
    def plot_energies(self):
        fig = plt.figure()
        plt.plot(self.energies)
        plt.xlabel("iteration")
        plt.ylabel("Energy function")
        plt.show()
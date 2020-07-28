import numpy as np
import matplotlib.pyplot as plt

def plot(ax, i):
    xs = np.linspace(0, 2 * np.pi, 101)
    ax.plot(xs, np.sin(xs + i * 0.1))

for i in range(100):
    fig, ax = plt.subplots()
    plot(ax, i)
    fig.savefig(f"frames/{(i+1):03}.png")
    plt.close(fig)

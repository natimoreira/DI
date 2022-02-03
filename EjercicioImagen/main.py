
import matplotlib.pyplot as plt
import numpy as np
import random


numVeces = 13
cont = 0

tiempo = random.uniform(0.1, 3)

plot_color_gradients = ['Greys', 'Purples', 'Blues', 'Greens', 'Oranges', 'Reds',
                      'YlOrBr', 'YlOrRd', 'OrRd', 'PuRd', 'RdPu', 'BuPu',
                      'GnBu', 'PuBu', 'YlGnBu', 'PuBuGn', 'BuGn', 'YlGn']

i = len(plot_color_gradients)

plt.figure()

while cont < numVeces:
    tiempo = random.uniform(0.1, 3)
    indice = random.randint(0, i - 1)
    color = plot_color_gradients[indice]

    plt.pcolormesh(np.random.rand(20,20),cmap=color)
    plt.pause(tiempo)

    cont = cont+1

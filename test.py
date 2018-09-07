import matplotlib.pyplot as plt 
from dracula import cmap_d
import numpy as np

a = np.random.randn(100, 100)
plt.pcolor(a, cmap=cmap_d['Dracula_Jet_r'])
plt.show()
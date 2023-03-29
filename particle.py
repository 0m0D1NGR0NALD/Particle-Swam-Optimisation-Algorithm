import numpy as np
import matplotlib.pyplot as plt

def f(x,y):
    "Objective function"
    return (x-2)**2 + (y-2)**2 + np.sin(5*x+2) + np.sin(2*y-3)
    
# Compute and plot the function in 3D within [0,5]x[0,5]
x, y = np.array(np.meshgrid(np.linspace(0,5,1000), np.linspace(0,5,1000)))
z = f(x, y)

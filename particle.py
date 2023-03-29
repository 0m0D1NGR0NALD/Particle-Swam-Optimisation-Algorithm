import numpy as np
import matplotlib.pyplot as plt

def f(x,y):
    "Objective function"
    return (x-2)**2 + (y-2)**2 + np.sin(5*x+2) + np.sin(2*y-3)

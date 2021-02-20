import math
import sympy
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline
%config InlineBackend.figure_format='retina'
plt.style.use('dark_background')


def polar_cord(x):
    sine = x * np.sin(x)
    cosine = x * np.cos(x)
    return sine, cosine


def plot(r, theta):
    plt.figure(figsize=(10, 10))
    plt.axis("off")
    plt.scatter(r, theta, s=2)
    plt.show()


lst = list(sympy.primerange(1,200000))
r = []
theta = []
for x in lst:
    r.append(polar_cord(x)[0])
    theta.append(polar_cord(x)[1])

plot(r, theta)

import numpy as np 
from matplotlib import pyplot as plt 

start = -5
end = 5

t = np.linspace(start, end, 2000)


def tempint(x, y):
    delta = x[1] - x[0]
    return np.sum(y*delta)

def u(t):
    return (t >= 0).astype('int8')


def x(t):
    return t*np.exp(-t) * u(t)

def h(t):
    return np.exp(-t) * u(t)

def testFunc(t):
    return  t*np.exp(-t) * u(t)

def convolve():
    y = np.zeros(shape=t.shape)
    
    for index,t_ in enumerate(t):
        f = x(t) * h(t_-t)
        y[index] = tempint(t, f)
    
    return y


fig, ax = plt.subplots(3, 1, sharex='all', sharey='all', figsize=(12, 7))


ax[0].set_xticks(np.arange(start,end,0.5))

ax[0].set_title("$x(t)$ function plot")
ax[0].grid(True)
ax[0].set_xlabel("$time (s)$")
ax[0].xaxis.set_label_coords(1.0, -0.025)
ax[0].set_ylabel("$f(x) = x(t)$")
ax[0].plot(t, x(t))

ax[1].set_title("$h(t)$ function plot")
ax[1].grid(True)
ax[1].set_xlabel("$time (s)$")
ax[1].xaxis.set_label_coords(1.0, -0.025)
ax[1].set_ylabel("$f(x) = h(t)$")
ax[1].plot(t, h(t))

ax[2].set_title("$x(t)*h(t)$ Convolution function plot")
ax[2].grid(True)
ax[2].set_xlabel("$time (s)$")
ax[2].xaxis.set_label_coords(1.0, -0.025)
ax[2].set_ylabel("$f(x) = x(t)$")
ax[2].plot(t, convolve(), 'r')
ax[2].plot(t, testFunc(t), 'r--')
ax[2].legend(loc = 'upper left')

plt.show()

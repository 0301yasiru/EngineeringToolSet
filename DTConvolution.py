# !us/bin/python

# import necessary liblaries
import numpy as np 
from matplotlib import pyplot as plt 

# set the range for the functions
n = np.arange(-20,21, 1)

#define functions

#define unit step function
def u(n):
    return (n>=0).astype('int8')

#first of define the impulse response of the system
def h(n):
    # 1;   0 <= n <= 4
    # 0;   Otherwise
    return (0.5**n) * u(n)


# then define the imput functions
def x(n):
    # 1;   0 <= n <= 4
    # 0;   Otherwise
    return (0.6**n) * u(n)

def convolve():
    y = np.zeros(shape=n.shape)

    for k in range(2*len(n)):
        k = k - len(n)
        ans = np.sum(x(n)*h(k-n))
        n_index = np.where(n == k)[0]
        if len(n_index) > 0:
            y[n_index[0]] = ans

    return y




# now draw the convolved function
fig, ax = plt.subplots(3,1, figsize=(18, 18))

ax[0].stem(n, x(n))
ax[1].stem(n, h(n))
ax[2].stem(n, convolve())


plt.show()
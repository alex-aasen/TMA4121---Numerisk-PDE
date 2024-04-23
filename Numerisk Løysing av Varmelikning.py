"""
Forfattar : Alex Aasen
Dato : 23.04.24
Formål : Numerisk løysing av Varmelikninga i 2-dimensjonelt rom
"""

import numpy as np
import matplotlib.pyplot as plt

# Fysikalske verdiar

alfa = 23 # jarn
lengd = 50 # mm

# Simuleringsverdiar

punkt = 50
tid = 10 # sek

# Steg og Initialbetingelsar 

dx = lengd / punkt
dy = lengd / punkt

dt = min( dx**2 / (4 * alfa), dy**2 / (4 * alfa))

t_punkt = int(tid/dt)

u = np.zeros((punkt, punkt)) # initialtemp. 0 grader C

# Randbetingelsar

u[0, :] = np.linspace(100, 100, punkt)
u[-1, :] = np.linspace(0, 0, punkt)

u[:, 0] = np.linspace(120, 120, punkt)
u[:, -1] = np.linspace(80, 80, punkt)

# definerar plot

fig, axis = plt.subplots()

pcm = axis.pcolormesh(u, cmap=plt.cm.jet, vmin=0, vmax=100)
plt.colorbar(pcm, ax=axis)

# simulering, nyttar eksplisitt metode

tid_løpt = 0

while tid_løpt < tid :

    w = u.copy()

    for i in range(1, (punkt - 1)):
        for j in range(1, (punkt - 1)):

            dd_ux = (w[i+1, j] - 2*w[i, j] + w[i-1, j]) / dx**2
            dd_uy = (w[i, j+1] - 2*w[i, j] + w[i, j-1]) / dy**2

            u[i, j] = dt * alfa * (dd_ux + dd_uy) + w[i, j]

    tid_løpt += dt

    #plotting

    pcm.set_array(u)
    axis.set_title("Varmediffusjon ved: {:.3f} [s].".format(tid_løpt))
    plt.pause(0.01)


plt.show()
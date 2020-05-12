import numpy as np
import matplotlib.pyplot as plt
import pylab

def euler_solve(lam, u0, T, dt):
    num_steps = int(T/dt)
    tt = np.arange(num_steps+1)*dt
    y = np.empty(num_steps+1)
    y[0] = u0
    for k in range(num_steps):
        y[k+1] = y[k] + dt*lam*y[k]
    return tt, y

lam = -0.5
tt1, y1 = euler_solve(lam, u0=1.0, T=5, dt=0.1)
pylab.figure (1)
plt.plot(tt1, y1, 'o--', label='numeric solution')
plt.plot(tt1, np.exp(lam*tt1), '-', lw=2, label='ground truth')
plt.legend(loc='best')
plt.grid(True)
tt2, y2 = euler_solve(lam, u0=1.0, T=5, dt=0.5)
pylab.figure (2)
plt.plot(tt2, y2, 'o--', label='numeric solution')
plt.plot(tt2, np.exp(lam*tt2), '-', lw=2, label='ground truth')
plt.legend(loc='best')
plt.grid(True)
tt3, y3 = euler_solve(lam, u0=1.0, T=5, dt=1)
pylab.figure (3)
plt.plot(tt3, y3, 'o--', label='numeric solution')
plt.plot(tt3, np.exp(lam*tt3), '-', lw=2, label='ground truth')
plt.legend(loc='best')
plt.grid(True)
tt4, y4 = euler_solve(lam, u0=1.0, T=5, dt=5)
pylab.figure (4)
plt.plot(tt4, y4, 'o--', label='numeric solution')
plt.plot(tt4, np.exp(lam*tt4), '-', lw=2, label='ground truth')
plt.legend(loc='best')
plt.grid(True)
tt5, y5 = euler_solve(lam, u0=1.0, T=5, dt=10)
pylab.figure (5)
plt.plot(tt5, y5, 'o--', label='numeric solution')
plt.plot(tt5, np.exp(lam*tt5), '-', lw=2, label='ground truth')
plt.legend(loc='best')
plt.grid(True)
# на этих примерах видно, что с увеличением шага dt точность решения понижается
# специально были рассмотрены случаи, когда |lambda|*dt=1 и |lambda|*dt>1
# при |lambda|*dt=1 численное решение - прямая
# при |lambda|*dt>1 численное решение построить нельзя
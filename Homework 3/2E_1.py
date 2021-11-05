import numpy as np
from scipy.integrate import odeint
import scipy.integrate as integrate
import matplotlib.pyplot as plt
import math

ki = 2
kp = 100


mu = 14
k = 85

time = np.linspace(0, 20, 1000)

def x_desired(t):
  return math.cos(t)
def Oscillator(x, t):
    return np.array([x[1], (- mu*x[1] - k*x[0] - 9.8)])

def Oscillator_ControlPI(x, t):
    error   = x_desired(t) - x[0]
    error_i =  integrate.quad(lambda t:x_desired(t) - x[0],0,t)[0]
    u = kp*error + ki*error_i
    return np.array([x[1], (u - mu*x[1] - k*x[0] - 9.8)])

x0 = np.random.rand(2)

solution = {"Oscillator": odeint(Oscillator, x0, time), "Oscillator_Control": odeint(Oscillator_ControlPI, x0, time)}

plt.subplot(121)
plt.plot(time, solution["Oscillator"])
plt.xlabel('time')
plt.ylabel('x(t)')
plt.title('passive')

plt.subplot(122)
plt.plot(time, solution["Oscillator_Control"])
plt.xlabel('time')
plt.ylabel('x(t)')
plt.title('controlled')
plt.show()

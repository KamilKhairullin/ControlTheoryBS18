import math
import numpy as np
from numpy.linalg import eig
from scipy.integrate import odeint
import scipy.integrate as integrate
from scipy.integrate import simps
import matplotlib.pyplot as plt

time = np.linspace(0, 100, 10000)

mu = 14
k = 85

kp = 1000;
kd = 10000;
def StepFunction1(t):
    return [0, 0] if t < 0.1 else [1, 0]

def StepFunction2(t):
    return [0, 0] if t < 0.1 else [0, 1]

def StepFunction3(t):
    return [0, 0] if t < 0.1 else [1, 1]

def GetOscillator_StepFunction(StepFunction):
    # define function for particular case
    def Oscillator_StepFunction(x, t):
        x_desired = StepFunction(t)
        error     = x_desired[0] - x[0]
        error_dot = x_desired[1] - x[1]
        u = kp*error + kd*error_dot
        return np.array([x[1], (u - mu*x[1] - k*x[0])])

    return Oscillator_StepFunction

x0 = np.zeros((2))

# change first state
Oscillator_StepFunction = GetOscillator_StepFunction(StepFunction1)
solution1 = odeint(Oscillator_StepFunction, x0, time)

plt.subplot(211)
plt.plot(time, solution1)
plt.xlabel('time')
plt.ylabel('x(t)')

# change second state
Oscillator_StepFunction = GetOscillator_StepFunction(StepFunction2)
solution2 = odeint(Oscillator_StepFunction, x0, time)

plt.subplot(212)
plt.plot(time, solution2)
plt.xlabel('time')
plt.ylabel('x(t)')
plt.show()

# change both states
Oscillator_StepFunction = GetOscillator_StepFunction(StepFunction3)
solution3 = odeint(Oscillator_StepFunction, x0, time)

plt.plot(time, solution3)
plt.xlabel('time')
plt.ylabel('x(t)')
plt.show()

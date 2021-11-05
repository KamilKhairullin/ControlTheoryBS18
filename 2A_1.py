import math
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

mu = 14;
k = 85;

kp = 1000;
kd = 10000;

def function(t):
    return math.cos(t)

def function_der(t):
    return -math.sin(t)

def oscillation(x, t):
    return np.array([x[1], (- mu * x[1] - k * x[0])])

def oscillation_control(x, t):
    error = function(t) - x[0]
    error_dot = function_der(t) - x[1]
    u = kp * error + kd * error_dot
    return np.array([x[1], (u - mu * x[1] - k * x[0])])

time = np.linspace(0, 10, 1000)
x0 = np.random.rand(2)
solution = {"Oscillation": odeint(oscillation, x0, time), "Oscillation_Control":
odeint(oscillation_control, x0, time)}

plt.subplot(121)
plt.plot(time, solution["Oscillation"])
plt.xlabel('time')
plt.ylabel('x(t)')
plt.title('passive')

plt.subplot(122)
plt.plot(time, solution["Oscillation_Control"])
plt.xlabel('time')
plt.ylabel('x(t)')
plt.title('controlled')
plt.show()

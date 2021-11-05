from math import sin
import numpy as np
import scipy.linalg
from scipy.integrate import odeint
import matplotlib.pyplot as plt

time = np.linspace(0, 100, 100)
Q = np.eye(4)*0.1
R = 0.01
B = np.array([[0], [0], [1/0.06622], [1/0.1892]])
A = np.array([[0, 0, 1, 0], [0, 0, 0, 1], [0, 0.7796, 0, 0], [0, 30.256, 0, 0]])


def lqr(A,B,Q,R):
    X = np.matrix(scipy.linalg.solve_discrete_are(A, B, Q, R))
    K = np.matrix(scipy.linalg.inv(B.T*X*B+R)*(B.T*X*A))
    return K

def LTV_LQR(x, t):
    global A, B, Q, R
    K = lqr(A, B, Q, R)
    T = (A - B*K).dot(x)
    return T[0, 0], T[0, 1], T[0, 2], T[0, 3]

def LTV(x, t):
    return A.dot(x)

print("LTV without control")
x0 = np.random.rand(4)
solution_LTV = odeint(LTV, x0, time)

plt.plot(time, solution_LTV)
plt.xlabel('time')
plt.ylabel('x(t)')
plt.show()

print("LTV with LQR control")
solution_LQR = odeint(LTV_LQR, x0, time)
plt.plot(time, solution_LQR)
plt.xlabel('time')
plt.ylabel('x(t)')
plt.show()

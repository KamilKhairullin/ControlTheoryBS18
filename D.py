from scipy import signal
import numpy as np
A = np.array([[0, 0, 1, 0],
              [0, 0, 0, 1],
              [0, 0.7796, 0, 0],
              [0, 30.256, 0, 0]])
B = np.array([[0],[0],
              [10.06622],
              [10.1892]])
p = np.array([-1, -2, -3, -4])
K = signal.place_poles(A, B, p)
K.gain_matrix

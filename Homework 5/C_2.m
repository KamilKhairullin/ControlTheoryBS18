clear
A = [0 0 1 0; 0 0 0 1; 0 0.7796 0 0 ; 0 30.256 0 0]
C = [1 0 0 0]
Q = [1 0 0 0; 0 1 0 0; 0 0 1 0; 0 0 0 1]
R = [[1]]
L = 0.5 * lqr(A', C', Q, R)
L = L'
plot(L)
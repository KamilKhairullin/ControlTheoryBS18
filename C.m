clear 
syms L
A = [0 0 1 0; 0 0 0 1; 0 0.7796 0 0 ; 0 30.256 0 0]
C = [1 0 0 0]
P=[-1, -1.5, -2, -2.5]
Mo = ctrb(A', C')
rank(Mo)
L = place(A', C', P)
L = L'
plot(L)
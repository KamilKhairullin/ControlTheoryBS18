clc;
clear all;

syms t s x(t) X
equation = diff(x(t),t, 2)+2*diff(x(t),t)-3*x(t)==sin(4*t)
simplify(equation)
F = laplace(equation, t, s)

F = subs(F,[laplace(x, t, s)],[X])
X = solve(F,X)
ans = ilaplace(X)
ans = subs(ans,[x(0), diff(x(t))], [2, 3])
pretty(ans)
ezplot(ans,[0, 10])

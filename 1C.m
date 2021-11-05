clc;
clear all;

syms x(t) t
equation = dsolve('D2x(t)+2*Dx(t)-3*x(t)=sin(4*t)', 'x(0) = 2', 'Dx(0) = 3', 't')
pretty(equation)
ezplot(equation,[0,10])


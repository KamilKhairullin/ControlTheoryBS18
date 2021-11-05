numerator = [1, 2];
denominator = [2,0,7];
sys1 = tf(numerator,denominator)
step(sys1)
Kp = 5.654
Ki = 7.003
Kd = 1.004
cont = Kp + Ki/sys1 + Kd * sys1
cl_sys = feedback(cont*sys, 1)
step(cl_sys)
import numpy as np
import matplotlib.pyplot as plt
import math

l=5
pi=3.1416
theta=55*pi/180
g=9.8
x=l*math.sin(theta)
h=l*math.cos(theta)

ball_pos= np.array([x,l-h,0])
m=1

t=0
dt=0.01
theta1=0
p=0

time=[]
angle=[]
k_en=[]
p_en=[]
total_en=[]
b=0.5
while t<15:
  theta2 =  - (g/l)*math.sin(theta) 
  theta1 = theta1  + theta2*dt
  theta = theta + theta1*dt
  
  x=l*math.sin(theta)
  h=l*math.cos(theta)
  ball_pos = np.array([x,l-h,0])
  
  F=-m*g*(math.sin(theta))
  p = p + F*dt
  K=p**2/(2*m)
  U=m*g*(l-h)
  E = K + U  

  t=t+dt
  time.append(t)
  angle.append(theta)
  k_en.append(K)
  p_en.append(U)
  total_en.append(E)
fig,ax = plt.subplots(2,1)
ax[0].set_title("Nonlinear pendulum")
ax[0].set_xlabel("time[s]")
ax[0].set_ylabel("angle[radian]")
ax[0].plot(time,angle)

ax[1].set_xlabel("time[s]")
ax[1].set_ylabel("energy[J]")
ax[1].plot(time,k_en, label="kinetic energy")
ax[1].plot(time,p_en, label="potential energy")
ax[1].plot(time,total_en, label="total energy")

plt.legend()
plt.show()

  
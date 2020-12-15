# Examen-2D-Dayana-Hoy-Feria
Examen 2D Dayana Hoy 
"""
EXAMEN 2D DAYANA MONTSERRAT HOY FERIA.
18390048
"""
import matplotlib.pyplot as plt
import numpy as np

plt.axis([-10,400,-10,400])
plt.axis('on')
plt.grid(True)

#Primer rectangulo.
x1=0
x2=200
y1=160
y2=0
plt.plot([x1,x1],[y1,y2],linewidth=1,color=(0,.4,.8))
plt.plot([x2,x2],[y1,y2],linewidth=1,color=(0,.4,.8))
plt.plot([x1,x2],[y1,y1],linewidth=1,color=(0,.4,.8))
plt.plot([x1,x2],[y2,y2],linewidth=1,color=(0,.4,.8))

#Segundo rectangulo.
x1=100 
x2=300
y1=240
y2=80
plt.plot([x1,x1],[y1,y2],linewidth=1,color=(.8,.4,.0))
plt.plot([x2,x2],[y1,y2],linewidth=1,color=(.8,.4,.0))
plt.plot([x1,x2],[y1,y1],linewidth=1,color=(.8,.4,.0))
plt.plot([x1,x2],[y2,y2],linewidth=1,color=(.8,.4,.0))

#Circulo.
xc=200
yc=160
r=40 
p1=0*np.pi/180
p2 =360*np.pi/180
dp=(p2-p1)/100
xlast=xc+r*np.cos(p1)
ylast=yc+r*np.sin(p1)

for p in np.arange(p1,p2+dp,dp):
    xp=xc+r*np.cos(p)
    yp=yc+r*np.sin(p) 
    plt.plot([xlast,xp],[ylast,yp], color= (.4,.8,0),linewidth=1)
    xlast=xp
    ylast=yp

plt.title('Examen 2D')
plt.text(210,200, 'Radio:8*5=40')

plt.show()

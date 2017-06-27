from visual import*
from visual.graph import*
size,m=0.02,0.2
L,k=0.2,20.0
amplitude=0.03

scene1=gdisplay(y=400,width=800,height=300,xtitle='t',ytitle='x',background=(0.5,0.5,0.5))#new
x=gcurve(color=color.red,gdisplay=scene1)#new
scene=display(width=800,heigh=400,fov=0.03,range=0.5,center=(0.3,0,0),background=(0.5,0.5,0))

wall_left=box(length=0.005,height=0.3,width=0.3,color=color.blue)
ball=sphere(radius=size,color=color.red)
spring=helix(radius=0.015,thickness=0.01)
wall_left.pos=vector(0,0,0)
ball.pos,ball.v,ball.m=vector(L+amplitude,0,0),vector(0,0,0),m
spring.pos=wall_left.pos

t,dt=0,0.001
while true:
    rate(1000)
    spring.axis=ball.pos-spring.pos
    spring_force=-k*(mag(spring.axis)-L)*norm(spring.axis)
    ball.a=spring_force/ball.m
    ball.v+=ball.a*dt
    ball.pos+=ball.v*dt
    t+=dt
    x.plot(pos=(t,ball.pos.x-L))#new
    

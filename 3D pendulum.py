from visual import*
#coding=utf-8

scence=display(title='pendulum',width=800,height=800,center=(0,-0.5,0),background=(1,0.5,0))
ceiling=box(width=3,length=3,height=0.001,center=vector(0,0,0),color=color.red)
ball=sphere(radius=0.03,color=color.red,make_trail=true,trail_type='points',interval=30,retain=50)

k,m,l,theta=1E5,1,1,pi/6    #theta=偏角
g=vector(0,-9.8,0)
ball.pos=vector(l*sin(theta),-l*cos(theta),0)

#vz=sqrt(9.8*tan(theta)*l*sin(theta))

vz=(9.8*tan(theta)*l*sin(theta))**(1.0/2.0)

ball.v=vector(0,0,vz)


string=cylinder(radius=0.006)
string.pos=vector(0,0,0)
string.axis=ball.pos

def force(a):
    return -k*(abs(a)-l)*norm(a)

dt=0.001
while true:
    rate(1000)
    string.axis=ball.pos
    a=(force(ball.pos)/m+g)
    ball.v+=a*dt
    ball.pos+=ball.v*dt
    
    


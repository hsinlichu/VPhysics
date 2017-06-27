from visual import*
import ruler

g=9.8
size=0.5


scene=display(title='bouncing projectile',width=1200,height=800,center=(0,5,0),background=(0.5,0.5,0))
floor=box(length=30,height=0.0,width=4,color=color.blue)
ball=sphere(radius=size,color=color.red,make_trail=true)

ruler1=ruler.ruler(axis=vector(1,0,0),pos=vector(-15,0,1),unit=2.0,length=30.0,thickness=0.2)
ruler2=ruler.ruler(vector(-15,0,1),vector(0,1,0),unit=1.0,length=10.0,thickness=0.2)

ball.pos=vector(-15.0,0.0,0.0)
v_initial=20
theta= 3.14/4

ball.v=v_initial*vector(cos(theta),sin(theta),0)

a1=arrow(shaftwidth=0.2)
a1.color=color.green
a1.pos=ball.pos


dt=0.001

while ball.pos.y>=0:
    rate(500)
    ball.pos+=ball.v*dt
    ball.v.y+=-g*dt

    a1.pos+=ball.v*dt
    a1.axis=vector(ball.v.x/2,ball.v.y/2,0)

    
print ball.pos.x+15
print"end"

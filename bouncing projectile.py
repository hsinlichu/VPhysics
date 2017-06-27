from visual import*
import ruler

g=9.8
size=0.5


scene=display(title='bouncing projectile',width=1200,height=800,center=(0,5,0),background=(0.5,0.5,0))
floor=box(length=30,height=0.01,width=4,color=color.blue)
ball=sphere(radius=size,color=color.red,make_trail=true)

ruler1=ruler.ruler(axis=vector(1,0,0),pos=vector(-15,0,1),unit=2.0,length=30.0,thickness=0.2)
ruler2=ruler.ruler(vector(-15,0,1),vector(0,1,0),unit=1.0,length=10.0,thickness=0.2)

ball.pos=vector(-15.0,10.0,0.0)
ball.v=vector(2.0,00,0)

a1=arrow(shaftwidth=0.2)
a1.color=color.green
a1.pos=vector(-15.0,10.0,0)


dt=0.001

while ball.pos.x<15.0:
    rate(1000)
    ball.pos+=ball.v*dt
    ball.v.y+=-g*dt

    a1.pos+=ball.v*dt
    a1.axis=vector(ball.v.x/2,ball.v.y/2,0)

    if ball.y<=size and ball.v.y<0:
        ball.v.y=-ball.v.y

print"end"

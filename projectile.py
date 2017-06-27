from visual import*
g=9.8
size=1
height=15

scene=display(width=800,height=800,center=(0,height/2,0),background=(0.5,0.5,0))
floor=box(length=30,height=0,width=10,color=color.blue)
ball=sphere(radius=size,color=color.red)

ball.pos=vector(-15,size,0)
ball.v=vector(10,10,0)

a1=arrow(shaftwidth=0.5)
a1.color=color.green
a1.pos=vector(-15,size,0)


dt=0.001
t=0
while ball.pos.y>=size:
    rate(500)
    ball.pos+=ball.v*dt
    ball.v.y+=-g*dt

    a1.pos+=ball.v*dt
    a1.axis=vector(ball.v.x/2,ball.v.y/2,0)
    
  
    t+=0.001
print(t)
print"end"

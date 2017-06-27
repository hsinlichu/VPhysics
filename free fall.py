from visual import*
g=9.8
size=0.25
height=15

scene=display(width=800,height=800,center=(0,height/2,0),background=(0.5,0.5,0))
floor=box(length=30,heigh=0.01,width=10,color=color.blue)
ball=sphere(radius=size,color=color.red)

ball.pos=vector(0,height,0)
ball.v=vector(0,0,0)

dt=0.001
while ball.pos.y>=size:
    rate(1000)
    ball.pos+=ball.v*dt
    ball.v.y+=-g*dt

print"end"

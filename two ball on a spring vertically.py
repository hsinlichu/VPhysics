from visual import*
size,m=0.05,0.2
r,k,g=0.5,15,9.8

scene=display(title='two ball on a spring',width=800,height=800,cnter=vector(0,-0.2,0),background=(0.5,0.5,0))
ceiling=box(length=0.8,height=0.005,width=0.8,colcr=color.blue)
ball=sphere(radius=size,color=color.red)
spring=helix(radius=0.02,thickness=0.01)

ball.pos=vector(0,-r,0)
ball.v=vector(0,0,0)

dt=0.001

while true:
    rate(1000)
    spring.axis=ball.pos-spring.pos
    spring_force=-k*(abs(ball.pos)-r)*norm(spring.axis)
    ball_a=vector(0,-g,0)+spring_force/m
    ball.v+=ball_a*dt
    ball.pos+=ball.v*dt

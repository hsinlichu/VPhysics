from visual import*
size=[0.15,0.10]
mass=[0.1,0.1]
colors=[color.yellow,color.green]
p=[vector(1,0.2,0),vector(0,0,0)]
v=[vector(-0.5,0,0),vector(0,0,0)]

def af_col_v(v1,v2,x1,x2):
    v1_prime=v[0]+dot(v[1]-v[0],p[0]-p[1])/abs(p[1]-p[0])**2*(p[0]-p[1])
    v2_prime=v[1]+dot(v[0]-v[1],p[1]-p[0])/abs(p[0]-p[1])**2*(p[1]-p[0])
    return (v1_prime,v2_prime)

scene=display(width=800,length=800,x=600,y=100,background=(0.3,0.3,0))
ball_reference=sphere(pos=(0,0,0),radius=0.02,color=color.red)
balls=[]
for i in [0,1]:
    balls.append(sphere(pos=p[i],radius=size[i],color=colors[i]))
    balls[i].v=v[i]

dt=0.001
while true:
    rate(1000)
    for ball in balls:
        ball.pos+=ball.v*dt
    if abs(balls[0].pos-balls[1].pos)<=(size[0]+size[1]) and dot(balls[0].pos-balls[1].pos,balls[0].v-balls[1].v)<=0:
        (balls[0].v,balls[1].v)=af_col_v(balls[0].v,balls[1].v,balls[0].pos,balls[1].pos)
        
    

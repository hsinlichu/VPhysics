from visual import*
r=0.3
k=25.0
size=[0.05,0.04,0.03]
m=[0.3,0.4,0.3]
colors=[color.yellow,color.green,color.blue]
p=[vector(0,0,0),vector(0,-r,0),vector(0.25,-0.45,0)]
v=[vector(0,0,0),vector(0,0,0),vector(-0.2,0.42,0)]
balls=[]

scene=display(title="collision and internal energy",width=800,height=800,x=600,y=100,background=(0.3,0.3,0))

for i in [0,1,2]:
    balls.append(sphere(radius=size[i],color=colors[i],pos=p[i]))
    balls[i].v=v[i]

spring=helix(radius=0.02,thickness=0.01)
spring.pos=balls[0].pos
spring.axis=balls[1].pos-balls[0].pos

def collision(v1,p1,v2,p2):
    a=v1-v2
    v1_af=((m[0]*p0+m[2]*p2)/(m[0]+m[2]))*a+v2
    v2_af=(2*m[0]/(m[0]+m[2]))*a+v2
    return (v1_af,v2_af)

def spring_force():
    f0 =-k*(r-abs(spring.axis))*norm(spring.axis)                
    f1 = -f0
    return (f0,f1)
dt=0.001
while true:
    rate(1000)
    balls[2].pos+=v[2]*dt

    if abs(balls[0].pos-balls[2].pos)<=(size[0]+size[2]) and dot(balls[2].pos-balls[0].pos,balls[2].v)<=0:
        (balls[2].v,balls[0].v)=collision(balls[2].v,balls[2].pos,balls[0].v,balls[0].v)

    (f0,f1)=spring_force()               
    
    a0=f0/m[0]
    balls[0].v+=a0*dt
    balls[0].pos+=balls[0].v*dt
    a1=f1/m[1]
    balls[1].v+=a1*dt
    balls[1].pos+=balls[1].v*dt

    spring.pos=balls[0].pos
    spring.axis=balls[1].pos-balls[0].pos


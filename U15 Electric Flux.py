from visual import*
epsilon0=8.8542E-12
k=1.0/(4*pi*epsilon0)
lamda0,RodR,RodL=1E-6,0.02,1.0
R,L=0.5,1.4
ball_m,ball_q=1E-6,1E-12

def E(r):
    field=vector(0,0,0)
    for i in arange(-RodL/2,RodL/2,0.002):
        distence=r-vector(i,0,0)        
        field+=k*(lamda0*(cos(pi*i/RodL)**2)*0.002)/abs(distence)**2*norm(distence)
    return field
Q=0
for i in arange(-RodL/2,RodL/2,0.002):    
    Q+=(lamda0*(cos(pi*i/RodL)**2))*0.002
print Q


scene=display(title="charged rod",x=0,y=0,width=600,height=600,background=(0.5,0.5,0))
Rod=cylinder(pos=(-RodL/2.0,0,0),axis=(RodL,0,0),radius=RodR,color=color.yellow,opacity=0.40)
tube=cylinder(pos=(-L/2,0,0),axis=(L,0,0),radius=R,color=color.blue,opacity=0.40)

trajectory=[sphere(pos=(0,0,0),radius=0.001,color=(1,1,0),make_trail=True,v=vector(0,0,0),a=vector(0,0,0)) for i in range(20)]


for i,x in zip(arange(-RodL/2,RodL/2,RodL/10),range(10)):
    trajectory[x].pos.x=i
    trajectory[x].pos.y=RodR
    trajectory[10+x].pos.x=i
    trajectory[10+x].pos.y=-RodR

flux1=0
for i in arange(-RodL/2,RodL/2,0.002):
    flux1+=E(vector(i,R,0)).y*1*2*pi*R*0.002
print flux1

flux2=0    
for i in arange(0,R,0.002):
    flux2+=2*E(vector(-L/2,i,0)).x*(-1)*2*pi*i*0.002
print flux2

#print trajectory[i].pos
print "flux=",flux1+flux2,"Q/epsilon0",Q/epsilon0
dt=0.001
while True:
    rate(1000)
    for i in trajectory:
        i.a=E(i.pos)*ball_q/ball_m
        i.pos+=i.a*dt
        if abs(i.pos)>=1.5:
            i.v=0




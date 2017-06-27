from visual import*
prob=0.0008
N,L=600,10E-9/2.0
E=vector(1500000,0,0)
q,m,size=1.6E-19,1E-6/6E23,1E-10
t,dt,vrms=0,1E-16,100000.0
atoms,atoms_v,atom_a=[],[],[]
counter=0

scenev=display(width=600,height=600,x=600,fov=0.01,range=(1.5*vrms,1.5*vrms,1.5*vrms),background=(0.2,0.2,0))
scene=display(width=600,height=600,background =(0.2,0.2,0))
container=box(display=scene,length=2*L,height=2*L,width=2*L,opacity=0.2,color=color.yellow)

pos_array=-L+2*L*random.rand(N,3)
theta=pi*random.rand(N,1).flatten()
phi=2*pi*random.rand(N,1).flatten()
v_array=transpose(vrms*array([sin(theta)*cos(phi),sin(theta)*sin(phi),cos(theta)]))##transpose
for i in range(N):
    atoms.append(sphere(display=scene,pos=pos_array[i],make_trail=False,radius=size,color=random.rand(3,1)))
    atoms_v.append(sphere(display=scenev,pos=v_array[i],radius=vrms/50,color =random.rand(3,1)))

vd_ball=sphere(display=scenev,pos=(0,0,0),radius=vrms/30,color=color.red)
x_axis=curve(display=scenev,pos=[(-1.4*vrms,0,0),(1.4*vrms,0,0)],radius=vrms/100)
y_axis=curve(display=scenev,pos=[(0,-1.4*vrms,0),(0,1.4*vrms,0)],radius=vrms/100)
atoms[87].make_trail=True
vv=vector(0,0,0)
a=q*E/m
while True:
    t+=dt
    rate(1000)
    v_array+=a*dt
    pos_array+=v_array*dt
    outside=abs(pos_array)>=L
    if outside[N-1,0] or outside[N-1,1] or outside[N-1,2]:atoms[N-1].retain=0
    pos_array[outside]=-pos_array[outside]
    vv+=vector(sum(v_array,0)/N)
    
    for i in range(N):
        test=random.rand(1,1).flatten()
        if test<=0.0008:
            counter+=1
            aa=pi*random.rand(1,1).flatten()
            bb=2*pi*random.rand(1,1).flatten()
            v_array[i]=transpose(vrms*array([sin(aa)*cos(bb),sin(aa)*sin(bb),cos(aa)]))
        atoms_v[i].pos,atoms[i].pos=v_array[i],pos_array[i]
    if int(t/dt)%2000==0:
        tau=t*N/counter
        
        print tau,vv/(t/dt),q*E*tau/m
        vd_ball.pos=vv/(t/dt)
        t,counter,vv=0,0,vector(0,0,0)
        
    
    atoms[N-1].retain=2000

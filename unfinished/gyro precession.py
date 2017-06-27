from visual import*
g=9.8
M,R,w=0.5,0.10,0.05
i=0.5*M*R**2
l,r=0.12,0.005
theta=70*pi/180.0
omega=10*2*pi*vector(cos(theta),sin(theta),0)
ir=0.045
L=i*omega

scene=display(width=1000,height=1000,range=0.6,background=(0.5,0.5,0))

spintop=frame()
shaft=cylinder(frame=spintop,pos=(0,0,0),axis=(1,0,0),radius=r,length=l,material=materials.wood)
disk=cylinder(frame=spintop,pos=(ir-w/2,0,0),axis=(w,0,0),radius=R,material=materials.wood)

ball=sphere(radius=0.005,make_trail=true,color=color.red,trail_type="points",interval=1000,retain=20)
ball.pos=ir*vector(cos(theta),sin(theta),0)

spintop.pos=(0,0,0)
base=cone(pos=(0,-0.2,0),axis=(0,0.2,0),color=color.blue,radius=0.1)

dt=0.0002
lastball_posz=0
counter=0
T=0

while True:
    rate(5000)
    
    
    torque=cross(ir*norm(spintop.axis),vector(0,-M*g,0))
    L+=torque*dt
    spintop.axis=L
    delta_angle=mag(omega)*dt
    spintop.rotate(angle=delta_angle,axis=spintop.axis)

    ball.pos=norm(spintop.axis)*l

    T+=dt
    if dot(ball.pos.z,lastball_posz)<0:
        counter+=1
        if counter==2:
            print T
            counter=0
            T=0

    lastball_posz=ball.pos.z
    

    
        
    
    

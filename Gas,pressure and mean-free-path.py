from visual import*
from random import random
from visual.graph import*

N=50
L=((24.4E-3/(6E23))*N)**(1/3.0)/2
m,size=4E-3/6E23,310E-12
L_size=L-size
k,T=1.38E-23,298.0
t,dt=0,0.5E-13
vrms=(3*k*T/m)**0.5
atoms=[]

print 'Theoretical MVP:',(2*L)**3/((2**0.5)*pi*((2*size)**2)*N)

deltav=100
vdist=gdisplay(x=800,y=0,ymax=N*deltav/1000.,width=500,height=300,xtitle='v',ytitle='dN')
theory=gcurve(color=color.cyan)
dv=10
for v in arange(0.,3001.+dv,dv):
    theory.plot(pos=(v,(deltav/dv)*N*4.*pi*((m/(2.*pi*k*T))**1.5)*exp((-0.5*m*v**2)/(k*T))*v**2*dv))
observation=ghistogram(bins=arange(0.,3000.,deltav),accumulate=1,average=1,color=color.red)

scene=display(width=800,height=800,background=(0.2,0.2,0))
container=box(length=2*L,height=2*L,width=2*L,opacity=0.2,color=color.yellow)
for i in range(N):
    position=vector(-L_size+2*L_size*random(),-L_size+2*L_size*random(),-L_size+2*L_size*random())
    if i==N-1:
        atom=sphere(pos=position,radius=size,color=color.yellow,make_trail=True,retain=600)
    else:
        atom=sphere(pos=position,radius=size,color=(random(),random(),random()))
    ra,rb=pi*random(),2*pi*random()
    atom.m,atom.v=m,vector(vrms*sin(ra)*cos(rb),vrms*sin(ra)*sin(rb),vrms*cos(ra))
    atoms.append(atom)

def vcollision(a1,a2):
    v1prime=a1.v-2*a2.m/(a1.m+a2.m)*(a1.pos-a2.pos)*dot(a1.v-a2.v,a1.pos-a2.pos)/abs(a1.pos-a2.pos)**2
    v2prime=a2.v-2*a1.m/(a1.m+a2.m)*(a2.pos-a1.pos)*dot(a2.v-a1.v,a2.pos-a1.pos)/abs(a2.pos-a1.pos)**2
    return v1prime,v2prime
free_path=0
collision_time=0
p_total=0
while True:
    t+=dt
    rate(100000)
    
    
    v=[]
    for i in range(N):
        atoms[i].pos+=atoms[i].v*dt
        v.append(mag(atoms[i].v))
    for i in range(N):    
        for j in range(i+1,N):
            if abs(atoms[i].pos-atoms[j].pos)<=2*size and dot(atoms[i].pos-atoms[j].pos,atoms[i].v-atoms[j].v)<=0:
                atoms[i].v,atoms[j].v=vcollision(atoms[i],atoms[j])
                collision_time+=2
        if abs(atoms[i].pos.x) >=L_size and atoms[i].pos.x*atoms[i].v.x>0:
            atoms[i].v.x=-atoms[i].v.x
            p_total+=2*m*abs(atoms[i].v.x)
        if abs(atoms[i].pos.y) >=L_size and atoms[i].pos.y*atoms[i].v.y>0:
            atoms[i].v.y=-atoms[i].v.y
            p_total+=2*m*abs(atoms[i].v.y)
        if abs(atoms[i].pos.z) >=L_size and atoms[i].pos.z*atoms[i].v.z>0:
            atoms[i].v.z=-atoms[i].v.z
            p_total+=2*m*abs(atoms[i].v.z)
        free_path+=abs(atoms[i].v)*dt
    if t>=1000*dt:
        print 'average pressure:',p_total/(1000*dt*24*L**2)
        p_total=0
        t=0
        print 'mean free path:',free_path/collision_time
        free_path=0
        collision_time=0
            
                
    observation.plot(data=v)

    

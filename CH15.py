from visual import*
print "James Chu"
N=101
dx,dy=1E-2/(N-1),1E-2/(N-1)
dx2,dy2=dx*dx,dy*dy
L,d=5E-3,2E-3

def solve_laplacian(u,u_cond,dx,dy,Niter=800):
    V=array(u)
    for i in range(Niter):
        V[u_cond]=u[u_cond]
        V[1:-1,1:-1]=((V[1:-1,2:]+V[1:-1,:-2])*dx2+(V[2:,1:-1]+V[:-2,1:-1])*dy2)/(2*(dx**2+dy**2))
    return V

def get_field(V,dx,dy):
    Ex,Ey=gradient(V)
    Ex,Ey=-Ex/dx,-Ey/dy
    return Ex,Ey

u=zeros([N,N])
u[N/2-int(L/dx/2.0):N/2+int(L/dx/2.0),N/2-int(d/dy/2.0)]=-100.0
u[N/2-int(L/dx/2.0):N/2+int(L/dx/2.0),N/2+int(d/dy/2.0)]=100.0
u_cond=not_equal(u,0)

V=solve_laplacian(u,u_cond,dx,dy)

scene=display(title="dipole",height=1000,width=1000,center=(N*dx/2,N*dy/2,0))
box(pos=(N*dx/2,N*dy/2-d/2-dy,0),length=L,height=dy/5,width=2*dx) #down
box(pos=(N*dx/2,N*dy/2+d/2-dy,0),length=L,height=dy/5,width=2*dx) #up

for i in range(N):
    for j in range(N):
        point=box(pos=(i*dx,j*dy,0),length=dx,height=dy,width=dx,color=((V[i,j]+100)/200,(100-V[i,j])/200,0.0))

Ex,Ey=get_field(V,dx,dy)
for i in range(1,N-1,2):
    for j in range(1,N-1,2):
        ar=arrow(pos=(i*dx,j*dy,2*dx),axis=(Ex[i,j]/6E8,Ey[i,j]/6E8,0),shaftwidth=dx/4.0,color=color.black)

box(pos=(50*dx,60*dy,0),length=dx*70,height=dy*6,width=4*dx,color=color.blue,opacity=0.38)

flux_up,flux_down,flux_right,flux_left=0,0,0,0

for a in range(15,85,1):         #dA multuple later
    flux_up+=Ey[a,63]*1

for b in range(15,85,1):
    flux_down+=Ey[b,57]*(-1)

for c in range(57,63,1):
    flux_left+=Ex[15,c]*(-1)

for e in range(57,63,1):
    flux_right+=Ex[85,e]*1


flux=(flux_up+flux_down)*70*dx+(flux_right+flux_left)*6*dy
print "flux",flux
Q=8.8542E-12*flux
c=Q/200

print "Capacitpr:",c
print "Ideal:",(8.8542E-12)*1*L/d
print L,d

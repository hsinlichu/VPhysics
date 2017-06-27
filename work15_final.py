from visual import*
N=101
dx,dy=1E-2/(N-1),1E-2/(N-1)
dx2,dy2=dx*dx,dy*dy
L,d=5E-3,2E-3

def solve_laplacian(u,u_cond,dx,dy,Niter=800):
    V=array(u)
    for i in range(Niter):
        V[u_cond]=u[u_cond]
        V[1:-1,1:-1]=((V[2:,1:-1]+V[:-2,1:-1])*dy2+(V[1:-1,2:]+V[1:-1,:-2])*dx2)/(2*(dx2+dy2))
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

scene=display(title='dipole',height=1000,width=1000,center=(N*dx/2,N*dy/2,0))
box(pos=(N*dx/2,N*dy/2-d/2-dy,0),length=L,height=dy/5,width=2*dx)
box(pos=(N*dx/2,N*dy/2+d/2-dy,0),length=L,height=dy/5,width=2*dx)

for i in range(N):
    for j in range(N):
        point=box(pos=(i*dx,j*dy,0),length=dx,height=dy,width=dx,color=((V[i,j]+100)/200,(100-V[i,j])/200,0.0))

Ex,Ey=get_field(V,dx,dy)

for i in range(1,N-1,2):
    for j in range(1,N-1,2):
        ar=arrow(pos=(i*dx,j*dy,2*dx),axis=(Ex[i,j]/6E8,Ey[i,j]/6E8,0),shaftwidth=dx/4.0,color=color.black)

box(pos=(50*dx,60*dy,0),length=dx*70,height=dy*6,width=4*dx,color=color.blue,opacity=0.38)
flux_xup,flux_xdown,flux_yleft,flux_yright=0,0,0,0

for a in arange(15,85,1):
    flux_xup+=Ey[a,63]*1
for b in arange(15,85,1):
    flux_xdown+=Ey[b,57]*(-1)
for c in arange(57,63,1):
    flux_yleft+=Ex[15,c]*(-1)
for dd in arange(57,63,1):
    flux_yright+=Ex[85,dd]*1
flux=(flux_xup+flux_xdown)*dx*70+(flux_yleft+flux_yright)*dy*6
Q=8.8542E-12*flux
C=Q/200
print C
print"ideal",(8.8542E-12)*1*L/d
print L,d


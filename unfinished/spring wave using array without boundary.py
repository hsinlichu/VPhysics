from visual import*
A,N,omega=0.10,50,2*pi/1.0
size,m,k,d=0.06,0.1,10.0,0.4
scene=display(title="spring wave",width=1200,height=300,background=(0.5,0.5,0), range= N*d/2+0.5,center=((N-1)*d/2,0,0))
#balls=[sphere(radius=size,color=color.red,pos=vector(i*d,0,0),v=vector(0,0,0)) for i in range(N)]
#springs=[helix(radius=size/2.0,thickness=d/15.0,pos=vector(i*d,0,0),axis=vector((i+1)*d-i*d,0,0)) for i in range(N-1)]
c=curve(display=scene)

unit_K,n=2*pi/(N*d),10
wavevector=n*unit_K
phase=wavevector*arange(N)*d
ball_pos,ball_orig,ball_v,spring_len=arange(N)*d+A*sin(phase),arange(N)*d,zeros(N),ones(N)*d
t,dt=0,0.001

while True:
    rate(1000)
    t+=dt
    
    spring_len[:-1]=ball_pos[1:]-ball_pos[:-1]
    spring_len[-1]=ball_pos[0]+N*d-ball_pos[-1]
    ball_v[1:]+=k*(spring_len[1:]-spring_len[:-1])/m*dt
    
    ball_pos+=ball_v*dt
    ball_v[0]=0

#    for i in range(N):
#        balls[i].pos.x=ball_pos[i]
#        if i !=N-1:
#            springs[i].pos=ball_pos[i]
#            springs[i].axis=balls[i+1].pos-balls[i].pos

    ball_disp=ball_pos-ball_orig
    c.x=ball_orig
    c.y=ball_disp*4.0+1.0


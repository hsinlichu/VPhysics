from visual import*
k=8.99*10**9
L,size=1.0,0.1
polecharge,poleposition,polecolor=[1E-5,-1E-5],[vector(L,0,0),vector(-L,0,0)],[(1,0,0),(0,0,1)]
ball_m,ball_q=1E-6,1E-12




scene=display(title="dipole",height=500,width=500,range=3.5,auto_scale=False,background=(0.5,0.5,0))
pole_set=[sphere(pos=p,radius=size,color=cc,q=charge) for (charge,p,cc) in zip(polecharge,poleposition,polecolor)]


originPos=vector(0.25,0,0)
position=[]
for a in [vector(0,1,0),vector(0,0,1)]:
    for i in range(12):
        originPos=rotate(originPos,pi/6,a)
        position.append(originPos+(1,0,0))
        print rotate(originPos,pi/6,a)#,pi/6*i,a

        print "----------------------------"
        


trajectory=[sphere(pos=pp,radius=0.001,color=(1,1,0),q=ball_q,make_trail=True,v=vector(0,0,0),a=vector(0,0,0)) for pp in position]
print len(trajectory),trajectory[0].pos,trajectory[1].pos

ball=[]

label(text="Left click to place balls.",pos=(0,0.5,0),opacity=0.2)



def Force_E(r):
    
    dis_positive=r-pole_set[0].pos
    dis_negative=r-pole_set[1].pos
    if dis_positive<0.1 or dis_negative<0.1:
        return 0
    Force_positive=k*pole_set[0].q*(1E-12)/abs(dis_positive)**2*norm(dis_positive)
    Force_negative=k*pole_set[1].q*(1E-12)/abs(dis_negative)**2*norm(dis_negative)
    Force_total=Force_positive+Force_negative    
    return Force_total

def makeSphere(evt):
    loc=evt.pos
    print "click at",loc
    ball.append(sphere(pos=loc,radius=0.05,color=(1,0,1),make_trail=True,v=vector(0,0,0),a=vector(0,0,0),q=ball_q))
    print "electric force:",Force_E(loc)
    return 0

scene.bind("mousedown",makeSphere,scene)       
x=0
dt=0.001
while True:
    rate(30000)
    
    for i in ball:
        
        i.a=Force_E(i.pos)/ball_m
        i.v+=i.a*dt
        i.pos+=i.v*dt
        if abs(i.pos-pole_set[0].pos) <0.1:
            i.pos=pole_set[0].pos
        if abs(i.pos-pole_set[1].pos) <0.1:
            i.pos=pole_set[1].pos

    for line in trajectory:
        
        line.a=Force_E(line.pos)/ball_m
        line.pos+=line.a*dt
        if  abs(line.pos-pole_set[1].pos) <0.1:
            line.pos=pole_set[1].pos
        

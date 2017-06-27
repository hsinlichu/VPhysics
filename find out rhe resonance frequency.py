from visual import*
from visual.graph import*
size,m=0.02,0.2
L,k=0.2,20.0
omega=[0.1*i+0.7*sqrt(k/m) for i in range(1,int(0.5*sqrt(k/m)/0.1))]

'''
scene1=gdisplay(y=400,width=800,height=300,xtitle='t',ytitle='x',background=(0.5,0.5,0.5))#new
scene2=gdisplay(x=700,y=400,width=800,height=300,xtitle='t',ytitle='averge_power',background=(0.4,0.4,0.5))#new
x=gcurve(color=color.red,gdisplay=scene1)#new
p=gdots(color=color.cyan,gdisplay=scene2)#new
scene=display(x=700,width=800,heigh=400,fov=0.03,range=0.5,center=(0.3,0,0),background=(0.4,0.4,0))

wall_left=box(length=0.005,height=0.3,width=0.3,color=color.blue)
ball=sphere(radius=size,color=color.red)
spring=helix(radius=0.015,thickness=0.01)
'''
scene3=gdisplay(y=400,width=800,height=300,xtitle='omega',ytitle='averge power comsumption',background=(0.5,0.5,0.5))
p=gcurve(color=color.red,gdisplay=scene3)

class obj:
    pass
wall_left,ball,spring=obj(),obj(),obj()
wall_left.pos=vector(0,0,0)
ball.pos,ball.v,ball.m=vector(L,0,0),vector(0,0,0),m
spring.pos=wall_left.pos

def drag_force(m,v):
    return -0.05*m*(k/m)**0.5*v
def sinusoidal_force(m,t):
    return 0.1*sin(omega_d*t)*norm(spring.axis)


    

t,dt=0,0.001

power=0
times=1

averge_powerset=[]



for omega_d in omega:
    print "omega:",omega_d
    T,Tcount=2*pi/omega_d,0
    print "T:",T
    while true:
        rate(1000000)
        spring.axis=ball.pos-spring.pos
        spring_force=-k*(mag(spring.axis)-L)*norm(spring.axis)
        ball.a=(spring_force+drag_force(ball.m,ball.v)+sinusoidal_force(ball.m,t))/ball.m
        ball.v+=ball.a*dt
        ball.pos+=ball.v*dt
        t+=dt
        Tcount+=dt
        power+=dot(sinusoidal_force(ball.m,t),ball.v)
    
        if Tcount>=T:
            averge_power=power/T
            print "averge_power of the",times,"period",averge_power
            averge_powerset.append(averge_power)
            
            Tcount=0
            power=0
            
            if times>=4 and (averge_powerset[times-1-1]-averge_powerset[times-2-1])<(averge_powerset[times-1]-averge_powerset[times-1-1]):
                print "reach the steady-state:",averge_powerset[times-1]
                p.plot(pos=(omega_d,averge_powerset[times-1]))
                
                averge_powerset=[]
                times=1
                break
            times+=1


#            p.plot(pos=(t,averge_power))#new
#        x.plot(pos=(t,ball.pos.x-L))#new
    
    

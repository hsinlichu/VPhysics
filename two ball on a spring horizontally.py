#coding=utf-8

from visual import*
r,k=0.5,15
size=[0.05,0.04]
m=[0.2,0.5]

scene=display(title='two ball on a spring horizontally',width=800,height=800,center=vector(0,0,0),background=(1,0.5,0))

ball_left=sphere(radius=size[0],color=color.red)
ball_right=sphere(radius=size[1],color=color.blue)
ball_left.v=vector(0,0,0)
ball_right.v=vector(0,0,0)

ball=[ball_left,ball_right]

ball[1].pos=vector(0,0,0)
ball[0].pos=vector(-r-0.2,0,0)

a1=arrow(shaftwidth=0.002)                  #左箭頭
a1.color=color.green

a2=arrow(shaftwidth=0.002)                  #右箭頭
a2.color=color.green









spring=helix(radius=0.02,thickness=0.01)

#r_l=m[1]*(abs((ball[1].pos-ball[0].pos)))/(m[0]+m[1])  #左球彈簧半徑
#r_r=m[0]*(abs((ball[1].pos-ball[0].pos)))/(m[0]+m[1])  #右球彈簧半徑

#print 'r_l:',r_l,'r_r:',r_r

#T=(2*pi*r_l)/abs(ball[0].v)
#print '週期:',T
dt=0.001
t=0
while true:
    rate(1000)
    spring.axis=ball[0].pos-ball[1].pos                      #彈簧
    spring.pos=ball[1].pos
    #print (-norm(spring.axis))  

    com=(m[1]*ball[1].pos+m[0]*ball[0].pos)/(m[0]+m[1])
    #print 'r:',com
    
    spring_force=-k*(abs(spring.axis)-r)*(norm(spring.axis))#left ball
    
    #print '壓縮伸長量:',abs(ball[0].pos-r)-r_l
    a_l=spring_force/m[0]
    #print 'force:',spring_force,'left a:',a_l
    ball[0].v+=a_l*dt
    ball[0].pos+=ball[0].v*dt
    #print 'left pos:',ball[0].pos,'v:',ball[0].v

    a_r=-spring_force/m[1]                                       #right ball
    ball[1].v+=a_r*dt
    #print 'right v:',ball[1].v,'right a:',a_r
    #print '-------------------------------------'
    ball[1].pos+=ball[1].v*dt

    a1.pos=ball[0].pos
    a1.axis=ball[0].v/5

    a2.pos=ball[1].pos
    a2.axis=ball[1].v/5

    t+=1

    #print "t=",t,",質心位於:",r




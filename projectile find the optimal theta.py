from visual import*
import ruler

g=9.8
size=0.5


scene=display(title='bouncing projectile',width=1200,height=800,center=(0,5,0),background=(0.5,0.5,0))
floor=box(length=30,height=0.0,width=4,color=color.blue)
ball=sphere(radius=size,color=color.red,make_trail=false)

ruler1=ruler.ruler(axis=vector(1,0,0),pos=vector(-15,0,1),unit=2.0,length=30.0,thickness=0.2)
ruler2=ruler.ruler(vector(-15,0,1),vector(0,1,0),unit=1.0,length=10.0,thickness=0.2)

ball.pos=vector(-15.0,0.0,0.0)
v_initial=30
theta= 10*pi/180

ball.v=v_initial*vector(cos(theta),sin(theta),0)

a1=arrow(shaftwidth=0.2)
a1.color=color.green
a1.pos=ball.pos

c=0.4
power=1.5
max_distance=0

dt=0.001



while ball.pos.y>=0:
    rate(5000)

    ball.pos+=ball.v*dt    
    ball.v.y+=-g*dt
    
    drag_a=c*(mag(ball.v)**power)*norm(ball.v)

    ball.v-=drag_a*dt
    
    a1.pos=ball.pos
    a1.axis=vector(ball.v.x/2,ball.v.y/2,0)
    
    
    if ball.pos.y<0 and ball.v.y<0:
        print ball.pos.x+15,theta*180/pi

        if ball.pos.x+15>max_distance:
            max_distance=ball.pos.x+15
            print 'max:',max_distance,theta*180/pi
        else:
            print'the max distance:',max_distance,theta*180/pi
            break
    
        ball.pos=vector(-15.0,0.0,0.0)
        theta+=0.01
        ball.v=v_initial*vector(cos(theta),sin(theta),0)

ball2=sphere(radius=size,color=color.blue,make_trail=true)
ball2.pos=vector(-15.0,0.0,0.0)
v_initial=30
print theta

ball2.v=v_initial*vector(cos(theta),sin(theta),0)

a1=arrow(shaftwidth=0.2)
a1.color=color.red
a1.pos=ball2.pos


time=0
t=1
dt=0.001

while true :
    rate(1000)
    ball2.pos+=ball2.v*dt    
    ball2.v.y-=g*dt

    drag_a=c*(mag(ball2.v)**power)*norm(ball2.v)
        

    ball2.v-=drag_a*dt
    
    a1.pos=ball2.pos
    a1.axis=vector(ball2.v.x/2,ball2.v.y/2,0)
        
    #print ball2.pos.y,ball2.v.y

    if ball2.pos.y<=0 and ball2.v.y<0:
        ball2.v.y=-ball2.v.y
        time+=1
        print time
        

    if time==3:
        print 'you already jump ',time,'times.''and the distance is:',ball2.pos.x
        break




print"end"


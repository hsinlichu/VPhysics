from visual import*
#constant
Earthbelt=((4.0/3.0)*pi*6357*6378*6378-(4.0/3.0)*pi*6357*6357*6357)*3.8*10**12
#I_Earth=(0.4*(4.0/3.0)*pi*6357*6357*6357*3.8*10**12*6357000**2+0.4*(4.0/3.0)*pi*6322*6322*6322*10.7*10**12*6322000**2)
I_Earth=(0.4*(4.0/3.0)*pi*6357*6357*6357*3.0*10**12*6357000**2+0.4*(4.0/3.0)*pi*6322*6322*6322*3.8*10**12*6322000**2)
G=6.637E-11
Earth_mass=5.972E24
Sun_mass=1.989E30
Moon_mass=7.3477E22
Moon_velocity=vector(0,0,(-2*pi*384400000)/(29.53*24*60*60))
Moon_pos=vector(384400000*cos(23.5*pi/180),384400000*sin(23.5*pi/180),0)
Earth_pos=vector(0,0,0)
Sun_velocity=vector(0,0,(-2*pi*1.495e11)/(365.2*24*60*60))
Sun_pos=vector(1.495e11*cos(23.5*pi/180),1.495e11*sin(23.5*pi/180),0)
scene=display(width=1000,height=1000,background=(0.5,0.5,0))
#arrow&earth&print I
A=arrow(pos=vector(0,0,0),axis=vector(cos(66.5/180*pi),sin(66.5/180*pi),0)*I_Earth*2*pi/(60*60*24),color=color.yellow)
earth=sphere(pos=(0,0,0),radius=mag(A.axis)*0.25,color=color.white,materials=materials.earth)
cut=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
#testmoon
t0=0
dt0=3600
Tau_moon=vector(0,0,0)
Moon_deltau=vector(0,0,0)
while t0<=24*3600*29.53:
    rate(24*365*1000)
    t0+=dt0
    F_moon=(-G*Earth_mass*Moon_mass/mag2(Moon_pos-Earth_pos))*norm(Moon_pos-Earth_pos)
    Moon_pos+=Moon_velocity*dt0
    Moon_velocity+=(F_moon/Moon_mass)*dt0
    for number in cut:
        m=Earthbelt/16
        m_pos=vector(6357000*sin(2*pi*number/16),0,6357000*cos(2*pi*number/16))
        Moon_tau=cross(m_pos-Earth_pos,(G*m*Moon_mass/mag2(Moon_pos-m_pos))*norm(Moon_pos-m_pos))
        Moon_deltau+=Moon_tau
        Tau_moon+=Moon_deltau
Moon_finaltau=vector(Tau_moon.x,0,Tau_moon.z)
#testsun
t1=0
dt1=3600*24
Tau_sun=vector(0,0,0)
Sun_deltau=vector(0,0,0)
while t1<=24*3600*365.2:
    rate(365*1000)
    t1+=dt1
    F_sun=(-G*Earth_mass*Sun_mass/mag2(Sun_pos-Earth_pos))*norm(Sun_pos-Earth_pos)
    Sun_pos+=Sun_velocity*dt1
    Sun_velocity+=(F_sun/Sun_mass)*dt1
    for number in cut:
        m=Earthbelt/16
        m_pos=vector(6357000*sin(2*pi*number/16),0,6357000*cos(2*pi*number/16))
        Sun_tau=cross(m_pos-Earth_pos,(G*m*Sun_mass/mag2(Sun_pos-m_pos))*norm(Sun_pos-m_pos))
        Sun_deltau+=Sun_tau
        Tau_sun+=Sun_deltau
Sun_finaltau=vector(Tau_sun.x,0,Tau_sun.z)
Total_tau=mag(Tau_moon*12)+mag(Tau_sun)
print "I                 ",mag(A.axis)
print "L of earth        ",mag(A.axis)*(2*pi/86400)
print "delta L by moon   ",Tau_moon*12
print "delta L by sun    ",Tau_sun
print "total tau         ",Total_tau
#really run
T=0
dT=1
counter=0
while true:
    rate(100000)
    Apast=A.axis.z
    pointer=cross(vector(0,1,0),norm(A.axis))
    T=T+dT
    A.axis+=Total_tau*pointer*dT
    if A.axis.z*Apast<0:
        counter+=1
        if counter==2:
            print "T",T
            T=0
            counter=0
        


    
    

  
















        

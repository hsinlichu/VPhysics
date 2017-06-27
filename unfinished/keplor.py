from visual import*
G,g,AU=6.67E-11,9.8,1.49597871E11
mass={"sun":1.989E30,"mars":6.41693E23,"earth":5.97219E24,"halley":2.2E14}
d_perihelion={"halley":8.78139501E10 ,"mars":2.067E11,"earth":1.47098090E11}
v_perihelion={"halley":5.457E4,"mars":2.65E4,"earth":3.027E4}
color_set={"earth":color.yellow,"mars":color.blue,"halley":color.green}
material_set={"earth":materials.earth,"mars":materials.marble,"halley":materials.emissive}

def g_force(m,pos):
    return ((-G*m*mass["sun"])/mag2(pos))*norm(pos)
class as_obj(sphere):
    def kenitic_energy(self):
        return (0.5)*self.m*abs(self.v)**2
    def potential_energy(self):
        return (-G*self.m*mass["sun"])/abs(self.v)

scene=display(height=800,width=800,center=(0,0,0),background=(0.5,0.5,0))
scene.forward=vector(0,-1,0)

sun=sphere(m=mass["sun"],radius=6.955E8,pos=vector(0,0,0),color=color.red)
halley=as_obj(radius=1.5E4,m=mass["halley"],color=color_set["halley"],make_trail= True,material=material_set["halley"])
halley.v=vector(0,0,-v_perihelion["halley"])
halley.pos=vector(d_perihelion["halley"],0,0)
mars=as_obj(radius=3.396E6,m=mass["mars"],color=color_set["mars"],make_trail= True,material=material_set["mars"])
mars.v=vector(0,0,-v_perihelion["mars"])
mars.pos=vector(d_perihelion["mars"],0,0)
earth=as_obj(radius=6.371E6,m=mass["earth"],color=color_set["earth"],make_trail= True,material=material_set["earth"])
earth.v=vector(0,0,-v_perihelion["earth"])
earth.pos=vector(d_perihelion["earth"],0,0)
'''
planet=["halley","mars","earth"]

planet_dict={"halley":halley,"mars":mars,"earth":earth}
for i in planet:
    planet_dict[i]=anyball(m=mass[i],v=v_perihelion[i],color=color_set[i],make_trail= true,material=material[i],pos=d_perihelion[i])
'''
planet=[halley,mars,earth]
print "original kenitic_energy:",earth.kenitic_energy()
print "original potential_energy:",earth.potential_energy()
print "total energy:",earth.kenitic_energy()+earth.potential_energy()
print "-------------------------------------------------------------"

t=0



dt=86400
while true:
    rate(1000)
   
#    earth.pos+=earth.v*dt
#    earth.v+=(g_force(earth.m,earth.pos)/earth.m)*dt
#    mars.pos+=mars.v*dt
#    mars.v+=(g_force(mars.m,mars.pos)/mars.m)*dt
#    halley.pos+=halley.v*dt
#    halley.v+=(g_force(halley.m,halley.pos)/halley.m)*dt
    
    for i in planet:
        i.pos+=i.v*dt
        i.v+=(g_force(i.m,i.pos)/i.m)*dt

    print diff_angle(vector(d_perihelion["earth"],0,0),earth.pos)
    if diff_angle(vector(d_perihelion["earth"],0,0),earth.pos)==0 and t!=0:
        print "earth period:",dt
    t+=dt
   
    


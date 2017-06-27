from visual import*
pos,axis=vector(0,0,0),vector(0,1,0)
scene=display(width=800,height=800,range=10,background=color.white)
ball=sphere(radius=1.0,material=materials.earth)

def keyinput(evt):
    global pos,axis
    move={"left":vector(-0.1,0,0),"right":vector(0.1,0,0),"up":vector(0,0.1,0.1)
          ,"down":vector(0,-0.1,0),"i":vector(0,0,-0.1),"o":vector(0,0,0.1)}
    axel={"c":vector(0.02,-0.02,0),"r":vector(-0.02,0.02,0)}
    s=evt.key
    if s in move:
        pos=pos+move[s]
        if s in axel:
            axis=axis+axel[s]

scene.bind("keydown",keyinput)
while true:
    rate(200)
    ball.rotate(angle=pi/600,axis=axis,origin=pos)
    ball.pos=pos

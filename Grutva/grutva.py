# Jai shree ram
    
import pygame
import pymunk
import pymunk.pygame_util
import math
import tkinter as tk

pygame.init()

screen = pygame.display.Info() 
pygame.display.set_caption('GRUTVA')
Icon = pygame.image.load('grutva.png')
pygame.display.set_icon(Icon)
WIDTH, HEIGHT = screen.current_w - 25, screen.current_w - 650 

opacity = 100
colors = {"red":(255,0,0,opacity), "green":(0, 128, 0, opacity), "purple":(128, 0, 128, opacity), "yellow":	(255, 195, 0, opacity), "blue":(0, 255, 255, opacity), "black":(0, 0, 0, opacity)}

window = pygame.display.set_mode((WIDTH, HEIGHT))
size = [10, 10]
current_shape = "ball"
current_color = "red"
current_mass = 10
current_elasticiy = 0.9
current_friction = 0.4
current_gravity = 981
current_size = [10,10]

def create_boundaries(space, width, height):
    rects =[
        [(width/2, height-10), (width, 20)],
        [(width/2, 10), (width, 20)],
        [(10, height/2), (20, height)],
        [(width - 10, height/2), (20, height)]
    ]
    for pos, size in rects:
        body = pymunk.Body(body_type=pymunk.Body.STATIC)
        body.position = pos
        shape = pymunk.Poly.create_box(body, size)
        shape.elasticity = 0.4
        shape.friction = 0.5
        space.add(body, shape)

def draw(window, space, draw_options):
    window.fill((173,255,255, 100))
    space.debug_draw(draw_options)
    pygame.display.update()

def change_object(obj):
    global current_shape
    
    current_shape = obj

def change_color(color):
    global current_color
    print(color,current_color)
    current_color = color

def change_mass(val):
    global current_mass
    current_mass = val

def change_friction(val):
    global current_friction
    current_friction = val

def change_elasticity(val):
    global current_elasticiy
    current_elasticiy = val

def change_gravity(val):
    global current_gravity
    current_gravity = val

def change_size_x(val):
    global current_size
    current_size[0] = val

def change_size_y(val):
    global current_size
    print(current_size )
    current_size[1] = val

def pop_up():
    root = tk.Tk()
    root.geometry('450x340')
    root.title("setting") 
    root.iconbitmap("atom.ico")
    
    # shapes
    shapes = tk.Label(root, text="Shapes :")
    shapes.grid(row = 0, column = 0)
    ball_select = tk.Button(root, text ="ball", command =lambda: change_object("ball"))
    ball_select.grid(row = 1, column = 1, pady = 2, padx=3)
    box_select = tk.Button(root, text ="box", command =lambda: change_object("box"))
    box_select.grid(row = 1, column = 2, pady = 2, padx =3)
    spring_select = tk.Button(root, text ="pogo", command = lambda: change_object("pogo"))
    spring_select.grid(row = 1, column = 3, pady = 2, padx = 3)
    
    x = 5
    # colors
    colorsL = tk.Label(root, text="colors :")
    colorsL.grid(row = 2, column = 0)
    red_sel =  tk.Button(root, text ="    ", command = lambda: change_color("red"), background="red")
    red_sel.grid(row = 3, column = 1, pady = 2, padx = x)
    blue_sel = tk.Button(root, text ="    ", command = lambda: change_color("blue"), background="blue")
    blue_sel.grid(row = 3, column = 2, pady = 2, padx = x)
    green_sel = tk.Button(root, text ="    ", command = lambda: change_color("green"), background="green")
    green_sel.grid(row = 3, column = 3, pady = 2, padx = x)
    purple_sel = tk.Button(root, text ="    ", command = lambda: change_color("purple"), background="purple")
    purple_sel.grid(row = 3, column = 4, pady = 2, padx = x)
    black_sel = tk.Button(root, text ="    ", command = lambda: change_color("black"), background="black")
    black_sel.grid(row = 3, column = 5, pady = 2, padx = x)
    yellow_sel = tk.Button(root, text ="    ", command = lambda: change_color("yellow"), background="yellow")
    yellow_sel.grid(row = 3, column = 6, pady = 2, padx = x)
    
    massL = tk.Label(root, text="mass :")
    massL.grid(row=4,column=0, pady=2)
    mass_inp = tk.Text(root, height = 1,width = 3)
    mass_inp.grid(row=4,column=1, pady=2, padx=x)
    mass_sub =  tk.Button(root, text ="set", command = lambda: change_mass(int(mass_inp.get(1.0, "end-1c"))))
    mass_sub.grid(row=4,column=2,padx=x,pady=2)

    frictionL = tk.Label(root, text="friction:")
    frictionL.grid(row=5,column=0, pady=2)
    friction_inp = tk.Text (root, height = 1,width = 3)
    friction_inp.grid(row=5,column=1, pady=2, padx=x)
    friction_sub =  tk.Button(root, text ="set", command = lambda:change_friction(int(friction_inp.get(1.0, "end-1c"))))
    friction_sub.grid(row=5,column=2,padx=x,pady=2)
    
    elasticityL = tk.Label(root, text="elasticity :")
    elasticityL.grid(row=6,column=0, pady=2)
    elasiticity_inp = tk.Text(root, height = 1,width = 3)
    elasiticity_inp.grid(row=6,column=1, pady=2, padx=x)
    elasiticity_sub =  tk.Button(root, text ="set", command = lambda: change_elasticity(int(elasiticity_inp.get(1.0, "end-1c"))))
    elasiticity_sub.grid(row=6,column=2,padx=x,pady=2)
    
    gravityL = tk.Label(root, text="gravity :")
    gravityL.grid(row=7,column=0, pady=2)
    gravity_inp = tk.Text(root, height = 1,width = 3)
    gravity_inp.grid(row=7,column=1, pady=2, padx=x)
    gravity_sub = tk.Button(root, text ="set", command = lambda: change_gravity(int(gravity_inp.get(1.0, "end-1c"))))
    gravity_sub.grid(row=7,column=2,padx=x,pady=2)
    
    sizeL = tk.Label(root, text="size x :")
    sizeL.grid(row=8,column=0, pady=2)
    size_inp = tk.Text(root, height = 1,width = 3)
    size_inp.grid(row=8,column=1, pady=2, padx=x)
    size_sub = tk.Button(root, text ="set", command = lambda: change_size_x(int(size_inp.get(1.0, "end-1c"))))
    size_sub.grid(row=8,column=2,padx=x,pady=2)

    sizeLy = tk.Label(root, text="size y :")
    sizeLy.grid(row=9,column=0, pady=2)
    size_inpy = tk.Text(root, height = 1,width = 3)
    size_inpy.grid(row=9,column=1, pady=2, padx=x)
    size_suby = tk.Button(root, text ="set", command = lambda: change_size_y(int(size_inpy.get(1.0, "end-1c"))))
    size_suby.grid(row=9,column=2,padx=x,pady=2)
    root.mainloop()

def addpogo(space,m0=9,m1=1,length=200,stiffness=800,damping=5,size=40,e=1):
        x0, y0 = pygame.mouse.get_pos()
        b0 = pymunk.Body(mass=m0,moment=1e99)
        b0.position = (x0,y0)
        c0 = pymunk.Poly.create_box(b0, (0.2*size*m0, size))
        c0.elasticity = e
        b1 = pymunk.Body(mass=m1,moment=1e99)
        b1.position = (x0,y0+length)
        c1 = pymunk.Poly.create_box(b1, (0.2*size*m1, size))
        c1.elasticity = e
        # space.add(b0, c0, b1, c1)
        joint = pymunk.DampedSpring(a=b0, b=b1, 
            anchor_a=(0,0), anchor_b=(0,0), 
            rest_length=length, stiffness=stiffness, damping=damping)
        space.add(b0, c0, b1, c1, joint)

def create_object(space, size, position):
    global colors, current_color, current_mass

    body = pymunk.Body(body_type = pymunk.Body.DYNAMIC) 
    body.position = position
    if current_shape == "ball":
        shape = pymunk.Circle(body, size[0])
    elif current_shape == "box":
        shape = pymunk.Poly.create_box(body,(current_size[0],current_size[1]))
    elif current_shape == "pogo":
        addpogo(space)
        return 
    shape.mass = current_mass
    shape.elasticity = current_elasticiy
    shape.friction = current_friction
    shape.color = colors[current_color]
    print(current_color,colors[current_color])
    space.add(body, shape)
    return shape
 
def run(window, width, height):
    global current_gravity, current_size
    run = True
    clock = pygame.time.Clock()
    fps = 60
    delta = 1/fps
    space = pymunk.Space()
    
    draw_options = pymunk.pygame_util.DrawOptions(window)

    create_boundaries(space, width, height)
    while run:
        space.gravity = (0, current_gravity)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
            if event.type == pygame.MOUSEBUTTONDOWN:
                position = pygame.mouse.get_pos()
                object_ = create_object(space, current_size, position) 
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pop_up()
        space.step(delta)
        clock.tick(fps)
        draw(window, space, draw_options)
    pygame.quit 

if __name__ == "__main__":
    run(window, WIDTH, HEIGHT)
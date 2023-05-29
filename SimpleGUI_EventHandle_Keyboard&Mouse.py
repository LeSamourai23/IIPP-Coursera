import simpleguitk as simplegui

height= 1000
width= 1000
position= [height/2, width/2]
velocity= 50 

def key_handler(key):
    if key == simplegui.KEY_MAP["up"]:
        position[1] = position[1] - velocity

    elif key == simplegui.KEY_MAP["down"]:
        position[1] = position[1] + velocity

    elif key == simplegui.KEY_MAP["left"]:
        position[0] = position[0] - velocity

    elif key == simplegui.KEY_MAP["right"]:
        position[0] = position[0] + velocity

def mouse_handler(mouse_pos):
    global position
    position = mouse_pos

def draw_handler(canvas):
    canvas.draw_circle(position, 50, 10, 'aqua', 'aqua')

frame = simplegui.create_frame("Event", width, height)
frame.set_keydown_handler(key_handler)
frame.set_mouseclick_handler(mouse_handler)
frame.set_draw_handler(draw_handler)
frame.start()

import simpleguitk as simplegui

position = [500, 500]
velocity = 50
timer= 1000
display= True

def timer_handler():
    global display
    display = not display

def draw_handler(canvas):
    if display:
        canvas.draw_image(image, (200, 200), (2000, 2000), position, (200, 200))

def key_handler(key):
    
    global position
    
    if key == simplegui.KEY_MAP["up"]:
        position[1]= position[1]-50
        sound.play()

    elif key == simplegui.KEY_MAP["down"]:
        position[1]= position[1] + 50
        sound.play()

    elif key == simplegui.KEY_MAP["left"]:
        position[0]= position[0] - 50
        sound.play()

    elif key == simplegui.KEY_MAP["right"]:
        position[0]= position[0] + 50
        sound.play()

def mouse_handler(click):
    global position
    position = click
    sound.play()


image= simplegui.load_image("https://img.freepik.com/free-photo/yellow-tenis-ball_144627-21443.jpg")
sound= simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/Epoq-Lepidoptera.ogg")  #replace the sound by tennis ball stock sound

frame= simplegui.create_frame("Tennis", 1000, 1000)
frame.set_draw_handler(draw_handler)
frame.set_keydown_handler(key_handler)
frame.set_mouseclick_handler(mouse_handler)
frame.set_canvas_background("white")

timer= simplegui.create_timer(timer, timer_handler)

timer.start()
frame.start()